pipeline {
    agent any

    environment {
        // Define the SSH private key path in Jenkins, and the host to connect to
        SSH_KEY_PATH = '/var/jenkins_home/.ssh/id_rsa'
        WIN_HOST = 'host.docker.internal'
        WIN_PORT = '22'
        WIN_USER = 'user'  // The user you're logging into the Windows machine with
        SSH_PASSWORD = 'password'
    }

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
                        // SSH into Windows machine to run remote commands
                        sh '''sshpass -p "$SSH_PASSWORD"
                        ssh -o StrictHostKeyChecking=no -i ${SSH_KEY_PATH} ${WIN_USER}@${WIN_HOST} -p ${WIN_PORT} 'echo "Connected to Windows from Docker"' && docker-compose up --build
                        '''
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
