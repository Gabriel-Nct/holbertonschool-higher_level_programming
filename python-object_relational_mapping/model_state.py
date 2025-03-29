#!/usr/bin/python3
"""
This module defines a State class that inherits from Base.
The class is mapped to a MySQL table named 'states'.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class that defines a State
    Attributes:
        id (int): The state's id
        name (str): The state's name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
