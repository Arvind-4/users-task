from django.conf import settings
from backend.utils import get_env_value

DJANGO_PG_HOST = get_env_value("DJANGO_PG_HOST")
DJANGO_PG_DATABASE = get_env_value("DJANGO_PG_DATABASE")
DJANGO_PG_USER = get_env_value("DJANGO_PG_USER")
DJANGO_PG_PASSWORD = get_env_value("DJANGO_PG_PASSWORD")

if all([DJANGO_PG_HOST, DJANGO_PG_DATABASE, DJANGO_PG_USER, DJANGO_PG_PASSWORD]):
    print("Using PostgreSQL database")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DJANGO_PG_DATABASE,
            "USER": DJANGO_PG_USER,
            "PASSWORD": DJANGO_PG_PASSWORD,
            "HOST": DJANGO_PG_HOST,
            "PORT": 5432,
            "OPTIONS": {
                "sslmode": "require",
            },
        }
    }

else:
    print("Using SQLite database")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": settings.BASE_DIR / "db.sqlite3",
        }
    }
