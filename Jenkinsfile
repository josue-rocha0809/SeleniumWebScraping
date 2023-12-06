pipeline {
  agent any
  stages {
    stage('scraping') {
      steps {
             sh 'python3 -m venv venv'
             sh '. venv/bin/activate'
             sh 'pip install selenium'
             sh 'python3 main.py'
      }
    }
  }
}
