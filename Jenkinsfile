pipeline {
    agent any

    environment {
        // Ganti dengan nama image yang Anda inginkan
        IMAGE_NAME = 'project-mobile-backend'
        CONTAINER_PORT = '5000'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Jenkins otomatis menarik kode dari SCM (GitHub)
                script {
                    echo "Kode berhasil ditarik dari GitHub."
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Membangun image Docker..."
                    // Pindah ke direktori backend-api sebelum build
                    dir('backend-api') {
                        // Perintah untuk membangun image, tag menggunakan nomor build
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
        // ... (notifikasi sukses/gagal)
    }
}
