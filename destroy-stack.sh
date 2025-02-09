#!/bin/bash

# Suppression des stacks
docker stack rm utilisateurs
docker stack rm fortune
docker stack rm flask
docker stack rm clusterswarm
docker stack rm apache