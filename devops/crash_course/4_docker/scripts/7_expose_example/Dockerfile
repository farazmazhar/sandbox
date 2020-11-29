# Boiler plate script
FROM centos:latest
LABEL maintainer="farazmazhar"
RUN yum update -y
RUN yum install -y httpd net-tools
RUN echo "This is a custom index file built during image creation" > /var/www/html/index.html

# Defines network ports for this container to listen on at runtime.
EXPOSE 80

ENTRYPOINT apachectl "-DFOREGROUND"

# run with '-d' option.
# use '-P' to map ports, including exposed ports.