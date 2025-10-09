pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-id'
        DOCKER_IMAGE = 'abhikkumar04/sci-calc:latest'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Abhik-04/SPE_Mini_Project'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_scientific_calculator.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build(DOCKER_IMAGE)
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
        stage('Deploy Container Locally') {
            steps {
                script {
                    sh 'docker stop sci-calc || true'
                    sh 'docker rm sci-calc || true'
                    sh "docker run -d --name sci-calc ${DOCKER_IMAGE}"
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
