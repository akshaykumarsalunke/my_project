pipeline {
    agent any
    stages {
        stage('Deploy to Astronomer') {
            when {
                expression {
                    return env.GIT_BRANCH == "origin/main"
                }
            }
            steps {
                checkout scm
                sh '''
                env | grep ASTRO
                curl -LJO https://github.com/astronomer/astro-cli/releases/download/v1.26.0/astro_1.26.0_linux_amd64.tar.gz
                tar -zxvf astro_1.26.0_linux_amd64.tar.gz astro && rm astro_1.26.0_linux_amd64.tar.gz
                ./astro deploy ${ASTRONOMER_DEPLOYMENT_ID} -f
                '''
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
