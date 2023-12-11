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
        success {
            mail to: 'josue.r@gercanada.com',
                 subject: "Éxito: Build #${env.BUILD_NUMBER}",
                 body: "El pipeline se ha ejecutado correctamente. URL del build: ${env.BUILD_URL}"
        }
        failure {
            mail to:'josue.r@gercanada.com',
                 subject: "Fallo: Build #${env.BUILD_NUMBER}",
                 body: "El pipeline ha fallado. Revisa los detalles en: ${env.BUILD_URL}"
        }
        unstable {
            mail to: 'josue.r@gercanada.com',
                 subject: "Inestable: Build #${env.BUILD_NUMBER}",
                 body: "El pipeline está inestable. Revisa los detalles en: ${env.BUILD_URL}"
        }
    }
}
