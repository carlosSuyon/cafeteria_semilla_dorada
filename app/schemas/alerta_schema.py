from pydantic import BaseModel, Field,ConfigDict
from typing import Optional
from datetime import date
from enum import Enum

#Esquema base para alerta
class AlertaBaseSchema(BaseModel):
    __tablename__ = 'alertas'
    mensaje: str = Field(..., description="Mensaje de la alerta")
    fecha: date = Field(..., description="Fecha de creación de la alerta")
    leida: bool = Field(..., description="Indica si la alerta ha sido leída o no")

    origen_id: int

#Esquema para crear una alerta
class AlertaCreateSchema(AlertaBaseSchema):
    pass

#Esquema para responder con los datos de una alerta
class AlertaResponseSchema(AlertaBaseSchema):
    id: int = Field(..., description="ID de la alerta")

    model_config = ConfigDict(from_attributes=True)

