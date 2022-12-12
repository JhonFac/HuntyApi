# from models import Usuarios
from schemas import UsuarioSchema
from sqlalchemy.orm import Session


# Querys Generales
def getAllRows(db: Session, model):
    return db.query(model).all()


def getRowsById(db: Session, model, id: int):
    return db.query(model).filter(model.id == id).first()


def createRow(db, data):
    print(data)
    db.add_all(data)
    db.commit()
    return data


def removeRow(db: Session, model, id: int):
    user = getRowsById(db, model, id)
    db.delete(user)
    db.commit()


def getRelationRows(db: Session, model, id: int):
    return db.query(model).filter(model.article_id == id)


# # update para usuarios
# def updateUser(db: Session, model, data):
#     user = getRowsById(db, model, data.id)

#     user.cell = data.cel
#     user.nombre = data.nombre
#     user.apellido = data.apellido
#     user.email = data.email

#     db.commit()
#     db.refresh(user)
#     return user


# # update para usuarios
# def updateVacate(db: Session, model, data):
#     print(data)
#     vacante = getRowsById(db, model, data.id)

#     vacante.PositionName = data.PositionName
#     vacante.CompanyName = data.CompanyName
#     vacante.Salary = data.Salary
#     vacante.Currency = data.Currency
#     vacante.VacancyLink = data.VacancyLink

#     db.commit()
#     db.refresh(vacante)
#     return vacante


# # update para empresas
# def updateVacate(db: Session, model, data):
#     print(data)
#     company = getRowsById(db, model, data.id)

#     company.companyname = data.companyname

#     db.commit()
#     db.refresh(company)
#     return company
