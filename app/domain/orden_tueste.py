from sqlalchemy import Column, Integer, Float, Enum, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from app.domain.base import Base
import datetime
import enum

class PerfilTueste(str, enum.Enum):
    CLARA = "CLARA"
    MEDIA = "MEDIA"
    OSCURA = "OSCURA"

class OrdenDeTueste(Base):
    __tablename__ = 'ordenes_de_tueste'
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    fecha = Column(DateTime, default=datetime.datetime.utcnow)

    stock_cafe_verde_kg = Column(Float, nullable=False)  # Cantidad de café verde a tostar
    stock_tostado_kg = Column(Float, nullable=False)  # Cantidad de café tostado producido
    merma_kg = Column(Float, nullable=False)  # Pérdida durante el proceso de tueste

    perfil_tueste = Column(Enum(PerfilTueste), nullable=False)

    # Relaciones
    movimientos = relationship("Movimiento", back_populates="orden_de_tueste")
    maquina_id = Column(Integer, ForeignKey('maquinas.id'), nullable=False)
