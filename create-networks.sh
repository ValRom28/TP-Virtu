#!/bin/bash

# Création des réseaux
docker network create publicswarm --attachable -d overlay
docker network create utilisateurs --attachable -d overlay
docker network create clusterswarm --attachable -d overlay
docker network create flask --attachable -d overlay