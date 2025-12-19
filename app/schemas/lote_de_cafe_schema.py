from pydantic import BaseModel, Field
from datetime import date

class LoteBase(BaseModel):
    fecha_compra: date
    cantidad_inicial_kg: float = Field(..., gt=0)
    proveedor_cafe_id: int
    origen_lote_id: int

# Al heredar de LoteBase, LoteCreate SOLO pide los campos de arriba
class LoteCreate(LoteBase):
    pass  

class LoteResponse(LoteBase):
    id: int
    cantidad_actual_kg: float # No es parte del POST(create) pero sí lo mostramos en la respuesta
    
    class Config:
        from_attributes = True