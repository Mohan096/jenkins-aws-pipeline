pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        AWS_DEFAULT_REGION = 'us-west-2'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/jenkins-aws-ec2-pipeline.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pip install boto3'
                    } else {
                        bat 'pip install boto3'
                    }
                }
            }
        }

        stage('Launch EC2 Instance') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python launch_ec2.py'
                    } else {
                        bat 'python launch_ec2.py'
                    }
                }
            }
        }
    }
}

