#!/bin/bash

check_error () {
    if [[ $? -ne 0 ]]; then
        echo "[!] $1"
        exit 1
    fi
}

flag=$1

echo "[*] Stopping containers"
docker-compose down
check_error "Error while trying to stop containers"

if [[ $flag = "" ]] || [[ $flag = "mysql" ]]; then
    echo "[*] Rebuilding mysql"
    docker-compose build --no-cache mysql
    check_error "Error while trying to build mysql container"
fi

if [[ $flag = "" ]] || [[ $flag = "backend" ]]; then
    echo "[*] Rebuilding backend"
    docker-compose build --no-cache backend
    check_error "Error while trying to build backend container"
fi

if [[ $flag = "" ]] || [[ $flag = "frontend" ]]; then
    echo "[*] Rebuilding frontend"
    docker-compose build --no-cache frontend
    check_error "Error while trying to build frontend container"
fi

echo "[**] Recreating network and linking them"
docker-compose up -d
check_error "Error while trying to link containers"