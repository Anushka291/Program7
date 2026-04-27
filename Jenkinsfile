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
                    bat 'docker rm -f flask-container || exit 0'
                    bat 'docker run -p 3001:3001 --name flask-container flask-app'
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
        always {
            bat 'docker rm -f flask-container || exit 0'
        }
    }
}