pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
            }
        }
    }

    post {
        success {
            echo 'Build and deployment successful!'
            // Optionally, you can send a success email if needed
            mail to: '',
                 subject: "Build Successful: ${currentBuild.fullDisplayName}",
                 body: "Build completed successfully: ${env.BUILD_URL}"
        }
        failure {
            echo 'Build failed!'
            // This will use the default recipients you set in Jenkins
            mail to: '',
                 subject: "Build Failed: ${currentBuild.fullDisplayName}",
                 body: "Something is wrong with ${env.BUILD_URL}. Please check the console output."
        }
        unstable {
            echo 'Build is unstable!'
            // Optionally, you can handle unstable builds here
            mail to: '',
                 subject: "Build Unstable: ${currentBuild.fullDisplayName}",
                 body: "The build is unstable: ${env.BUILD_URL}. Please check the console output."
        }
        always {
            // This block will run regardless of the build status
            echo 'Cleaning up...'
        }
    }
}