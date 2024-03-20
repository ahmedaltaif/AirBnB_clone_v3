#!/usr/bin/python3

""" State Module for HBNB project """

from sqlalchemy.orm import relationship
import models
from models.base_model import Base, BaseModel
from models.city import City
from sqlalchemy.ext.declarative import declarative_base
import shlex
from sqlalchemy import Column, Integer, String


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

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
