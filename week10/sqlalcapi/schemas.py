from pydantic import BaseModel


class STodo(BaseModel):
    id: int
    task: str
    done: bool


class STodoCreate(BaseModel):
    task: str
    done: bool = None

