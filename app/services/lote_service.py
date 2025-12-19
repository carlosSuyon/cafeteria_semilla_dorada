# Importamos la sesión de base de datos
from sqlalchemy.orm import Session
# Importamos los repositorios necesarios para las validaciones
from app.repositories.lote_de_cafe_repository import LoteRepository
from app.repositories.origen_lote_repository import OrigenRepository
from app.repositories.proveedor_cafe_repository import ProveedorRepository
# Importamos los esquemas y excepciones
from app.schemas import lote_de_cafe_schema
from fastapi import HTTPException, status

class LoteService:
    """
    Capa de lógica de negocio para la gestión de Lotes de Café Verde.
    Orquesta las validaciones antes de permitir operaciones en la DB.
    """

    def __init__(self):
        # Instanciamos los repositorios para uso interno
        self.lote_repo = LoteRepository()
        self.origen_repo = OrigenRepository()
        self.proveedor_repo = ProveedorRepository()

    #Relacionado con el metodo @app.post("/lotes/", response_model=lote_schema.Lote) de REST API
    def crear_lote(self, db: Session, lote_in: lote_de_cafe_schema.LoteCreate):
        """
        Lógica para dar de alta un nuevo lote con validaciones de integridad.
        """
        # 1. Validar que el origen exista y esté activo (Borrado Lógico)
        origen = self.origen_repo.get_by_id(db, origen_id=lote_in.origen_lote_id)
        if not origen:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El origen especificado no existe o no está activo"
            )

        # 2. Validar que el proveedor exista y esté activo
        # (Asumiendo que lote_in tiene proveedor_id)
        proveedor = self.proveedor_repo.get_by_id(db, proveedor_id=lote_in.proveedor_cafe_id)
        if not proveedor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El proveedor especificado no existe o no está activo"
            )

        # 4. Si todas las validaciones pasan, delegar la creación al repositorio
        return self.lote_repo.create(db, lote_data=lote_in)

    # Relacionado con el metodo @app.get("/lotes/{lote_id}", response_model=lote_schema.Lote) de REST API
    def obtener_lote(self, db: Session, lote_id: int):
        """Obtiene un lote y valida su existencia."""
        lote = self.lote_repo.get_by_id(db, lote_id=lote_id)
        if not lote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Lote no encontrado"
            )
        return lote

    # Relacionado con el metodo @app.get("/lotes/", response_model=List[lote_schema.Lote]) de REST API
    def listar_lotes(self, db: Session, skip: int = 0, limit: int = 100):
        """Retorna la lista de lotes paginada."""
        return self.lote_repo.get_all(db, skip=skip, limit=limit)
    
    #Un lote no se puede eliminar si ya ha sido registrado en una compra