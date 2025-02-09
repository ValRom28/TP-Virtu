#!/bin/bash

# Build des images Docker
docker build -t utilisateurs:latest ./utilisateurs
docker build -t fortune:latest ./fortune
docker build -t flask:latest ./flask
docker build -t clusterswarm:latest ./clusterswarm
docker build -t apache:latest ./apache