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
}
