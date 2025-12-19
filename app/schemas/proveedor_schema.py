from pydantic import BaseModel, Field,ConfigDict
from typing import Optional


class ProveedorBase(BaseModel):
    nombre: str = Field(..., title="Nombre del proveedor", max_length=100)
    telefono: Optional[str] = Field(None, title="Teléfono del proveedor", max_length=15)
    email: Optional[str] = Field(None, title="Correo electrónico del proveedor", max_length=100)
    
class ProveedorCreate(ProveedorBase):
    pass
class ProveedorUpdate(ProveedorBase):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
class ProveedorResponse(ProveedorBase):
    id: int = Field(..., title="ID del proveedor")
    
    model_config = ConfigDict(from_attributes=True)
