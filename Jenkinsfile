pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'ls'
      }
    }
  }
  environment {
    ENVStaging = 'staging'
    ENVProd = 'production'
  }
}