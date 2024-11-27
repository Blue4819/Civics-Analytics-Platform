pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/Blue4819/Civics-Analytics-Platform'
            }
        }
        
        stage('Build') {
            steps {
                script {
                    try {
                        // Build and run the application using Docker Compose
                        bat 'docker-compose up --build -d' 
                    } catch (Exception e) {
                        // Mark build as failed and re-throw the exception
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
        }
        }
        stage('Test') {
            steps {
                echo 'Testing.'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Eg: Deploying the project.'
            }
        }
    }

    post {
        success {
            echo 'Build and deployment successful!'
            // Optionally, you can send a success email if needed
            mail to: 'prachi.bharti21@st.niituniversity.in, purva.21@st.niituniversity.in, tanya.singh21@st.niituniversity.in, mehak.kapoor21@st.niituniversity.in',
                 subject: "Build Successful: ${currentBuild.fullDisplayName}",
                 body: "Build completed successfully: ${env.BUILD_URL}"
        }
        failure {
            echo 'Build failed!'
            // This will use the default recipients you set in Jenkins
            mail to: 'prachi.bharti21@st.niituniversity.in, purva.21@st.niituniversity.in, tanya.singh21@st.niituniversity.in, mehak.kapoor21@st.niituniversity.in',
                 subject: "Build Failed: ${currentBuild.fullDisplayName}",
                 body: "Something is wrong with ${env.BUILD_URL}. Please check the console output."
        }
    }
}
