SECRET_KEY=django-insecure-88888888888888888888888888888888888888888888888888
DEBUG=True

DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=motivator
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=127.0.0.1
DB_PORT=5432

EMAIL_PORT=465
EMAIL_USE_SSL=True
EMAIL_HOST=smtp.yandex.ru
TEST_EMAIL_LOGIN=mail
TEST_EMAIL_PASSWORD=pass

CACHE_ENABLED=True
CACHE_LOCATION=redis://127.0.0.1:6379

CELERY_BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379
CELERY_TIMEZONE=Europe/Moscow
CELERY_TASK_TRACK_STARTED=True

# Адреса через запятую (можно оставить пустым)
# http://localhost:8000 автоматически добавляется при дебаге
CORS_ALLOWED_ORIGINS=http://localhost:8000,http://localhost:8000,http://localhost:8000

TELEGRAM_BOT_TOKEN=111111:xxxxxx