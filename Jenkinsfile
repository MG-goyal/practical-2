pipeline {
    agent any

    stages {
        stage('Run ML Pipeline') {
            steps {
                bat "C:\Users\Mayank\AppData\Local\Python\bin\python.exe -m pip install -r requirements.txt"
                bat "C:\Users\Mayank\AppData\Local\Python\bin\python.exe ml_pipeline.py"
            }
        }
    }

    post {
        success { echo 'SUCCESS - Model validated' }
        failure { echo 'FAILED - Check logs' }
    }
}