# app/routers/lote_router.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

# Importamos la infraestructura (DB)
from app.core.database import get_db
# Importamos el "Controlador" (Service)
from app.services.lote_service import LoteService
# Importamos los "Contratos" de datos (Schemas)
from app.schemas import lote_de_cafe_schema

# Definimos el router con su prefijo y etiquetas para la documentación
router = APIRouter(
    prefix="/lotes",
    tags=["Lotes de Café Verde"]
)

# Instanciamos el Service (Gestor)
# En aplicaciones más grandes, esto se puede inyectar con Depends
lote_service = LoteService()

@router.post("/", response_model=lote_de_cafe_schema.LoteCreate, status_code=status.HTTP_201_CREATED)
def crear_nuevo_lote(lote: lote_de_cafe_schema.LoteCreate, db: Session = Depends(get_db)):
    """
    Endpoint (Boundary) para registrar un nuevo lote.
    Delega la validación y creación al Service (Control).
    """
    return lote_service.crear_lote(db=db, lote_in=lote)

@router.get("/", response_model=List[lote_de_cafe_schema.LoteResponse])
def listar_todos_los_lotes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint para obtener el listado de lotes.
    """
    return lote_service.listar_lotes(db=db, skip=skip, limit=limit)

@router.get("/{lote_id}", response_model=lote_de_cafe_schema.LoteResponse)
def obtener_lote_por_id(lote_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para buscar un lote específico.
    """
    return lote_service.obtener_lote(db=db, lote_id=lote_id)

# Nota: No se implementa DELETE o UPDATE para lotes, ya que no es permitido modificarlos o eliminarlos una vez creados.