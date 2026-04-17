# Frontend — Autenticación con React + Tailwind

Interfaz frontend desarrollada con React, Vite y Tailwind CSS que se conecta a la API de autenticación del backend.

---

## Stack

| Herramienta | Versión |
|---|---|
| React | 19.x |
| Vite | 8.x |
| Tailwind CSS | 3.x |

---

## Funcionalidades

- Formulario de login con campos de usuario y contraseña.
- Conexión vía `fetch` al endpoint `POST /token` del backend.
- Mensaje de éxito con el access token cuando las credenciales son válidas.
- Mensaje de error descriptivo cuando las credenciales son inválidas o hay un problema de conexión.
- Diseño limpio y responsivo con Tailwind CSS.

---

## Instalación y ejecución local

### Prerrequisitos

- Node.js 18+
- Backend ejecutándose en `http://localhost:8000`

### Pasos

```bash
# Desde la carpeta frontend/
npm install

# Iniciar el servidor de desarrollo
npm run dev
```

La aplicación estará disponible en `http://localhost:5173`.

### Build de producción

```bash
npm run build
```

---

## Credenciales de prueba

Las mismas que acepta el backend:

| Campo | Valor |
|---|---|
| Usuario | `admin` |
| Contraseña | `admin123` |
