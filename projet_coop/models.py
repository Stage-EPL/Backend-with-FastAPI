from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from core.database import db

class Project(db.Model):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date_begin = Column(DateTime, default=datetime.now(), onupdate=datetime.now)
    date_end = Column(DateTime, default=datetime.now(), onupdate=datetime.now)
    duration = Column(Integer)
    project_type = Column(String)
    partners = Column(String)
    description = Column(String)

    # visuals = Column(String)  # Stocker comme str et gérer la conversion dans la sérialisation
