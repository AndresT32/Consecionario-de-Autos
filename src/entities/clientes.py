import uuid

from sqlalchemy import Boolean, Column, DateTime, String,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base


class Cliente(Base):
    __tablename__ = "tbl_Cliente"

    id_Cliente = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
    Apellido = Column(String(50),  nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    Direccion = Column(String(100), default=True, unique = True)
    Tipo_Cliente = Column(String(50), nullable=False)
    

    # Por si el Cliente va a tener acceso al sistema:
    #id_usuario = Column(UUID, ForeignKey("tbl_usuarios.id"), nullable=True)
    #Usuario = relationship("Usuario", foreign_keys=[id_usuario])