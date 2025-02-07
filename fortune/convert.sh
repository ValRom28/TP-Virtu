#!/usr/bin/env bash

for img in /var/www/html/images/*
do
	convert -resize 800x600 $img $img
done
