#!/usr/bin/python3
"""
Script for Defines State class and
base class with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """this class for State class

    Attributes:
        __tablename__ (str): for The table name of the class
        id (int): for The State id of the class
        name (str): for The State name of the class
        cities (:obj:`City`): for The Cities belongs to State

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
