pipeline {
    agent any

    stages {
        stage('1. Verification') {
            steps {
                echo 'Vérification du code source...'
                sh 'docker --version'
            }
        }
        stage('2. Build & Deploy') {
            steps {
                echo 'Reconstruction de l application Flask...'
                # On demande à Jenkins de relancer l'appli en tâche de fond
                sh 'docker compose up -d --build web-app'
            }
        }
    }
}
