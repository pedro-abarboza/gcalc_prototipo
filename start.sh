#!/bin/bash

set -e

# Verificar se estamos no Docker e ajustar o hostname se necessário
HOST_IP=$DB_HOST
if [ "$DB_HOST" = "localhost" ] || [ "$DB_HOST" = "127.0.0.1" ]; then
    # Verificar se estamos rodando em um container Docker
    if [ -f /.dockerenv ]; then
        echo "Detectado ambiente Docker, ajustando hostname para host.docker.internal..."
        # Em Docker, 'localhost' dentro do container não é o mesmo que 'localhost' do host
        # host.docker.internal aponta para o host em Docker Desktop (Mac/Windows)
        # Para Linux, o equivalente seria usar a gateway IP do Docker
        HOST_IP="host.docker.internal"
        # Configurar /etc/hosts para Linux se necessário
        if [ ! -z "$(grep -i linux /etc/os-release)" ]; then
            DOCKER_GATEWAY=$(ip route | grep default | cut -d' ' -f3)
            if [ ! -z "$DOCKER_GATEWAY" ]; then
                HOST_IP=$DOCKER_GATEWAY
            fi
        fi
        export DB_HOST=$HOST_IP
        echo "Usando $HOST_IP para conectar ao banco de dados no host."
    fi
fi

# Garantir que a porta esteja definida
PORT=${PORT:-8000}
echo "Iniciando servidor na porta $PORT"

# Tentar conectar ao banco de dados (sem bloquear)
echo "Verificando a conexão com o banco de dados em $DB_HOST:$DB_PORT..."
python -c "
import sys
import psycopg2
import os
import time

host = os.environ.get('DB_HOST', 'localhost')
port = os.environ.get('DB_PORT', '5432')
dbname = os.environ.get('DB_NAME', 'gcalc')
user = os.environ.get('DB_USER', 'postgres')
password = os.environ.get('DB_PASSWORD', 'postgres')

print(f'Tentando conectar ao banco: {host}:{port}/{dbname} como {user}')
try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    conn.close()
    print('Conexão com o banco de dados estabelecida!')
except Exception as e:
    print(f'Aviso: Não foi possível conectar ao banco de dados: {e}')
    print('Certifique-se de que as variáveis de ambiente DB_* estão configuradas corretamente.')
    print('O aplicativo continuará, mas pode falhar se o banco não estiver disponível.')
" || echo "Verificação de banco de dados concluída com avisos."

# Executa migrações
echo "Aplicando migrações..."
python manage.py migrate || echo "Falha nas migrações - verifique a conexão com o banco de dados"


# Configura com base no ambiente
if [ "$ENV" = "production" ]; then
    echo "Iniciando em modo de produção..."
    
    # Inicia o servidor Gunicorn para produção
    if [ -n "$GUNICORN_WORKERS" ]; then
        WORKERS=$GUNICORN_WORKERS
    else
        # Cálculo automático de workers (2 * CPU cores + 1)
        WORKERS=$((2 * $(grep -c processor /proc/cpuinfo) + 1))
    fi
    
    echo "Iniciando Gunicorn com $WORKERS workers na porta $PORT..."
    exec gunicorn core.wsgi:application \
        --bind 0.0.0.0:$PORT \
        --workers $WORKERS \
        --timeout ${GUNICORN_TIMEOUT:-120} \
        --access-logfile ${GUNICORN_ACCESS_LOG:-'-'} \
        --error-logfile ${GUNICORN_ERROR_LOG:-'-'}
else
    echo "Iniciando em modo de desenvolvimento..."
    # Inicia o servidor Django development
    python manage.py runserver 0.0.0.0:$PORT
fi 