
from sqlalchemy import Column, Integer, String,Boolean,Float
from sqlalchemy.orm import relationship
from app.domain.base import Base


class OrigenLote(Base):
    __tablename__ = 'origen_lote'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(String(255), nullable=True)

    #Valor que dispara la alerta de stock bajo para lotes de este origen
    stock_bajo_alerta = Column(Float, nullable=False, default=10.0)

    #Relaciones
    lotes = relationship("LoteDeCafe", back_populates="origen")   
   
    estado_activo = Column(Boolean, default=True, nullable=False)