# models.py
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

Base = declarative_base()

class SmartLocation(Base):
    __tablename__ = 'epa_sld_database_v3'

    objectid = Column(Integer, primary_key=True, index=True)
    shape = Column(Geometry(geometry_type='MULTIPOLYGON', srid=102039))
