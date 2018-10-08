pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python3 run.py' 
                archiveArtifacts artifacts: '**.pdf', fingerprint: true 
            }
        }
        stage('Archive') {
            steps {
                echo 'Archiving the build PDF....'
                echo 'Not Really, I haven\'t figured how do do this yet'
            }
        }
    }
}
