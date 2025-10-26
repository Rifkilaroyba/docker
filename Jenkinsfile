pipeline {
    agent any

    environment {
        // ... (Environment variables)
        IMAGE_NAME = 'project-mobile-backend'
        CONTAINER_PORT = '5000'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Jenkins otomatis menarik kode SCM yang dikonfigurasi di Job
                echo "Starting Checkout..."
            }
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

        stage('Stop Old Container') {
            steps {
                script {
                    echo "Mengecek dan menghentikan container lama..."
                    // Hentikan container lama jika masih berjalan
                    sh "docker stop ${IMAGE_NAME} || true"
                    // Hapus container lama
                    sh "docker rm ${IMAGE_NAME} || true"
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    echo "Menjalankan container baru..."
                    // Jalankan container baru menggunakan image yang baru dibuat
                    sh """
                    docker run -d \
                    -p ${CONTAINER_PORT}:${CONTAINER_PORT} \
                    --name ${IMAGE_NAME} \
                    ${IMAGE_NAME}:${BUILD_NUMBER}
                    """
                    echo "Deployment selesai. Container berjalan di port ${CONTAINER_PORT}."
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline selesai. Periksa status untuk detail.' 
        }
        success {
            echo 'Pipeline berhasil! Deployment Docker baru telah selesai.'
        }
        failure {
            echo 'Pipeline GAGAL. Periksa Console Output untuk error Docker.'
        }
    }
}
