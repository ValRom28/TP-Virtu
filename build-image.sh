#!/bin/bash

# Build des images Docker
docker build -t utilisateurs ./utilisateurs
docker build -t fortune ./fortune
docker build -t flask ./flask
docker build -t clusterswarm ./clusterswarm
docker build -t apache ./apache