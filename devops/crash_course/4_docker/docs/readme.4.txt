-- DOCKER DEEP DIVE (README CONT.) --
    - Container ID: 0481f8c2934d
    - Image ID: 29701584ac00
    - Building a web farm (centos:centos6) // Part 1:
        a. Pulling CentOS6 container:
            CMD> sudo docker pull centos:centos6
        b. Run the container:
            CMD> sudo docker run -it centos:centos6 /bin/bash
        c. Install packages:
            DCM> yum install -y wget

            # Installing epel.
            DCM> wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
            DCM> rpm -Uvh epel-release-6-8.noarch.rpm

            # Install some more packages:
            DCM> yum install which sudo httpd php openssh-server

            # Add paths:
            DCM> nano .bashrc
'''
/sbin/service httpd start
/sbin/service sshd start
'''
        d. Commit the container into an image:
            CMD> sudo docker commit 0481f8c2934d centos6:baseweb
        e. Run the newly created image:
            CMD> sudo docker run -it centos6:baseweb /bin/bash
        f. Fix openssh-server:
            DCM> service sshd start
    
    - Building a web farm (centos:centos6) // Part 2:
        a. Building the website.
            # oswd.org/designs/browse/

    - Building a web farm (centos:centos6) // Part 3:
        a. Start the container:
            CMD> sudo docker run --name=webtest -i -t centos6:baseweb /bin/bash
        b. Start container with mounting www/ folder:
            CMD> sudo docker run -name=webtest -v /home/faraz/dockerm4/www/:/var/www/html -it centos6:baseweb /bin/bash
        c. Push the www/ to git.
    
    - Building a web farm (centos:centos6) // Part 4:
        a. Run two instances:
            CMD> sudo docker run -itd --name=devweb1 -p 8081:80 -v /home/faraz/dockerm4/www/:/var/www/html centos6:baseweb /bin/bash
            CMD> sudo docker run -itd --name=devweb2 -p 8082:80 -v /home/faraz/dockerm4/www2/:/var/www/html centos6:baseweb /bin/bash
        b. Install nginx.
        c. Modfiy /var/lib/nginx/sites-available/default
'''
upstream containerapp {
    server 127.0.0.1:8081;
    server 127.0.0.1:8082;
}

server{
    listen *:8083;

    server_name 127.0.0.1;
    index index.html index.htm index.php'

    access_log /var/log/nginx/localweb.log;
    error_log /var/log/nginx/localerr.log;

    location / {
        proxy_pass http://containerapp;
    }
}
'''
    
    - Integrating Custom Network in your Docker Container:
        _. Working as root.
        _. Stop the service before doing this:
            CMD> service docker stop
        a. Create a bridge:
            CMD> ip link add br10 type bridge
        b. Add ip address range:
            CMD> ip addr add 10.10.100.1/24 dev br10
        c. Up the bridge adapter:
            CMD> ip link set br10 up
        e. Assign the bridge to a docker container:
            CMD> docker -d -b br10 &

    - Testing Version Compatibility - Using Tomcat and Java // Part 1:
        a. Creating container for jdk7:
            CMD> docker run -it --name=jdk7 -v /home/faraz/dockerm4/ex2prereq/:/root/downloads centos:centos6 /bin/bash
        b. Update repos and install packages:
            DCM> yum update -y
            DCM> yum install -y git wget sudo which tar
        c. Extract JDK7:
            DCM> cd /root/downloads
            DCM> mkdir tmp
            DCM> cd tmp
            DCM> tar xvfz ../jdk-7u45-linux-x64.tar.gz
            DCM> mv jdk1.7.0_45/ /opt/java
        d. Set 'alternatives':
            DCM> alternatives --install /usr/bin/java java /opt/java/bin/java 2
            DCM> alternatives --config java
            DCM> alternatives --install /usr/bin/jar jar /opt/java/bin/jar 2
            DCM> alternatives --install /usr/bin/javac javac /opt/java/bin/javac 2
            DCM> alternatives --set jar /opt/java/bin/jar
            DCM> alternatives --set javac /opt/java/bin/javac
        e. Commit the container:
            CMD> docker commit jdk7 centos6:java7
        f. Repeat for container jdk8
            CMD> docker run -it --name=jdk8 -v /home/faraz/dockerm4/ex2prereq/:/root/downloads centos:centos6 /bin/bash
            DCM> yum update -y
            DCM> yum install -y git wget sudo which tar
            DCM> cd /root/downloads
            DCM> mkdir tmp
            DCM> cd tmp
            DCM> tar xvfz ../jdk-8u92-linux-x64.tar.gz
            DCM> mv jdk1.8.0_92/ /opt/java
            DCM> alternatives --install /usr/bin/java java /opt/java/bin/java 2
            DCM> alternatives --config java
            DCM> alternatives --install /usr/bin/jar jar /opt/java/bin/jar 2
            DCM> alternatives --install /usr/bin/javac javac /opt/java/bin/javac 2
            DCM> alternatives --set jar /opt/java/bin/jar
            DCM> alternatives --set javac /opt/java/bin/javac
            CMD> docker commit jdk8 centos6:jdk8
    
    - Testing Version Compatibility - Using Tomcat and Java // Part 2:
        a. Start a container:
            CMD> docker run -it --name=java7tomcat7 -v /home/faraz/dockerm4/ex2prereq/:/root/downloads -p 8085:8080 centos6:java7 /bin/bash
            CMD> docker run -it --name=java7tomcat8 -v /home/faraz/dockerm4/ex2prereq/:/root/downloads -p 8086:8080 centos6:java7 /bin/bash
            CMD> docker run -it --name=java8tomcat7 -v /home/faraz/dockerm4/ex2prereq/:/root/downloads -p 8087:8080 centos6:jdk8 /bin/bash
            CMD> docker run -it --name=java8tomcat8 -v /home/faraz/dockerm4/ex2prereq/:/root/downloads -p 8088:8080 centos6:jdk8 /bin/bash
        b. Extract Tomcat:
            DCM> cd /root/downloads/tmp
            DCM> tar xvfz ../apache-tomcat-7.0.92.tar.gz
                DCM2> ../apache-tomcat-8.5.37.tar.gz
            DCM> mv apache-tomcat-7.0.92/ /opt/tomcat
                DCM2> apache-tomcat-8.5.37 /opt/tomcat
        c. Set Java path:
            DCM> export JAVA_HOME=/opt/java
            DCM> export JAVA_JRE=/opt/java
            DCM> export CATALINA_BASE=/opt/tomcat
            DCM> export CATALINA_HOME=/opt/tomcat 
            DCM> export CATALINA_TMPDIR=/opt/tomcat/temp
            DCM> env | more
            DCM> cd /opt/tomcat/bin
            DCM> ./startup.sh &
            DCM> yum install curl -y
            DCM> docker commit java7tomcat centos6:jdk7tomcat7
            DCM> docker commit java8tomcat8 centos6:jdk8tomcat8
    
    - Testing Version Compatibility - Using Tomcat and Java // Part 3:
        a. Start the containers:
            CMD> docker run -it --name=java7tomcat7 -v /home/faraz/dockerm4/ex2prereq/:/root/downloads -p 8085:8080 -e JAVA_HOME=/opt/java -e JRE_HOME=/opt/java centos6:jdk7tomcat7 /bin/bash
            CMD> docker run -it --name=java8tomcat8 -v /home/faraz/dockerm4/ex2prereq/:/root/downloads -p 8088:8080 -e JAVA_HOME=/opt/java -e JRE_HOME=/opt/java centos6:jdk8tomcat8 /bin/bash
            DCM> /opt/tomcat/bin/startup.sh
            DCM> cd /root/downloads
            DCM> /opt/tomcat/bin/shutdown.sh
            DCM> cp sample.war /opt/tomcat/webapps
            DCM> /opt/tomcat/bin/startup.sh
                    

