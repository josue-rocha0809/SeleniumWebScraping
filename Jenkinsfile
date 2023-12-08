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
                    // Ejecutar el script y capturar la salida
                    def output = sh(script: './venv/bin/python main.py', returnStdout: true).trim()
                    // Escribir la salida en un archivo
                    writeFile file: 'output.txt', text: output
                }
            }
        }
    }
        post {
        always {
            // Envía un correo electrónico con el archivo adjunto
            emailext(
                subject: "Resultado del Script Python",
                body: "Aquí está el resultado del script de Python.",
                recipients: 'josue.r@gercanada.com',
                attachmentsPattern: 'canadaInfo.txt'
            )
        }
    }
}
