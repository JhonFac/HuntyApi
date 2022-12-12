from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class LenguajeSchema(BaseModel):

    # id: Optional[int]
    skill: Optional[str]
    time: Optional[int]

    class Config:
        orm_mode = True


class UsuarioSchema(BaseModel):
    # id: Optional[int] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    cel: Optional[int] = None
    email: Optional[str] = None
    yersExp: Optional[int] = None
    lenguajes: List[LenguajeSchema] = []
    matchProfile: List[LenguajeSchema] = []

    class Config:
        orm_mode = True


class EmpresasSchema(BaseModel):
    id: Optional[int] = None
    companyname: Optional[str] = None

    class Config:
        orm_mode = True


class VacantesSchema(BaseModel):

    # id: Optional[int] = None
    positionName: Optional[str] = None
    companyName: Optional[str] = None
    salary: Optional[int] = None
    currency: Optional[str] = None
    vacancyLink: Optional[str] = None
    lenguajes: List[LenguajeSchema] = []
    # company: List[EmpresasSchema] = []

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T]


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class JoinSkill(UsuarioSchema):
    lenguajes: List[LenguajeSchema]


class JoinvacansiesSkill(VacantesSchema):
    lenguajes: List[LenguajeSchema]
