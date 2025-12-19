from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    Clase base para todos los modelos del dominio.
    Aquí puedes añadir métodos o atributos comunes a todas las tablas,
    como 'created_at' o 'updated_at'.
    """
    pass

