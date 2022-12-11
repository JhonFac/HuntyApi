import json
from pprint import pprint
from typing import Generic, List, Optional, TypeVar

import crud
from config import SessionLocal
from fastapi import APIRouter, Depends, HTTPException, Path

# from models import Empresas, User, Usuarios, Vacantes
from models import Article, Book, Comment
from schemas import (
    ArticleSchema,
    BookSchema,
    EmpresasSchema,
    Request,
    Response,
    UsuarioSchema,
    VacantesSchema,
)
from sqlalchemy.orm import Session, joinedload

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ## SECCION DE USUARIOS
# @router.post("/usuarios/create")
# async def create_user_service(request: UsuarioSchema, db: Session = Depends(get_db)):
#     data = Usuarios(
#         nombre=request.nombre,
#         apellido=request.apellido,
#         cel=request.cel,
#         email=request.email,
#     )
#     crud.createRow(db, data)
#     return Response(status="Ok", code="200", message="User created successfully").dict(exclude_none=True)


@router.get("/books", response_model=List[BookSchema])
async def get_books(db: Session = Depends(get_db)):
    db_books = db.query(Book).options(joinedload(Book.authors)).all()
    return db_books


@router.get("/usuarios")
async def get_users(db: Session = Depends(get_db)):
    users = crud.getAllRows(db, Article)
    data = Request(parameter=users)
    # pprint(data.parameter[0])

    for i in data.parameter:
        rows = crud.getRelationRows(db, Comment, i.id)
        data = Request(parameter=rows)
        pprint(rows)
        pprint("")

        # print(data.parameter)
        # r = ["hola", "asdf"]
        # for x in data.parameter:
        #     print(data.parameter[x].id)
        #     # r.append(data.parameter[x].id)
        # i.relation = r

    return Response(status="Ok", code="200", message="Success fetch all data", result=users)


# @router.patch("/usuarios/update")
# async def updateUser(request: UsuarioSchema, db: Session = Depends(get_db)):
#     updateuser = crud.updateUser(db, Usuarios, data=request)
#     return Response(status="Ok", code="200", message="Success update data", result=updateuser)


# @router.delete("/usuarios/delete")
# async def deleteUser(request: UsuarioSchema, db: Session = Depends(get_db)):
#     print(request.id)
#     crud.removeRow(db, Usuarios, id=request.id)
#     return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


# ## SECCION DE VACANTES
# @router.post("/vacantes/create")
# async def create_user_service(request: VacantesSchema, db: Session = Depends(get_db)):
#     data = Vacantes(
#         PositionName=request.PositionName,
#         CompanyName=request.CompanyName,
#         Salary=request.Salary,
#         Currency=request.Currency,
#         VacancyLink=request.VacancyLink,
#     )
#     crud.createRow(db, data)
#     return Response(status="Ok", code="200", message="User created successfully").dict(exclude_none=True)


# @router.get("/vacantes")
# async def get_users(db: Session = Depends(get_db)):
#     users = crud.getAllRows(db, Vacantes)
#     return Response(status="Ok", code="200", message="Success fetch all data", result=users)


# @router.patch("/vacantes/update")
# async def updateUser(request: VacantesSchema, db: Session = Depends(get_db)):
#     updateuser = crud.updateVacate(db, Vacantes, data=request)
#     return Response(status="Ok", code="200", message="Success update data", result=updateuser)


# @router.delete("/vacantes/delete")
# async def deleteUser(request: VacantesSchema, db: Session = Depends(get_db)):
#     print(request.id)
#     crud.removeRow(db, Vacantes, id=request.id)
#     return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


# ## SECCION DE EMPRESAS
# @router.post("/empresas/create")
# async def create_user_service(request: EmpresasSchema, db: Session = Depends(get_db)):
#     data = Empresas(companyname=request.companyname)
#     crud.createRow(db, data)
#     return Response(status="Ok", code="200", message="User created successfully").dict(exclude_none=True)


# @router.get("/empresas")
# async def get_users(db: Session = Depends(get_db)):
#     users = crud.getAllRows(db, Empresas)
#     return Response(status="Ok", code="200", message="Success fetch all data", result=users)


# @router.patch("/empresas/update")
# async def updateUser(request: EmpresasSchema, db: Session = Depends(get_db)):
#     updateuser = crud.updateVacate(db, Empresas, data=request)
#     return Response(status="Ok", code="200", message="Success update data", result=updateuser)


# @router.delete("/empresas/delete")
# async def deleteUser(request: EmpresasSchema, db: Session = Depends(get_db)):
#     print(request.id)
#     crud.removeRow(db, Empresas, id=request.id)
#     return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
