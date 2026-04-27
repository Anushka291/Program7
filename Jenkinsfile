pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t calc-app .'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker run --rm calc-app python app.py'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker rm -f calc-container || true'
                bat 'docker run -d -p 3001:3001 --name calc-container calc-app'
            }
        }
    }
}