pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t registration:v1 .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                bat 'docker tag registration:v1 varsha028/registration:v1'
                bat 'docker push varsha028/registration:v1'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f C:/Users/pappu/Desktop/Week-2/Week-2/deployment.yaml'
                bat 'kubectl apply -f C:/Users/pappu/Desktop/Week-2/Week-2/service.yaml'
            }
        }
        stage('Automated UI Test') {
            steps {
                bat 'python C:/Users/pappu/Desktop/Week-2/Week-2/test_registration.py'
            }
        }

    }
}
