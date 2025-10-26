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
                    echo "🧹 Checking if any container uses port ${CONTAINER_PORT}..."
                    bat """
                    echo Checking containers using port ${CONTAINER_PORT}...
                    docker ps --format "{{.ID}} {{.Ports}}" | find "0.0.0.0:${CONTAINER_PORT}->" > temp.txt || echo none > temp.txt
                    for /F "tokens=1" %%i in (temp.txt) do (
                        echo Stopping container ID %%i
                        docker stop %%i
                        docker rm %%i
                    )
                    del temp.txt
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
                    echo Waiting 5 seconds for port ${CONTAINER_PORT} to be released...
                    timeout /t 5 /nobreak >nul
                    """
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    echo "🚀 Running new container..."
                    // Cek dulu apakah port masih dipakai
                    bat """
                    netstat -ano | find ":${CONTAINER_PORT}" >nul
                    if %ERRORLEVEL%==0 (
                        echo ⚠️ Port ${CONTAINER_PORT} masih dipakai, menunggu 5 detik...
                        timeout /t 5 /nobreak >nul
                    )
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

