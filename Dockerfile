# On part d'une image officielle Python ultra-légère
FROM python:3.10-slim

# On définit le dossier de travail à l'intérieur du conteneur
WORKDIR /app

# On copie le fichier requirements pour installer les dépendances en premier (optimisation du cache)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# On copie tout le reste de notre code dans le conteneur
COPY . .

# On expose le port 5000 utilisé par Flask
EXPOSE 5000

# Commande exécutée lors du lancement du conteneur
CMD ["python", "app.py"]
