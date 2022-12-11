from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class ArticleSchema(BaseModel):

    id: Optional[int]
    firstName: Optional[str]


class CommentSchema(ArticleSchema):

    id: Optional[int]
    article_id: Optional[int]

    class Config:
        orm_mode = True


class LenguajeSchema(BaseModel):

    id: Optional[int]
    relation: Optional[str]
    lenguaje: Optional[str]
    time: Optional[int]


class UsuarioSchema(BaseModel):
    id: Optional[int] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    cel: Optional[int] = None
    email: Optional[str] = None
    yersExp: Optional[int] = None
    skills: List[LenguajeSchema] = []

    class Config:
        orm_mode = True


class EmpresasSchema(BaseModel):
    id: Optional[int] = None
    companyname: Optional[str] = None

    class Config:
        orm_mode = True


class VacantesSchema(BaseModel):

    id: Optional[int] = None
    PositionName: Optional[str] = None
    CompanyName: Optional[str] = None
    Salary: Optional[int] = None
    Currency: Optional[str] = None
    VacancyLink: Optional[str] = None
    skills: List[LenguajeSchema] = []
    company: List[EmpresasSchema] = []

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T]


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


######################
class AuthorBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class BookSchema(BookBase):
    authors: List[AuthorBase]
