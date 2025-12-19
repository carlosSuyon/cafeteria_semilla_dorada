from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Si usas SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./cafeteria.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para los routers/servicios
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
