#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from os import getenv
import shlex
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            var = models.storage.all()
            lista = []
            result = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.state_id == self.id):
                    result.append(elem)
            return (result)
            """list_city = []
            city_list = list(models.storage.all(City).values())
            for city in city_list:
                if states.id == self.id:
                    list_city.append(city)
            return list_city"""
