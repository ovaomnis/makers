from database import Base, engine, SessionLocal
from fastapi import FastAPI, status, Depends, HTTPException
from schemas import STodo, STodoCreate
from models import Todo
from sqlalchemy.orm import Session


Base.metadata.create_all(engine)

app = FastAPI()


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.post('/task', response_model=STodo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: STodoCreate, session: Session = Depends(get_session)):
    todo_db = Todo(task=todo.task)
    session.add(todo_db)
    session.commit()
    return todo_db


@app.get('/')
def read_todo(session: Session = Depends(get_session)):
    todos = session.query(Todo).all()
    return todos


@app.get('/task/{pk}', response_model=STodo)
def read_todo(pk: int, session: Session = Depends(get_session)):
    todo = session.query(Todo).get(pk)
    if not todo:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail={f'There no such todo with pk {pk}'})
    return todo


@app.put('/task/{pk}', response_model=STodo)
def create_todo(pk: int, todo: STodoCreate, session: Session = Depends(get_session)):
    todo_db = session.query(Todo).get(pk)
    if todo:
        todo_db.task = todo.task
        if todo.done != None:
            todo_db.done = todo.done
        session.commit()
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail={f'There no such todo with pk {pk}'})
    return todo_db


@app.delete('/task/{pk}')
def create_todo(pk: int, session: Session = Depends(get_session)):
    todo_db = session.query(Todo).get(pk)
    if todo_db:
        session.delete(todo_db)
        session.commit()
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail={f'There no such todo with pk {pk}'})
    return None



