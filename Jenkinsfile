pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Akalya-Dharshini/Jenkins-flask-docker-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-cicd-app:latest .'
            }
        }

        stage('Deploy Docker Container') {
            steps {
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                docker run -d -p 80:5000 --name flask-app flask-cicd-app:latest
                '''
            }
        }
    }
}
