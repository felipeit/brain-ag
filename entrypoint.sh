#!/bin/bash
set -e

echo ">> Executando migrações do Django..."
python manage.py migrate

echo ">> Restaurando os dados iniciais no banco do Django..."
python manage.py loaddata db.json

python manage.py runserver 0.0.0.0:8000