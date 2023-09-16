#!/usr/bin/python3
"""
Script for Define a State Class and
 base Class with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """this Class for State class

    Attribute:
        __tablename__ (str): for The table name of the class
        id (int): for The State Id of the class
        name (str): for The State name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
