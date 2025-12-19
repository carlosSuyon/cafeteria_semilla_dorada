from sqlalchemy import Column, Integer, String, DateTime,ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.domain import Base

class Alerta(Base):
    __tablename__ = 'alertas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime, nullable=False)
    mensaje = Column(String(255), nullable=False)
    leida = Column(Boolean, default=False)
    
    origen_id = Column(Integer, ForeignKey('origenes_lote.id'))
    origen_id = relationship("OrigenLote", back_populates="alertas")
