from sqlalchemy.orm import Session
from app.repositories.origen_lote_repository import OrigenRepository
from app.schemas import origen_lote_schema
from fastapi import HTTPException, status

class OrigenLoteService:
    def __init__(self):
        # Instanciamos el repositorio para uso interno
        self.origen_lote_repository = OrigenRepository()
    
    def crear_origen_lote(self, db: Session, origen_in: origen_lote_schema.OrigenLoteCreateSchema):
        """
        Lógica para dar de alta un nuevo origen de lote.
        """
        # 1. Normalización y verificación de duplicados
        nombre_normalizado = origen_in.nombre.strip().capitalize()
        existente = self.origen_repo.get_by_nombre(db, nombre=nombre_normalizado)
        if existente:
            if not existente.estado_activo:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El origen de lote ya existe pero está inactivo. Por favor, actívelo en lugar de crear uno nuevo."
                )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El origen de lote con este nombre ya existe."
            )
        origen_in.nombre = nombre_normalizado
        #Si todo está bien, creamos el nuevo origen
        return self.origen_lote_repository.create(db, origen_data=origen_in)
    
    def obtener_origen_lote(self, db: Session, origen_id: int):
        """Obtiene un origen de lote y valida su existencia."""
        origen = self.origen_lote_repository.get_by_id(db, origen_id=origen_id)
        if not origen:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El origen de lote especificado no existe"
            )
        return origen
    
    def listar_origenes_lote(self, db: Session, skip: int = 0, limit: int = 100):
        """Lista todos los orígenes de lote con paginación."""
        return self.origen_lote_repository.get_all(db, skip=skip, limit=limit)
        
    def eliminar_origen_lote(self, db: Session, origen_id: int):
        """Elimina un origen de lote por su ID."""
        origen = self.origen_lote_repository.get_by_id(db, origen_id=origen_id)
        if not origen:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El origen de lote especificado no existe"
            )
        self.origen_lote_repository.delete(db, origen_id=origen_id)
        return {"detail": "Origen de lote eliminado exitosamente"}

    #Modificar el stock minimo de alerta
    def actualizar_stock_bajo_alerta(self, db: Session, origen_id: int, nuevo_stock: float):
        """Actualiza el stock bajo alerta de un origen de lote."""
        origen = self.origen_lote_repository.get_by_id(db, origen_id=origen_id)
        if not origen:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El origen de lote especificado no existe"
            )
        origen.stock_bajo_alerta = nuevo_stock
        db.commit()
        db.refresh(origen)
        return origen
    
    #Activar un origen de lote
    def activar_origen_lote(self, db: Session, origen_id: int):
        """Activa un origen de lote que estaba inactivo."""
        origen = self.origen_lote_repository.get_by_id(db, origen_id=origen_id)
        if not origen:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El origen de lote especificado no existe"
            )
        origen.estado_activo = True
        db.commit()
        db.refresh(origen)
        return origen