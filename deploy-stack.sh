#!/bin/bash

# Déploiement des stacks
docker stack deploy -c utilisateurs/docker-compose.yml utilisateurs --detach
docker stack deploy -c fortune/docker-compose.yml fortune --detach
docker stack deploy -c flask/docker-compose.yml flask --detach
docker stack deploy -c clusterswarm/docker-compose.yml clusterswarm --detach
docker stack deploy -c apache/docker-compose.yml apache --detach