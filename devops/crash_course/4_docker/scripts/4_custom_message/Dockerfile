# Based on CentOS: Unprivileged entry with custom message. 
FROM centos:latest

# Telling who the maintainer is.
LABEL maintainer="farazmazhar"

# Running a command to add a user.
RUN useradd -ms /bin/bash user

# Echoing some random stuff.
RUN echo "EXPORT 192.168.0.0/24" >> /etc/exports.list

# Updating yum repos.
RUN yum update -y

# Installing net-tools and wget.
RUN yum install -y net-tools wget

# Moving to root home directory and install stuff.
RUN cd ~ && [wget certificate and stuff]
RUN yum localinstall -y ~/[install-folder]

# Telling which user to use for the entry.
USER user

# Adding env var to .bashrc.
# RUN cd ~ && echo "export env_var=[path]" >> /home/user/.bashrc
ENV VAR_BIN [path path]