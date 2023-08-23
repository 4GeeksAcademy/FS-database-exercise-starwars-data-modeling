import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    
    email = Column(String(250), unique=True,  nullable=False)
    password= Column(String(250), unique=True,  nullable=False)
class Suscripcion(Base):
    __tablename__ = 'suscripcion'

    id_suscripcion = Column(Integer, primary_key=True)   
    user_id = Column(Integer, ForeignKey('user.id'))
    alta= Column(Date, nullable=False )
    baja= Column(Date, nullable=False )

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name_character = Column(String(250))
  
class Planet(Base):
    __tablename__ = 'planet'
   
    id_planet = Column(Integer, primary_key=True)
    name_planet = Column(String(250))
class Film(Base):
    __tablename__ = 'film'
   
    id = Column(Integer, primary_key=True)
    name_film = Column(String(250))
class Film_participaciones(Base):
    __tablename__ = 'film_participaciones'
    
    id = Column(Integer, primary_key=True)
     
    id_character= Column(Integer, ForeignKey('character.id'))
    id_planet= Column(Integer, ForeignKey('planet.id')) 
    id_film=Column(Integer, ForeignKey('film.id'))  
    
class Favorito(Base):
    __tablename__ = 'favorito'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
  
class Favorito_user(Base):
    __tablename__ = 'listaUsuarioFavorito'
 
    id = Column(Integer, primary_key=True)
    lista_user = Column(Integer, ForeignKey('favorito.id'))
    id_character= Column(Integer, ForeignKey('character.id'))
    id_planet= Column(Integer, ForeignKey('planet.id'))
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
