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
                // Capturar los logs de la consola
                def consoleLog = currentBuild.rawBuild.getLog(1000).join("\n")

                // Determinar el estado del build y personalizar el asunto y el cuerpo del correo
                def mailSubject, mailBody
                if (currentBuild.result == 'SUCCESS') {
                    mailSubject = "Éxito: Build #${env.BUILD_NUMBER}"
                    mailBody = "El pipeline se ha ejecutado correctamente. URL del build: ${env.BUILD_URL}\n\nLogs:\n${consoleLog}"
                } else if (currentBuild.result == 'FAILURE') {
                    mailSubject = "Fallo: Build #${env.BUILD_NUMBER}"
                    mailBody = "El pipeline ha fallado. Revisa los detalles en: ${env.BUILD_URL}\n\nLogs:\n${consoleLog}"
                } else {
                    mailSubject = "Inestable: Build #${env.BUILD_NUMBER}"
                    mailBody = "El pipeline está inestable. Revisa los detalles en: ${env.BUILD_URL}\n\nLogs:\n${consoleLog}"
                }

                // Enviar un correo electrónico con los logs
                mail to: 'josue.r@gercanada.com',
                     subject: mailSubject,
                     body: mailBody
            }
        }
    }
}
