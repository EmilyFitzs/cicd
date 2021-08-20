pipeline {
    agent any
    stages {

        stage('build') {
            steps {
                echo 'this is the building stage!'
            }
        }

        stage('test') {
            steps {
                echo 'this is the testing stage'
            }
        }

        stage('upload to s3') {
           steps {
             sh '/usr/local/bin/aws s3 cp ./www.index.html s3://emily--s3/index.html'
             sh '/usr/local/bin/aws s3 cp ./www.error.html s3://emily--s3/error.html'
           }
        }
    }
}