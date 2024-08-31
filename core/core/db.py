from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración para DB por defecto (sqlite3)
SQILTE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Configuración para DB PostgreSQL
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<nombre_de_base_de_datos>',
        'USER': 'postgres',
        'PASSWORD': '<contraseña_base_de_datos>',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}