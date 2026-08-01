#!bin/bash

docker compose -f piHole/docker-compose.yml up -d
docker compose -f openSpeedTest/docker-compose.yml up -d
