# app/routers/origen_lote_router.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

# Importamos la infraestructura (DB)
from app.core.database import get_db
# Importamos el "Controlador" (Service)
from app.services.origen_lote_service import OrigenLoteService
# Importamos los "Contratos" de datos (Schemas)
from app.schemas import origen_lote_schema

# Definimos el router con su prefijo y etiquetas para la documentación
router = APIRouter(
    prefix="/origenes-lote",
    tags=["Orígenes de Lote"]
)
# Instanciamos el Service (Gestor)
# En aplicaciones más grandes, esto se puede inyectar con Depends
origen_lote_service = OrigenLoteService()

# Crear un nuevo origen de lote -
@router.post("/", response_model=origen_lote_schema.OrigenLotesResponseSchema, status_code=status.HTTP_201_CREATED)
def crear_nuevo_origen_lote(origen_in: origen_lote_schema.OrigenLoteCreateSchema, db: Session = Depends(get_db)):
    """
    Endpoint (Boundary) para registrar un nuevo origen de lote.
    Delega la validación y creación al Service (Control).
    """
    return origen_lote_service.crear_origen_lote(db=db, origen_in=origen_in)    

# Listar todos los orígenes de lote
@router.get("/", response_model=List[origen_lote_schema.OrigenLotesResponseSchema])
def listar_todos_los_origenes_lote(db: Session = Depends(get_db)):
    """
    Endpoint para obtener el listado de orígenes de lote.
    """
    return origen_lote_service.listar_origenes_lote(db=db)
# Obtener un origen de lote por ID
@router.get("/{origen_id}", response_model=origen_lote_schema.OrigenLotesResponseSchema)
def obtener_origen_lote_por_id(origen_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para buscar un origen de lote específico.
    """
    return origen_lote_service.obtener_origen_lote(db=db, origen_id=origen_id)
# Eliminar un origen de lote por ID, en realidad es una baja lógica osea estado_activo = False
@router.delete("/{origen_id}", status_code=status.HTTP_200_OK)
def eliminar_origen_lote(origen_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para eliminar un origen de lote específico.
    """
    return origen_lote_service.eliminar_origen_lote(db=db, origen_id=origen_id)
# Actualizar el stock bajo alerta de un origen de lote
@router.put("/{origen_id}/stock-bajo-alerta", status_code=status.HTTP_200_OK)
def actualizar_stock_bajo_alerta(origen_id: int, nuevo_stock: float, db: Session = Depends(get_db)):
    """
    Endpoint para actualizar el stock bajo alerta de un origen de lote.
    """
    return origen_lote_service.actualizar_stock_bajo_alerta(db=db, origen_id=origen_id, nuevo_stock=nuevo_stock)

#Activar  un origen de lote que estado_activo = False => estado_activo = True
@router.put("/{origen_id}/activar", status_code=status.HTTP_200_OK)
def activar_origen_lote(origen_id: int, activar: bool, db: Session = Depends(get_db)):
    """
    Endpoint para activar   un origen de lote.
    """
    return origen_lote_service.activar_origen_lote(db=db, origen_id=origen_id, activar=activar) 