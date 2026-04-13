# Backend — JWT Authentication API

FastAPI application that exposes JWT-based authentication endpoints.

---

## Stack

| Herramienta | Versión |
|---|---|
| Python | 3.11 |
| FastAPI | 0.111.x |
| Uvicorn | 0.30.x |
| python-jose | 3.3.x |
| bcrypt | 4.x |
| Poetry | 1.8.x |

---

## Endpoints

### `POST /token` — Obtener tokens

Autentica al usuario y devuelve un **access token** (expira en **300 segundos**) y un **refresh token** (expira en 24 horas).

**Request body (JSON):**

```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response:**

```json
{
  "access_token": "<jwt>",
  "refresh_token": "<jwt>",
  "token_type": "bearer"
}
```

---

### `POST /token/refresh` — Refrescar tokens

Recibe un refresh token válido y devuelve un nuevo par de tokens.

**Request body (JSON):**

```json
{
  "refresh_token": "<jwt>"
}
```

**Response:**

```json
{
  "access_token": "<new_jwt>",
  "refresh_token": "<new_jwt>",
  "token_type": "bearer"
}
```

---

## Documentación interactiva

Una vez levantada la aplicación, la documentación Swagger está disponible en:

```
http://localhost:8000/docs
```

---

## Instalación y ejecución local (con Poetry)

### Prerrequisitos

- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation) instalado

### Pasos

```bash
# Desde la carpeta backend/
poetry install

# Iniciar el servidor de desarrollo
poetry run uvicorn app.main:app --reload --port 8000
```

La API quedará disponible en `http://localhost:8000`.

---

## Ejecución con Docker

### Construir la imagen

```bash
# Desde la carpeta backend/
docker build -t jwt-backend .
```

### Ejecutar el contenedor

```bash
docker run -p 8000:8000 jwt-backend
```

La API quedará disponible en `http://localhost:8000`.

---

## Ejemplo de uso con curl

### 1. Obtener tokens

```bash
curl -X POST http://localhost:8000/token \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

### 2. Refrescar tokens

```bash
curl -X POST http://localhost:8000/token/refresh \
  -H "Content-Type: application/json" \
  -d '{"refresh_token": "<refresh_token_aquí>"}'
```

---

## Variables de entorno (producción)

Para mayor seguridad en producción se recomienda externalizar las siguientes constantes de `app/auth.py` como variables de entorno:

| Variable | Descripción |
|---|---|
| `SECRET_KEY` | Clave secreta para firmar los JWT (⚠️ obligatorio cambiar en producción) |
| `ACCESS_TOKEN_EXPIRE_SECONDS` | Tiempo de expiración del access token (default: 300) |
| `REFRESH_TOKEN_EXPIRE_SECONDS` | Tiempo de expiración del refresh token (default: 86400) |
