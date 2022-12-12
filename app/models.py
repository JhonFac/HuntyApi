import datetime

from config import Base
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import backref, relationship

join_skill = Table(
    "join_skill",
    Base.metadata,
    Column("user_id", ForeignKey("usuarios.id"), primary_key=True),
    Column("skill_id", ForeignKey("lenguajes.id"), primary_key=True),
)

join_skill_vacansies = Table(
    "join_skill_vacansies",
    Base.metadata,
    Column("vacansies_id", ForeignKey("vacantes.id"), primary_key=True),
    Column("skill_id", ForeignKey("lenguajes.id"), primary_key=True),
)

company_vacansies = Table(
    "company_vacansies",
    Base.metadata,
    Column("company_id", ForeignKey("empresas.id"), primary_key=True),
    Column("vacansies_id", ForeignKey("vacantes.id"), primary_key=True),
)


class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    lenguajes = relationship("Lenguajes", secondary="join_skill", back_populates="usuarios")
    firstName = Column(String)
    lastName = Column(String)
    cel = Column(Integer)
    email = Column(String)
    yersExp = Column(Integer)


class Lenguajes(Base):
    __tablename__ = "lenguajes"

    id = Column(Integer, primary_key=True)
    usuarios = relationship("Usuarios", secondary="join_skill", back_populates="lenguajes")
    vacantes = relationship("Vacantes", secondary="join_skill_vacansies", back_populates="lenguajes")
    skill = Column(String)
    time = Column(Integer)


class Vacantes(Base):
    __tablename__ = "vacantes"

    id = Column(Integer, primary_key=True, index=True)
    lenguajes = relationship("Lenguajes", secondary="join_skill_vacansies", back_populates="vacantes")
    empresas = relationship("Empresas", secondary="company_vacansies", back_populates="vacantes")
    positionName = Column(String)
    companyName = Column(String)
    salary = Column(Integer)
    currency = Column(String)
    vacancyLink = Column(String)


class Empresas(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    companyname = Column(String)
    vacantes = relationship("Vacantes", secondary="company_vacansies", back_populates="empresas")
