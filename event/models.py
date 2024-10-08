from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from core.database import db

class Event(db.Model):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date_begin = Column(DateTime, default=datetime.now(), onupdate=datetime.now)
    date_end = Column(DateTime, default=datetime.now(), onupdate=datetime.now)
    duration = Column(Integer)
    location = Column(String)
    partners = Column(String)
    description = Column(String)
    participants = Column(String)

    # visuals = Column(String)  # Stocker comme str et gérer la conversion dans la sérialisation
