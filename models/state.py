#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from models import storage_type
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City",  backref="state", cascade="delete")

    else:
        name = ""

        @property
        def cities(self):
            """Method that returns the list of City instances
            with state_id equals to the current State.id
            """
            from models import storage
            cities = []

            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    cities.append(city)
            return cities
