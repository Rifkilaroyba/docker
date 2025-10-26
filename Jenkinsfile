pipeline {
    agent any

    environment {
        IMAGE_NAME = 'project-mobile-backend'
        CONTAINER_PORT = '5000'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "🔄 Starting code checkout..."
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "🐳 Building Docker image from root directory: ${pwd()}"
                    bat """
                    docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest .
                    """
                }
            }
        }

        stage('Free Used Port') {
            steps {
                script {
                    echo "🧹 Checking if any container is using port ${CONTAINER_PORT}..."
                    bat """
                    for /f "tokens=1" %%i in ('docker ps -q --filter "publish=${CONTAINER_PORT}"') do (
                        echo ⚠️ Stopping container using port ${CONTAINER_PORT} (ID=%%i)...
                        docker stop %%i
                        docker rm %%i
                    )
                    """
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    echo "🛑 Stopping old container if exists..."
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
