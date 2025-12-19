# Importamos la sesión de base de datos
from sqlalchemy.orm import Session
# Importamos el modelo de dominio específico
from app.domain.origen_lote import OrigenLote
# Importamos los esquemas para tipado
from app.schemas import origen_lote_schema 

class OrigenRepository:
    """
    Gestiona el acceso a datos para los orígenes/variedades de café.
    Permite controlar el stock_minimo_kg configurado por el usuario.
    """

    def get_by_id(self, db: Session, origen_id: int):
        """Busca un origen por su ID primario."""
        return db.query(OrigenLote).filter(OrigenLote.id == origen_id).first()

    def get_by_nombre(self, db: Session, nombre: str):
        """Busca un origen por nombre (ej: 'Etiopía Yirgacheffe')."""
        return db.query(OrigenLote).filter(OrigenLote.nombre == nombre).first()

    def create(self, db: Session, origen_data:origen_lote_schema.OrigenLoteCreateSchema):
        """Registra una nueva variedad de café con su stock mínimo."""
        db_origen = OrigenLote (
            nombre=origen_data.nombre,
            descripcion=origen_data.descripcion,
            stock_minimo_kg=origen_data.stock_minimo_kg
        )
        db.add(db_origen)
        db.commit()
        db.refresh(db_origen)
        return db_origen

    def get_all(self, db: Session):
        """Retorna todos los orígenes registrados."""
        return db.query(OrigenLote).all()
    
    def delete(self, db: Session, origen_id: int):
       # Elimina un origen por su ID.(baja lógica)
        origen = db.query(OrigenLote).filter(OrigenLote.id == origen_id).first()
        if origen:
            origen.activo = False # Baja lógica
            db.commit()
        return origen