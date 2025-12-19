from pydantic import BaseModel, Field, ConfigDict, DateTime, conlist,Optional
from domain.orden_tueste import PerfilTueste    

class OrdenDeTuesteBaseSchema(BaseModel):
    fecha_tueste: DateTime
    stock_verde_kg: float = Field(..., gt=0)
    stock_tostado_kg: float = Field(..., gt=0)
    perfil_tueste: PerfilTueste
    merma_kg: float = Field(..., ge=0)

class OrdenDeTuesteCreateSchema(OrdenDeTuesteBaseSchema):
    id: Optional[int] = None
    pass
class OrdenDeTuesteResponseSchema(OrdenDeTuesteBaseSchema):
    class Config:
        from_attributes = True
