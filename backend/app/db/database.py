from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



DATABASE_URL = (
    "postgresql+psycopg://insightvault:insightvault"
    "@localhost:5432/insightvault"
)


engine = create_engine(
    DATABASE_URL
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)