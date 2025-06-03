#!/bin/sh

echo "Esperando o banco iniciar..."
until pg_isready -h db -U userfiap; do
  sleep 2
done

exec python app.py