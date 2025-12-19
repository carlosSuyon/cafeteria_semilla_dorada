# Importamos la sesión de SQLAlchemy para interactuar con la DB
from sqlalchemy.orm import Session
# Importamos el modelo de dominio (la tabla física)
from app.domain.lote_de_cafe import LoteDeCafe
# Importamos los esquemas de Pydantic para tipado y validación
from app.schemas import lote_de_cafe_schema

class LoteRepository:
    """
    Repositorio encargado de las operaciones CRUD para la entidad LoteDeCafe.
    Esta capa aísla la lógica de acceso a datos del resto de la aplicación.
    """

    def get_by_id(self, db: Session, lote_id: int):
        """Busca un lote específico por su ID único."""
        return db.query(LoteDeCafe).filter(LoteDeCafe.id == lote_id).first()

    
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        """Obtiene una lista paginada de todos los lotes."""
        return db.query(LoteDeCafe).offset(skip).limit(limit).all()

    def create(self, db: Session, lote_data: lote_de_cafe_schema.LoteCreate):
        """
        Crea un nuevo registro de lote en la base de datos.
        El peso_actual se inicializa igual al peso_inicial en esta etapa.
        """
        # Convertimos el esquema de Pydantic a un modelo de SQLAlchemy
        db_lote = LoteDeCafe(
            fecha_compra=lote_data.fecha_compra,
            cantidad_inicial_kg=lote_data.cantidad_inicial_kg,
            cantidad_actual_kg=lote_data.cantidad_inicial_kg, # Inicializamos el stock actual igual al inicial
            proveedor_cafe_id=lote_data.proveedor_cafe_id,
            origen_lote_id=lote_data.origen_lote_id,
             
        )
        db.add(db_lote)
        db.commit() # Confirmamos la transacción
        db.refresh(db_lote) # Refrescamos para obtener el ID generado
        return db_lote

    def update_stock(self, db: Session, lote_id: int, nuevo_peso: float):
        """
        Actualiza el peso_actual de un lote. 
        Este método será llamado principalmente por el Servicio de Inventario.
        """
        #Busca el lote por su ID
        db_lote = self.get_by_id(db, lote_id)
        if db_lote:
            # Actualiza el peso actual, se da por sentado que la validación del nuevo peso se hace en otra capa
            db_lote.cantidad_actual_kg = nuevo_peso
            db.commit()
            db.refresh(db_lote)
        return db_lote