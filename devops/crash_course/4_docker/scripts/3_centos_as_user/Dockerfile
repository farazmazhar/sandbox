# Based on CentOS: Unprivileged entry. 
FROM centos:latest

# Telling who the maintainer is.
LABEL maintainer="farazmazhar"

# Running a command to add a user.
RUN useradd -ms /bin/bash user

# Telling which user to use for the entry.
USER user
