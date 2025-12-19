from pydantic import BaseModel, Field,ConfigDict, DateTime,Optional
from domain.movimiento import TipoMovimiento

#Esquema para la creación de un nuevo movimiento, sin el id generado automáticamente. Se utiliza un lote_id en lugar de un objeto lote completo.
class MovimientoCreateSchema(BaseModel):
    tipo: TipoMovimiento = Field(..., description="Tipo de movimiento de café")
    
    cantidad: float = Field(..., gt=0, description="Cantidad de café en kilogramos")
    descripcion: str | None = Field(None, description="Descripción del movimiento")
    fecha: DateTime | None = Field(None, description="Fecha y hora del movimiento")
    
    orden_de_tueste_id:Optional[int] = Field(None, description="ID de la orden de tueste asociada, si aplica")
    lote_id:int = Field(..., description="ID del lote asociado al movimiento")

#Esquema para la respuesta de un movimiento, incluyendo el id generado automáticamente.
class MovimientoResponseSchema(MovimientoCreateSchema):
    id: int = Field(..., description="ID único del movimiento")
    tipo: TipoMovimiento = Field(..., description="Tipo de movimiento de café")
    cantidad: float = Field(..., gt=0, description="Cantidad de café en kilogramos")
    descripcion: str | None = Field(None, description="Descripción del movimiento")
    fecha: DateTime | None = Field(None, description="Fecha y hora del movimiento")
    orden_de_tueste_id:Optional[int] = Field(None, description="ID de la orden de tueste asociada, si aplica")
    lote_id:int = Field(..., description="ID del lote asociado al movimiento")
    
    # Configuración para permitir la creación del esquema a partir de un objeto ORM
    model_config = {ConfigDict: {'from_attributes': True}}

    #Un movimiento no se puede modificar, por lo que no se define un esquema de actualización
    #Un movimiento no se puede eliminar, por lo que no se define un esquema de eliminación
