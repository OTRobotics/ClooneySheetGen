pipeline {
    agent any
    parameters {
        string(name: 'EVENT_ID', defaultValue: '', description: 'FRC Events Event ID')
        string(name: 'EVENT_NAME', defaultValue: '', description: 'Event Name (OffSeason Support)')
    }
    stages {
        stage('Build Official Event') {
            environment {
                FRC_API_TOKEN = credentials('frc-api-token')
            }
            when {
                expression { params.EVENT_ID != ''}
            }
            steps {
                sh 'pip3 install -r requirements.txt'
                sh "python3 run.py FRCEVENTS ${params.EVENT_ID} ${env.FRC_API_TOKEN}"
            }
        }
        stage('Build Off Season') {
            when {
                expression { params.EVENT_ID == '' }
            }
            steps {
                sh 'pip3 install -r requirements.txt'
                sh "python3 run.py ${params.EVENT_NAME}"
            }
        }
        stage('Archive') {
            steps {
                echo 'Archiving the build PDF....'
                archiveArtifacts artifacts: '**.pdf', fingerprint: true
            }
        }
    }
}
