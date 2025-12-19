from sqlalchemy.orm import Session
from app.domain.orden_tueste import OrdenDeTueste
from app.repositories.orden_tueste_repository import OrdenTuesteRepository
from app.schemas import orden_tueste_schema
from fastapi import HTTPException, status

class OrdenTuesteService:
    """
    Capa de lógica de negocio para la gestión de Órdenes de Tueste.
    Orquesta las validaciones antes de permitir operaciones en la DB.
    """

    def __init__(self):
        # Instanciamos el repositorio para uso interno
        self.orden_tueste_repo = OrdenTuesteRepository()

    def crear_orden_tueste(self, db: Session, orden_in: orden_tueste_schema.OrdenDeTuesteBaseSchema):
        """
        Lógica para dar de alta una nueva orden de tueste con validaciones de integridad.
        """
        #Validaciones específicas pueden ir aquí
        #Validar que los stocks sean positivos
        if orden_in.stock_cafe_verde_kg < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El stock de café verde no puede ser negativo"
            )
        if orden_in.stock_tostado_kg < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El stock de café tostado no puede ser negativo"
            )
        if orden_in.merma_kg < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La merma no puede ser negativa"
            )
        #Validar que el perfil de tueste sea válido
        if orden_in.perfil_tueste not in ["CLARA", "MEDIA", "OSCURA"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Perfil de tueste inválido"
            )   
        #Validar que stock_verde_kg sea menor o igual al stock en los lotes disponibles para tostar
        

        # Delegar la creación al repositorio
        return self.orden_tueste_repo.create(db, orden_data=orden_in)

    def obtener_orden_tueste(self, db: Session, orden_id: int):
        """Obtiene una orden de tueste y valida su existencia."""
        orden = self.orden_tueste_repo.get_by_id(db, orden_id=orden_id)
        if not orden:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Orden de tueste no encontrada"
            )
        return orden

    def listar_ordenes_tueste(self, db: Session, skip: int = 0, limit: int = 100):
        """Lista órdenes de tueste con paginación."""
        return self.orden_tueste_repo.get_all(db, skip=skip, limit=limit)