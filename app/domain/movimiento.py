from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.domain.base import Base
import datetime
import enum

class TipoMovimiento(str, enum.Enum):
    ENTRADA = "ENTRADA"           # Compra inicial de café verde
    TUESTE = "TUESTE"             # Salida para producción
    MUESTRA = "MUESTRA"           # Control de calidad / Catación
    AJUSTE_NEGATIVO = "AJUSTE_-"  # Pérdida, humedad, error de pesaje
    AJUSTE_POSITIVO = "AJUSTE_+"  # Corrección de inventario

class Movimiento(Base):
    __table__name__ = 'movimientos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    tipo = Column(Enum(TipoMovimiento), nullable=False)
    cantidad = Column(Float, nullable=False)
    descripcion = Column(String(255), nullable=True)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)

    #Relaciones
    id_lote = Column(Integer, ForeignKey('lotes.id'), nullable=False)
    lote = relationship("Lote", back_populates="movimientos")

    orden_de_tueste_id = Column(Integer, ForeignKey('ordenes_de_tueste.id'), nullable=True)
    orden_de_tueste = relationship("OrdenDeTueste", back_populates="movimientos")