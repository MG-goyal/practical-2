pipeline {
    agent any
    
    stages {
        stage('Run ML Pipeline') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'py ml_pipeline.py'
            }
        }
    }

    post {
        success { echo 'SUCCESS - Model validated' }
        failure { echo 'FAILED - Check logs' }
    }
}