from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import pandas as pd

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://usuario:contraseña@localhost/dbname")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_orders_df():
    with engine.connect() as conn:
        return pd.read_sql("SELECT * FROM orders", conn)
