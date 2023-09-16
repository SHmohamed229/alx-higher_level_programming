#!/usr/bin/python3
"""
Script for Define a City class
with MySQLAlchemy ORM.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """this class for City class

    Attributes:
        __tablename__ (str): for The Table name of the class
        id (int): for The Id of the class
        name (str): for The name of Class
        state_id (int): for The state City belongs to

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
