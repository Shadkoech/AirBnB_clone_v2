#!/usr/bin/python3
"""Python module that defines DBStorage engine"""

from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

all_classes = {'State': State, 'City': City,
               'User': User, 'Place': Place,
               'Review': Review, 'Amenity': Amenity}


class DBStorage:
    """Class that represent DB storage engine. It manages storage
    using SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """ Method that creates and initializes an instance of
        DBStorage """

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query method on the current database session.
        Methods returns a dictionary((<class-name>.<object-id>: <obj>) """

        obj_dict = {}

        if cls:
            cls = all_classes[cls]

        if cls:
            for row in self.__session.query(cls).all():
                obj_dict.update({'{}.{}'.
                                format(row.__class__.__name__, row.id,): row})
        else:
            for key, val in all_classes.items():
                for row in self.__session.query(val):
                    obj_dict.update({'{}.{}'.format(
                        row.__class__.__name__, row.id,): row})
        return obj_dict

    def new(self, obj):
        """Add a new object to the current db"""

        self.__session.add(obj)

    def save(self):
        """Method that commits all changes to the current db"""

        self.__session.commit()

    def delete(self, obj=None):
        """Method that deletes from the current database session (obj)
        incase it is not none"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all the tables in a database and
        initializes a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Method that closes an executing
        SQLALchemy session """
        self.__session.close()
