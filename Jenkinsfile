pipeline {
    agent any

    environment {
        // ... (Environment variables)
        IMAGE_NAME = 'project-mobile-backend'
        CONTAINER_PORT = '5000'
    }

    stages {
        stage('Checkout Code') {
           // ... (steps)
        }
        
        stage('Build Docker Image') {
            steps {
                // PENTING: Masuk ke direktori backend-api sebelum build
                dir('backend-api') { 
                    script {
                        echo "Membangun image Docker dari direktori: ${PWD}" 
                        // Perintah ini sekarang berjalan DARI DALAM folder backend-api
                        // Tanda titik (.) berarti konteks build adalah folder saat ini.
                        sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ." 
                    }
                }
            }
        }

        // ... (Stages Stop Old Container dan Run New Container)
        stage('Stop Old Container') {
            // ...
        }

        stage('Run New Container') {
            // ...
        }
    }

    // ... (Post section)
}
