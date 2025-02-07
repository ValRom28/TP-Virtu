# Utiliser l'image de base PHP avec Apache
FROM php:7.4-apache

# Installer l'extension MySQLi
RUN docker-php-ext-install mysqli && \
    pecl install -f redis && \
    docker-php-ext-enable redis

# Copier le fichier PHP dans le répertoire racine du serveur
COPY index.php /var/www/html/

# Exposer le port 80
EXPOSE 80
