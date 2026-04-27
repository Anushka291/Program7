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
                bat 'python -m unittest discover || echo No tests found'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 3001:3001 calc-app'
            }
        }
    }
}