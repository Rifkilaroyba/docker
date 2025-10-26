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
                // Secara default Jenkins akan checkout otomatis, jadi cukup echo
            }
        }

        stage('Build Docker Image') {
            steps {
                dir("${WORKDIR}") {
                    script {
                        echo "🐳 Building Docker image from directory: ${pwd()}"
                        
                        // Hapus image lama jika ada (optional)
                        sh "docker rmi ${IMAGE_NAME}:latest || true"
                        
                        // Build image dengan dua tag: BUILD_NUMBER dan latest
                        sh """
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
                    // Stop dan remove container jika sedang berjalan
                    sh """
                    if [ \$(docker ps -q -f name=${IMAGE_NAME}) ]; then
                        docker stop ${IMAGE_NAME}
                    fi
                    if [ \$(docker ps -aq -f name=${IMAGE_NAME}) ]; then
                        docker rm ${IMAGE_NAME}
                    fi
                    """
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    echo "🚀 Running new container..."
                    sh """
                    docker run -d \
                        -p ${CONTAINER_PORT}:${CONTAINER_PORT} \
                        --name ${IMAGE_NAME} \
                        ${IMAGE_NAME}:${BUILD_NUMBER}
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
