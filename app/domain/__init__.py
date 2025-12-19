# app/domain/__init__.py

from .base import Base
from .lote_de_cafe import LoteDeCafe        # 👈 Antes tenías 'lote_de_cafe'
from .origen_lote import OrigenLote        # 👈 Verifica que coincida con el nombre de la clase
from .proveedor_cafe import ProveedorCafe  # 👈 Verifica que coincida con el nombre de la clase

# Esto permite que Base.metadata contenga todas las tablas registradas