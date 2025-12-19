from sqlalchemy  import Column, Integer, Float,Enum
from sqlalchemy.orm import relationship
from app.domain.base import Base
import datetime
import enum

class TipoDeProducto(str,enum.Enum):
   CAFE_TOSTADO = "CAFE TOSTADO" 
   BEBIDA = "BEBIDA"
   ACCESORIO ="ACCESORIO"
   CONFITERIA ="CONFITERIA"

class Producto(Base):
    __tablename__ = "Productos"
    id = Column(Integer, primary_key=True,autoincrement=True)
    precio_venta = Column(Float,nullable=False)
    tipo_producto = Column(Enum(TipoDeProducto), nullable=False)
    
