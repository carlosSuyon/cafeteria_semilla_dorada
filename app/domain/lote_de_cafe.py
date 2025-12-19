#Importaciones y dependencias
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.domain.base import Base
from sqlalchemy.orm import relationship

#Clase lote_de_cafe POO
class LoteDeCafe(Base):
    __tablename__ = 'lote_de_cafe'
    id : int = Column(Integer, primary_key=True, autoincrement=True)
    fecha_compra : Date = Column(Date, nullable=False)
    cantidad_inicial_kg : float = Column(Float, nullable=False)
    cantidad_actual_kg : float = Column(Float, nullable=False)

    proveedor_cafe = relationship("proveedor_cafe", back_populates="lotes_de_cafe")
    proveedor_cafe_id : int = Column(Integer, ForeignKey("proveedor_cafe.id"), nullable=False)

    origen_lote = relationship("origen_lote", back_populates="lotes_de_cafe")
    origen_lote_id : int = Column(Integer, ForeignKey("origen_lote.id"), nullable=False)

    
    def get_stock(self):
        return self.cantidad_actual_kg