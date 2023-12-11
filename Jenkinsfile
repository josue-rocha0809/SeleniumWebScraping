pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // Crear un entorno virtual
                    sh 'python3 -m venv venv'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Instalar paquetes usando el pip del entorno virtual
                    sh './venv/bin/pip install selenium==4.1.0'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Ejecutar el script usando el Python del entorno virtual
                    sh './venv/bin/python main.py'
                }
            }
        }
    }

 post {
        always {
            script {
                def output = '' // Variable para almacenar la salida
                try {
                    output = sh([script: './venv/bin/python main.py', returnStdout: true]).trim()
                } catch (Exception e) {
                    output = e.getMessage()
                }

                // Enviar un correo electrónico con la salida
                mail to: 'josue.r@gercanada.com',
                     subject: "Build #${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
                     body: "Salida del build:\n${output}"
            }
        }
    }
}