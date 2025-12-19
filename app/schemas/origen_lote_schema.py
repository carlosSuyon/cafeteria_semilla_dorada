from pydantic import BaseModel, Field,ConfigDict
from typing import Optional


class OrigenLoteSchema(BaseModel):
    nombre: str = Field(..., max_length=100)
    descripcion: Optional[str] = Field(None, max_length=255)
    
    stock_bajo_alerta: float = Field(default=10.0, ge=0 )


class OrigenLoteCreateSchema(OrigenLoteSchema):
    pass

class OrigenLotesResponseSchema(OrigenLoteSchema):
    #Solo se agrega el id para las respuestas porque es el unico campo extra que tiene el modelo
    id: int
    # Esto permite que apartir del objeto ORM se pueda crear el esquema (JSON response)
    model_config = ConfigDict(from_attributes=True)