from fastapi import FastAPI, Depends, HTTPException
import crud
import models
import schemas
from sqlalchemy.orm import Session
from queue_worker import send_message_to_queue
from database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello, World!"}


@app.post("/links", response_model=schemas.Link)
def create_link(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    db_link = crud.create_link(db, link)
    send_message_to_queue(db_link)
    return db_link


@app.get("/links/{link_id}", response_model=schemas.Link)
def get_link(link_id: int, db: Session = Depends(get_db)):
    db_link = crud.get_link(db, link_id=link_id)
    if db_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_link


@app.put("/links/{link_id}", response_model=schemas.Link)
def update_link(link_id: int, link: schemas.LinkUpdate, db: Session = Depends(get_db)):
    db_link = crud.update_link(db, link_id=link_id, link_update=link)
    if db_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_link
