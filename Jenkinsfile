pipeline {
    agent any
    environment {
        PATH = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
        DOCKERHUB_CREDENTIALS = 'dockerhub-id'
        DOCKER_IMAGE = 'abhikkumar04/sci-calc:latest'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Abhik-04/SPE_Mini_Proj'
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
        stage('Ansible Deploy') {
            steps {
                sh 'ansible-playbook deploy.yml'
            }
        }

    }
    post {
        success {
            echo 'Pipeline succeeded!'
            mail to: 'abhik.kumar04@gmail.com',
            subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: "The build was successful!\nProject: ${env.JOB_NAME}\nBuild Number: ${env.BUILD_NUMBER}\nBuild URL: ${env.BUILD_URL}"
        }
        failure {
            echo 'Pipeline failed!'
            mail to: 'abhik.kumar04@gmail.com',
            subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: "The build failed!\nProject: ${env.JOB_NAME}\nBuild Number: ${env.BUILD_NUMBER}\nBuild URL: ${env.BUILD_URL}"
        }
    }
}
