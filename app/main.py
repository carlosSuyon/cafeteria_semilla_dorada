from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine
from app.domain import Base # Aquí importas la Base que ya conoce a todos los modelos
from app.core.database import SessionLocal
from app.routes import lote_router, orige_lote_router,proveedor_router
#Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

#Aqui se crea la instancia de FastAPI
app = FastAPI(
    title="La Semilla Dorada API",
    version="1.0.0"
)

#Registrar los routers
app.include_router(lote_router.router)
app.include_router(orige_lote_router.router)
app.include_router(proveedor_router.router)
#Configurar CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes (en producción, especificar dominios)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Ruta /health para verificar que la API está funcionando correctamente
@app.get("/health")
def health_check():
    return {"status": "ok"}

#Para ejecutar la aplicación, use el siguiente comando:
# uvicorn app.main:app --reload