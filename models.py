from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    is_active = Column(Boolean, default=True)
    full_name = Column(String(100), nullable=True)
    email = Column(String(100), unique=True, nullable=True)
    role = Column(String(50), default="user")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', active={self.is_active})>"

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    origen = Column(String(100), nullable=False)
    destino = Column(String(100), nullable=False)
    estado = Column(String(50), nullable=False)
    tiempo_estimado_min = Column(Integer, nullable=False)
    hora_salida = Column(String(30), nullable=False)

    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, estado='{self.estado}')>"

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
