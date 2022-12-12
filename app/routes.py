from pprint import pprint

import crud
from config import SessionLocal
from controller import *
from fastapi import APIRouter, Depends, HTTPException, Path
from models import *
from schemas import *
from sqlalchemy.orm import Session, joinedload

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


## SECCION DE USUARIOS
@router.post("/usuarios/create")
async def create_user_service(request: UsuarioSchema, db: Session = Depends(get_db)):
    createUserRelation(request, db)
    return Response(status="Ok", code="200", message="User created successfully").dict(exclude_none=True)


@router.get("/usuarios", response_model=List[JoinSkill])
async def get_books(db: Session = Depends(get_db)):
    return db.query(Usuarios).options(joinedload(Usuarios.lenguajes)).all()


@router.patch("/usuarios/update")
async def updateUser(request: UsuarioSchema, db: Session = Depends(get_db)):
    updateuser = crud.updateUser(db, Usuarios, data=request)
    return Response(status="Ok", code="200", message="Success update data", result=updateuser)


@router.delete("/usuarios/delete")
async def deleteUser(request: UsuarioSchema, db: Session = Depends(get_db)):
    crud.removeRow(db, Usuarios, id=request.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


## SECCION DE VACANTES
@router.post("/vacantes/create")
async def create_user_service(request: JoinvacansiesSkill, db: Session = Depends(get_db)):
    createVacanciesRelation(request, db)
    return Response(status="Ok", code="200", message="User created successfully").dict(exclude_none=True)


@router.get("/vacantes", response_model=List[JoinvacansiesSkill])
async def get_users(db: Session = Depends(get_db)):
    return db.query(Vacantes).options(joinedload(Vacantes.lenguajes)).all()


@router.patch("/vacantes/update")
async def updateUser(request: VacantesSchema, db: Session = Depends(get_db)):
    updateuser = crud.updateVacate(db, Vacantes, data=request)
    return Response(status="Ok", code="200", message="Success update data", result=updateuser)


@router.delete("/vacantes/delete")
async def deleteUser(request: VacantesSchema, db: Session = Depends(get_db)):
    print(request.id)
    crud.removeRow(db, Vacantes, id=request.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


## SECCION DE EMPRESAS
@router.post("/empresas/create")
async def create_user_service(request: EmpresasSchema, db: Session = Depends(get_db)):
    data = Empresas(companyname=request.companyname)
    crud.createRow(db, data)
    return Response(status="Ok", code="200", message="User created successfully").dict(exclude_none=True)


@router.get("/empresas")
async def get_users(db: Session = Depends(get_db)):
    users = crud.getAllRows(db, Empresas)
    return Response(status="Ok", code="200", message="Success fetch all data", result=users)


@router.patch("/empresas/update")
async def updateUser(request: EmpresasSchema, db: Session = Depends(get_db)):
    updateuser = crud.updateVacate(db, Empresas, data=request)
    return Response(status="Ok", code="200", message="Success update data", result=updateuser)


@router.delete("/empresas/delete")
async def deleteUser(request: EmpresasSchema, db: Session = Depends(get_db)):
    print(request.id)
    crud.removeRow(db, Empresas, id=request.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
