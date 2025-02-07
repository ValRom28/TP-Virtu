# Utiliser l'image de base PHP avec Apache
FROM php:7.4-apache-buster

RUN apt-get update && apt-get install -y \
    fortune \
    imagemagick \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier PHP dans le répertoire racine du serveur
COPY index.php /var/www/html/
COPY images /var/www/html/images
COPY convert.sh /root

# Rendre le script exécutable
RUN chmod +x /root/convert.sh

# Exécuter le script
RUN /root/convert.sh

# Exposer le port 80
EXPOSE 80

# On change l'utilisateur pour plus de sécurité
USER www-data
