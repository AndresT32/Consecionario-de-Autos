import uuid

from sqlalchemy import Boolean, Column, DateTime, String,Numeric,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base


class Auto(Base):
    __tablename__ = "tbl_Auto"

    id_Auto = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    Marca = Column(String(50), nullable=False)
    Modelo = Column(String(50),nullable=False)
    Tipo_Auto = Column(String(50),nullable=False)
    Precio = Column(Numeric(10,2),nullable=False)
    Estado = Column(Boolean,default=True)

        # --- Auditoria ---

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    id_usuario_crea = Column(
        UUID(as_uuid=True), ForeignKey("tbl_usuario.id_Usuario"), nullable=False
    )
    id_usuario_edita = Column(
        UUID(as_uuid=True), ForeignKey("tbl_usuario.id_Usuario"), nullable=True
    )

    usuario_crea = relationship("Usuario", foreign_keys=[id_usuario_crea])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])

    # --- Llaves foráneas ---
    id_Sucursal = Column(
        UUID(as_uuid=True), ForeignKey("tbl_Sucursal.id_Sucursal"), nullable=False
    )
    id_Compra = Column(
        UUID(as_uuid=True), ForeignKey("tbl_Compra.id_Compra"), nullable=False
    )
    # --- Relationships ---
    Sucursal = relationship("Sucursal", foreign_keys=[id_Sucursal])
    Compra = relationship("Compra", foreign_keys=[id_Compra])