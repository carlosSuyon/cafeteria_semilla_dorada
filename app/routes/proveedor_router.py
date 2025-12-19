from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

# Importamos la infraestructura (DB)
from app.core.database import get_db
# Importamos el "Controlador" (Service)
from app.services.proveedor_service import ProveedorService
# Importamos los "Contratos" de datos (Schemas)
from app.schemas import proveedor_schema

# Definimos el router con su prefijo y etiquetas para la documentación
router = APIRouter(
    prefix="/proveedores",
    tags=["Proveedores de Café"]
)
# Instanciamos el Service (Gestor)
# En aplicaciones más grandes, esto se puede inyectar con Depends
proveedor_service = ProveedorService()
# Crear un nuevo proveedor de café verde
@router.post("/", response_model=proveedor_schema.ProveedorResponse, status_code=status.HTTP_201_CREATED)
def crear_nuevo_proveedor(proveedor_in: proveedor_schema.ProveedorCreate, db: Session = Depends(get_db)):
    """
    Endpoint (Boundary) para registrar un nuevo proveedor de café verde.
    Delega la validación y creación al Service (Control).
    """
    return proveedor_service.crear_proveedor(db=db, proveedor_in=proveedor_in)

# Listar todos los proveedores de café verde
@router.get("/", response_model=List[proveedor_schema.ProveedorResponse])
def listar_todos_los_proveedores(db: Session = Depends(get_db)):
    """
    Endpoint para obtener el listado de proveedores de café verde.
    """
    return proveedor_service.listar_proveedores(db=db)  

# Obtener un proveedor de café verde por ID
@router.get("/{proveedor_id}", response_model=proveedor_schema.ProveedorResponse)
def obtener_proveedor_por_id(proveedor_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para buscar un proveedor de café verde específico.
    """
    return proveedor_service.obtener_proveedor(db=db, proveedor_id=proveedor_id)
# Eliminar un proveedor de café verde por ID
@router.delete("/{proveedor_id}", status_code=status.HTTP_200_OK)
def eliminar_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para eliminar un proveedor de café verde específico.
    """
    return proveedor_service.eliminar_proveedor(db=db, proveedor_id=proveedor_id)

# Actualizar un proveedor de café verde por ID
@router.put("/{proveedor_id}", response_model=proveedor_schema.ProveedorResponse, status_code=status.HTTP_200_OK)
def actualizar_proveedor(proveedor_id: int, proveedor_in: proveedor_schema.ProveedorUpdate, db: Session = Depends(get_db)):
    """
    Endpoint para actualizar un proveedor de café verde específico.
    """
    return proveedor_service.actualizar_proveedor(db=db, proveedor_id=proveedor_id, proveedor_in=proveedor_in)

#Activar un proveedor de café verde que estado_activo = False => estado_activo = True
@router.put("/{proveedor_id}/activar", status_code=status.HTTP_200_OK)
def activar_proveedor(proveedor_id: int, activar: bool, db: Session = Depends(get_db)):
    """
    Endpoint para activar un proveedor de café verde.
    """
    return proveedor_service.activar_proveedor(db=db, proveedor_id=proveedor_id, activar=activar)
