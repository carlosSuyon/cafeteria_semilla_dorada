from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.orm import relationship
from app.domain.base import Base

class ProveedorCafe(Base):
    __tablename__ = "proveedor_cafe"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    telefono = Column(String(20), nullable=True)
    estado_activo = Column(Boolean, default=True, nullable=False)

    #Relacion inversa con LoteDeCafe
    lotes_de_cafe = relationship("LoteDeCafe", back_populates="proveedor_cafe")