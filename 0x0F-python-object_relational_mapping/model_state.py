#!/usr/bin/python3
"""
This script defines a Base class to
combine  Table, Mapper() and class object
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Attributes:
    __tablename__ (str): The table name of the class
    id (int): The State id of the class
    name (str): The State name of the class
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
