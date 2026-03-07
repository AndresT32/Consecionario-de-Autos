import uuid

from sqlalchemy import Boolean, Column, DateTime, String,Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from src.database.config import Base


class Empleado(Base):
    __tablename__ = "tbl_Empleado"

    id_Empleado = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Nombre = Column(String(50), nullable=False)
    Cargo = Column(String(50), nullable=False)
    Telefono = Column(String(50), nullable=False)
    Salario = Column(Numeric(10,2), nullable=False)

