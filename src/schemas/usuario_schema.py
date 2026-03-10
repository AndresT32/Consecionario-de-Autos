"""Esquemas de validación Pydantic para la entidad Usuario."""

from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

class UsuarioBase(BaseModel):
    """Atributos base de un Usuario."""
    nombre: str
    nombre_usuario: str
    email: EmailStr
    telefono: Optional[str] = None
    activo: Optional[bool] = True

class UsuarioCreate(UsuarioBase):
    """Esquema para creación de Usuario requerida contraseña."""
    contraseña_hash: str

class UsuarioUpdate(BaseModel):
    """Esquema para actualización parcial de Usuario."""
    nombre: Optional[str] = None
    nombre_usuario: Optional[str] = None
    email: Optional[EmailStr] = None
    contraseña_hash: Optional[str] = None
    telefono: Optional[str] = None
    activo: Optional[bool] = None

class UsuarioResponse(UsuarioBase):
    """Esquema de respuesta que omite la contraseña."""
    id_Usuario: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
