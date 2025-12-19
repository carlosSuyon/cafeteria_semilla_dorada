from sqlalchemy.orm import Session
from app.repositories.proveedor_cafe_repository import ProveedorRepository
from app.schemas import proveedor_schema
from fastapi import HTTPException, status


class ProveedorService:
    def __init__(self):
        # Instanciamos el repositorio para uso interno
        self.proveedor_repository = ProveedorRepository()
    
    def crear_proveedor(self, db: Session, proveedor_in: proveedor_schema.ProveedorCreate):
        """
        Lógica para dar de alta un nuevo proveedor de café verde.
        """
        #Validar que el email del proveedor no esté duplicado
        proveedor_existente = self.proveedor_repository.get_by_id(db, nombre=proveedor_in.nombre)
        if proveedor_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ya existe un proveedor registrado con ese email {proveedor_in.email}"
            )
        
        # Si la validación pasa, delegar la creación al repositorio
        return self.proveedor_repository.create(db, proveedor_data=proveedor_in)
    
    def obtener_proveedor(self, db: Session, proveedor_id: int):
        """Obtiene un proveedor y valida su existencia."""
        proveedor = self.proveedor_repository.get_by_id(db, proveedor_id=proveedor_id)
        if not proveedor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El proveedor especificado no existe"
            )
        return proveedor
    
    def listar_proveedores(self, db: Session, skip: int = 0, limit: int = 100):
        """Lista todos los proveedores con paginación."""
        return self.proveedor_repository.get_all(db, skip=skip, limit=limit)
    
    def eliminar_proveedor(self, db: Session, proveedor_id: int):
        """Elimina un proveedor por su ID."""
        proveedor = self.proveedor_repository.get_by_id(db, proveedor_id=proveedor_id)
        if not proveedor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El proveedor especificado no existe"
            )
        self.proveedor_repository.delete(db, proveedor_id=proveedor_id)
        return {"detail": "Proveedor eliminado exitosamente"}
    
    def actualizar_proveedor(self, db: Session, proveedor_id: int, proveedor_in: proveedor_schema.ProveedorUpdate):
        """Actualiza un proveedor por su ID."""
        proveedor = self.proveedor_repository.get_by_id(db, proveedor_id=proveedor_id)
        if not proveedor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El proveedor especificado no existe"
            )
        # Delegar la actualización al repositorio
        return self.proveedor_repository.update(db, proveedor_id=proveedor_id, proveedor_data=proveedor_in)

#Activar un proveedor de café verde que estado_activo = False => estado_activo = True
def activar_proveedor(self, db: Session, proveedor_id: int, activar: bool):
    proveedor = self.proveedor_repository.get_by_id(db, proveedor_id=proveedor_id)

    #Validar si el proveedor existe
    if not proveedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El proveedor especificado no existe"
        )
    #Si proveedor.estado_activo ya es igual a activar, no hacer nada
    if proveedor.estado_activo == activar:
        return proveedor
    #Actualizar el estado_activo del proveedor usando el repositorio
    return self.proveedor_repository.activar_proveedor(db, proveedor_id=proveedor_id)
    