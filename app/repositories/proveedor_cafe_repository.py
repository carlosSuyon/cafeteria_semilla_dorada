# Importamos la sesión de base de datos
from sqlalchemy.orm import Session
# Importamos el modelo de dominio específico
from app.domain.proveedor_cafe import ProveedorCafe
# Importamos los esquemas para tipado
from app.schemas import proveedor_schema

class ProveedorRepository:
    """
    Repositorio para la gestión de proveedores de café verde.
    """

    def get_by_id(self, db: Session, proveedor_id: int):
        """Busca un proveedor por su ID."""
        return db.query(ProveedorCafe).filter(ProveedorCafe.id == proveedor_id).first()

    def get_by_nombre(self, db: Session, nombre: str):
        """Busca un proveedor por su nombre comercial."""
        return db.query(ProveedorCafe).filter(ProveedorCafe.nombre == nombre).first()

    def create(self, db: Session, proveedor_data: proveedor_schema.ProveedorCreate):
        """Crea un nuevo registro de proveedor en la base de datos."""
        db_proveedor = ProveedorCafe(
            nombre=proveedor_data.nombre,
            telefono=proveedor_data.telefono,
            email=proveedor_data.email,
        )
        db.add(db_proveedor)
        db.commit()
        db.refresh(db_proveedor)
        return db_proveedor

    def get_all(self, db: Session):
        """Lista todos los proveedores activos."""
        return db.query(ProveedorCafe).all()
    
    def delete(self, db: Session, proveedor_id: int):
        """Elimina un proveedor por su ID. Marca como inactivo en lugar de eliminar físicamente."""
        proveedor = db.query(ProveedorCafe).filter(ProveedorCafe.id == proveedor_id).first()
        if proveedor:
            proveedor.activo = False # Marcamos como inactivo en lugar de eliminar físicamente
            db.commit()
        return proveedor
    
    def update(self, db: Session, proveedor_id: int, proveedor_data: proveedor_schema.ProveedorUpdate):
        """Actualiza un proveedor existente."""
        proveedor = db.query(ProveedorCafe).filter(ProveedorCafe.id == proveedor_id).first()
        if proveedor:
            for var, value in vars(proveedor_data).items():
                if value is not None:
                    setattr(proveedor, var, value)
            db.commit()
            db.refresh(proveedor)
        return proveedor
    
    #Activar un proveedor
    def activar_proveedor(self, db: Session, proveedor_id: int):
        """Activa un proveedor que estaba inactivo."""
        proveedor = db.query(ProveedorCafe).filter(ProveedorCafe.id == proveedor_id).first()
        if proveedor:
            proveedor.activo = True
            db.commit()
            db.refresh(proveedor)
        return proveedor