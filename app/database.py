from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Actualiza esta URL para que coincida con tu docker-compose.yml
SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@localhost:5433/supermercado_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia para obtener la sesión de la BD en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()