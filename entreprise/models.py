from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from core.database import db

class Entreprise(db.Model):
    __tablename__ = "entreprises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    domain = Column(String)
    mail = Column(String)
    address = Column(String)
    site = Column(String)
    logo = Column(String)
    description = Column(String)
    partnership_type = Column(String)
    partnership_date = Column(DateTime, default=datetime.now(), onupdate=datetime.now)

    # visuals = Column(String)  # Stocker comme str et gérer la conversion dans la sérialisation
