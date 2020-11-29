-- Jenkins --
    - Installations (for Ubuntu 18.04):
        a. Jenkins:
            # Installing prerequisite:
                > Install maven.
                    * sudo apt install maven -y
                > Install git.
                    * sudo apt install git -y
            # Installing (bash):
'''
sudo apt update -y
sudo apt install -y openjdk-8-jdk
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update -y
sudo apt install -y jenkins
systemctl status jenkins
'''

            # Setting up:
                > http://localhost:8080
                => sudo cat /var/lib/jenkins/secrets/initialAdminPassword
                > Continue

    - Prerequisite:
        a. Install JDK8.
'''
sudo yum update
cd /
sudo su
cd usr
mkdir java
wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u141-b15/336fa29ff2bb4ef291e347e091f7f4a7/jdk-8u141-linux-x64.rpm"
yum install jdk-8u141-linux-x64.rpm

'''
        b. Installing Tomcat:
'''
wget https://www-us.apache.org/dist/tomcat/tomcat-8/v8.5.37/bin/apache-tomcat-8.5.37.tar.gz
tar xvfz apache-tomcat-8.5.37.tar.gz
rm -r apache-tomcat-8.5.37.tar.gz
cd apache-tomcat-8.5.37
cd bin
./startup.sh
ps -ef | grep tomcat
wget http://localhost:8080
'''
        c. Modifiying files:
            # nano webapps/manager/META-INF/context.xml
                > look for <valve classname> and comment it out using <!-- -->
            # Restart the server.
        
    - Transfer/deploy war files to Tomcat server on EC2.
        a. Create credentials for EC2 instance.
            # Jenkins 
                -> Credentials
                    -> Global credentials (unrestricted)
                        -> Add credentials
                            => Kind: SSH Username with private key
                            => Username: ec2-user
                            => Private key:
                                -=> Enter directly
                                --=> Key: Copy contents of the *.pem file.
        
        b. Create new pipeline.
            # Pipeline section:
                -> Definition: Pipeline script.
                    => Script: [copy following...]
'''PIPELINE SCRIPT
node{
   stage('SCM Checkout'){
     git 'https://github.com/javahometech/my-app'
   }
   stage('Compile-Package'){
      sh "mvn clean install"
   }
   stage('Deploy to Tomcat'){
      sshagent(['tomcat-dev']) {
        sh 'scp -o StrictHostKeyChecking=no target/*.war ec2-user@{ec2PublicIp}:/home/ec2-user/apache-tomcat-8.5.37/webapps/'
    }
   }
}
'''