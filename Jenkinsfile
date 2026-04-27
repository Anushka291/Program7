pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-app .'
            }
        }

        stage('Run App (Manual Mode)') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    bat 'docker run -p 5001:5001 --name calculator-container flask-app'
                }
            }
        }
        
    }

    post {
        success {
            echo '✅ BUILD COMPLETED'
        }
        failure {
            echo '❌ BUILD FAILED'
        }
    }
}