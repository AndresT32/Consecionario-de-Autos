import pytest
import httpx
import uuid

BASE_URL = "https://consecionario-de-autos-1.onrender.com"
TIMEOUT = 120.0  # 2 minutos para que Render despierte


def test_root_health_check():
    """
    Proposito: Verificar que la API desplegada esta activa y responde.
    Funcionamiento: Hace GET a "/" y comprueba status 200 y mensaje de bienvenida.
    """
    response = httpx.get(f"{BASE_URL}/", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert "message" in data


def test_login_exitoso():
    """
    Proposito: Verificar que el login funciona y retorna un JWT valido.
    Funcionamiento: Envia credenciales validas a /usuarios/login y comprueba
    que la respuesta contiene un access_token.
    """
    payload = {
        "nombre_usuario": "admin2",
        "contraseña": "admin123",
    }
    response = httpx.post(f"{BASE_URL}/auth/login", json=payload, timeout=TIMEOUT, follow_redirects=True)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


def test_listar_clientes():
    """
    Proposito: Verificar que GET /clientes/ responde correctamente.
    Funcionamiento: Hace GET a /clientes/ y comprueba status 200 y lista.
    """
    response = httpx.get(f"{BASE_URL}/clientes/", timeout=TIMEOUT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_crear_y_obtener_cliente():
    """
    Proposito: Verificar el flujo completo de crear y consultar un cliente.
    Funcionamiento: Hace POST con datos validos, extrae el ID y hace GET
    verificando que los datos coinciden.
    """
    email_unico = f"test_{uuid.uuid4().hex[:8]}@pytest.com"
    payload = {
        "nombre": "Test",
        "Apellido": "Pytest",
        "email": email_unico,
        "telefono": "3001234567",
        "Direccion": f"Calle {uuid.uuid4().hex[:6]}",
        "Tipo_Cliente": "Natural",
    }
    create_response = httpx.post(f"{BASE_URL}/clientes/", json=payload, timeout=TIMEOUT)
    assert create_response.status_code == 201
    cliente_id = create_response.json()["id_Cliente"]

    get_response = httpx.get(f"{BASE_URL}/clientes/{cliente_id}", timeout=TIMEOUT)
    assert get_response.status_code == 200
    assert get_response.json()["email"] == email_unico


def test_cliente_no_existente_retorna_404():
    """
    Proposito: Verificar que buscar un cliente con ID inexistente retorna 404.
    Funcionamiento: Hace GET con un UUID que no existe y comprueba que retorna 404.
    """
    uuid_falso = "00000000-0000-0000-0000-000000000000"
    response = httpx.get(f"{BASE_URL}/clientes/{uuid_falso}", timeout=TIMEOUT)
    assert response.status_code == 404
