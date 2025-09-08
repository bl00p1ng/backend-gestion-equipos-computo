# Gestión de Equipos - Sistema CRUD

Sistema web para administrar equipos tecnológicos desarrollado con Flask (Backend) y Angular (Frontend).


## Instalación y Ejecución

### Backend (Flask)
```bash
cd backend
pip install flask flask-cors pymysql python-dotenv
docker-compose up -d  # Iniciar MySQL
python app.py         # Servidor en http://127.0.0.1:5000
```

## Funcionalidades

- ✅ **Crear** equipos (descripción + email responsable)
- ✅ **Listar** todos los equipos en tarjetas
- ✅ **Editar** equipos existentes (modal)
- ✅ **Eliminar** equipos con confirmación

## Base de Datos

Tabla `equipos`:
- `id` - INT AUTO_INCREMENT PRIMARY KEY
- `descripcion` - VARCHAR(255)
- `email` - VARCHAR(255)

## Notas

El sistema utiliza CORS configurado para desarrollo local.