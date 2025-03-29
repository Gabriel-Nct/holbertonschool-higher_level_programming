#!/usr/bin/python3
"""
This module defines a City class that represents a city in a database.
The City class inherits from Base and is linked to the MySQL table cities.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Class definition for a City.
    Inherits from Base and links to the MySQL table cities.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store cities.
        id (int): The city's id, which is the primary key.
        name (str): The name of the city.
        state_id (int): The state's id, which is a foreign key.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)