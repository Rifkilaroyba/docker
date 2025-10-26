pipeline {
    agent any

    environment {
        IMAGE_NAME = 'project-mobile-backend'
        CONTAINER_PORT = '5000'
        WORKDIR = 'backend-api'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "🔄 Starting code checkout..."
            }
        }

        stage('Build Docker Image') {
            steps {
                dir("${WORKDIR}") {
                    script {
                        echo "🐳 Building Docker image from directory: ${pwd()}"
                        bat """
                        docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest .
                        """
                    }
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    echo "🛑 Checking and stopping old container if exists..."
                    bat """
                    docker stop ${IMAGE_NAME} || echo No container to stop
                    docker rm ${IMAGE_NAME} || echo No container to remove
                    """
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    echo "🚀 Running new container..."
                    bat """
                    docker run -d -p ${CONTAINER_PORT}:${CONTAINER_PORT} --name ${IMAGE_NAME} ${IMAGE_NAME}:${BUILD_NUMBER}
                    """
                    echo "✅ Container is running on port ${CONTAINER_PORT}"
                }
            }
        }
    }

    post {
        always {
            echo '📦 Pipeline finished. Check logs for details.'
        }
        success {
            echo '✅ SUCCESS: Docker deployment completed.'
        }
        failure {
            echo '❌ FAILURE: Check Jenkins console for Docker error details.'
        }
    }
}
