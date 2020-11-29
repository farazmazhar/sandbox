# Based on CentOS: Unprivileged entry. 
FROM centos:latest

# Telling who the maintainer is.
LABEL maintainer="farazmazhar"

# Running a command to add a user.
RUN useradd -ms /bin/bash user

ENTRYPOINT echo "This command display this message on EVERY container that is run from it."

# Telling which user to use for the entry.
USER user
