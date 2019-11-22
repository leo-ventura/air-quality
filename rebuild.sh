#!/bin/bash

check_error () {
    if [[ $? -ne 0 ]]; then
        echo "[!] $1"
        exit
    fi
}

echo "[*] Stopping containers"
docker-compose down
check_error "Error while trying to stop containers"

echo "[*] Rebuilding mysql"
docker-compose build --no-cache mysql
check_error "Error while trying to build mysql container"

echo "[*] Rebuilding backend"
docker-compose build --no-cache backend
check_error "Error while trying to build backend container"

echo "[*] Rebuilding frontend"
docker-compose build --no-cache frontend
check_error "Error while trying to build frontend container"

echo "[**] Recreating network and linking them"
docker-compose up -d
check_error "Error while trying to link containers"