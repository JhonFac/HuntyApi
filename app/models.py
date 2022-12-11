import datetime

from config import Base
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import backref, relationship

# class Usuarios(Base):
#     __tablename__ = "usuarios"

#     id = Column(Integer, primary_key=True, index=True)
#     skills = relationship("Lenguajes", backref="relation")
#     firstName = Column(String)
#     lastName = Column(String)
#     cel = Column(Integer)
#     email = Column(String)
#     yersExp = Column(Integer)


# class Vacantes(Base):
#     __tablename__ = "vacantes"

#     id = Column(Integer, primary_key=True, index=True)
#     PositionName = Column(String)
#     CompanyName = Column(String)
#     Salary = Column(Integer)
#     Currency = Column(String)
#     VacancyLink = Column(String)
#     # skills = relationship("Lenguajes", back_populates="id")
#     company = relationship("Empresas")


# class Empresas(Base):
#     __tablename__ = "empresas"

#     id = Column(Integer, primary_key=True, index=True)
#     companyname = Column(String)
#     vacancies = Column(Integer, ForeignKey("vacantes.id"))


# class Lenguajes(Base):
#     __tablename__ = "Lenguajes"

#     id = Column(Integer, primary_key=True, index=True)
#     relation = Column(Integer, ForeignKey("usuarios.id"))
#     # skills = relationship("Usuarios", backref=backref("skills", lazy=True))
#     lenguaje = Column(String)
#     time = Column(Integer)


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    comments = relationship("Comment")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"))


# Declare Classes / Tables
book_authors = Table(
    "book_authors",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("author_id", ForeignKey("authors.id"), primary_key=True),
)


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    authors = relationship("Author", secondary="book_authors", back_populates="books")


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("Book", secondary="book_authors", back_populates="authors")
