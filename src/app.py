from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar los routers de endpoints
from src.endpoints.autos import router as autos_router
from src.endpoints.mantenimientos import router as mantenimientos_router
from src.endpoints.empleados import router as empleados_router
from src.endpoints.ventas import router as ventas_router
from src.endpoints.compras import router as compras_router
from src.endpoints.clientes import router as clientes_router
from src.endpoints.detalle_ventas import router as detalle_ventas_router
from src.endpoints.sucursales import router as sucursales_router
from src.endpoints.usuarios import router as usuarios_router

app = FastAPI(
    title="API Concesionario de Autos",
    description="API para gestionar inventarios, ventas, compras y mantenimientos de un concesionario.",
    version="1.0.0",
)

# Configuración básica de CORS (*)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root path
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API del Concesionario de Autos"}

# Incluir routers
app.include_router(autos_router)
app.include_router(clientes_router)
app.include_router(empleados_router)
app.include_router(ventas_router)
app.include_router(compras_router)
app.include_router(mantenimientos_router)
app.include_router(detalle_ventas_router)
app.include_router(sucursales_router)
app.include_router(usuarios_router)
