from sqlalchemy.orm import Session
from app.domain.orden_tueste import OrdenDeTueste
from app.schemas import orden_tueste_schema

class OrdenTuesteRepository:
    """
    Repositorio encargado de las operaciones CRUD para la entidad OrdenDeTueste.
    Esta capa aísla la lógica de acceso a datos del resto de la aplicación.
    """

    def get_by_id(self, db: Session, orden_id: int):
        """Busca una orden de tueste específica por su ID único."""
        return db.query(OrdenDeTueste).filter(OrdenDeTueste.id == orden_id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        """Obtiene una lista paginada de todas las órdenes de tueste."""
        return db.query(OrdenDeTueste).offset(skip).limit(limit).all()

    def create(self, db: Session, orden_data: orden_tueste_schema.OrdenDeTuesteCreateSchema):
        """
        Crea un nuevo registro de orden de tueste en la base de datos.
        """
        # Convertimos el esquema de Pydantic a un modelo de SQLAlchemy
        db_orden = OrdenDeTueste(
            fecha=orden_data.fecha_tueste,
            stock_cafe_verde_kg=orden_data.stock_verde_kg,
            stock_tostado_kg=orden_data.stock_tostado_kg,
            merma_kg=orden_data.merma_kg,
            perfil_tueste=orden_data.perfil_tueste,
            
        )
        db.add(db_orden)
        db.commit()