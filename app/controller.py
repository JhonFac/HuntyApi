from pprint import pprint

import crud
from models import Lenguajes, Usuarios, Vacantes


def createUserRelation(data, db):

    g = []
    l = []

    user = Usuarios(
        firstName=data.firstName, lastName=data.lastName, cel=data.cel, email=data.email, yersExp=data.yersExp
    )
    for i in data.lenguajes:
        g.append(Lenguajes(skill=i.skill, time=i.time))
        l.append(Lenguajes(skill=i.skill, time=i.time))

    user.lenguajes = l
    g.insert(0, user)

    crud.createRow(db, g)


def createVacanciesRelation(data, db):

    g = []
    l = []

    van = Vacantes(
        positionName=data.positionName,
        companyName=data.companyName,
        salary=data.salary,
        currency=data.currency,
        vacancyLink=data.vacancyLink,
    )

    for i in data.lenguajes:
        g.append(Lenguajes(skill=i.skill, time=i.time))
        l.append(Lenguajes(skill=i.skill, time=i.time))

    van.lenguajes = l
    g.insert(0, van)

    crud.createRow(db, g)
