# Integrante: Fernando Ariel Chandia Molina
# Email: fernando_chandia05@inacapmail.cl

# Proyecto Django: Géneros de Películas

Aplicación web hecha con Django y Bootstrap que muestra un listado de géneros de películas y, al entrar a cada uno, al menos 10 películas con nombre, año e imagen.

## Requisitos previos

- Python 3.10 o superior (marcar "Add Python to PATH" al instalar)
- Git

Verificar:

```powershell
python --version
git --version
```

## Instalación

### 1. Clonar el repositorio

```powershell
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO
```

### 2. Crear y activar el entorno virtual

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la ejecución de scripts:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
venv\Scripts\Activate.ps1
```

En Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

### 4. Aplicar migraciones

```powershell
python manage.py migrate
```

### 5. Ejecutar el servidor

```powershell
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/

## Estructura del proyecto

```
├── manage.py
├── requirements.txt
├── .gitignore
├── templates/
│   └── base.html              # Template base con menú de navegación
├── static/
│   ├── css/                   # Estilos personalizados
│   ├── js/                    # Scripts personalizados
│   └── images/peliculas/      # Imágenes de las películas
└── home_fernando/             # Aplicación principal
    ├── views.py               # Vistas con la data de géneros y películas
    ├── urls.py                # URLs con namespace
    └── templates/home_fernando/
        ├── inicio.html        # Listado de géneros (List group de Bootstrap)
        └── genero.html        # Películas del género (Cards de Bootstrap)
```

## Rutas

| URL | Descripción |
|---|---|
| `/` | Inicio: listado de géneros |
| `/generos/<slug>/` | Películas de un género |
| `/admin/` | Panel de administración de Django |

## Tecnologías

- Python / Django
- Bootstrap 5 (CDN)
- HTML, CSS y JavaScript

## Autores

- Fernando
- Alumno 2
