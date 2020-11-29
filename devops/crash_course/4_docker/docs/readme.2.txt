-- DOCKER DEEP DIVE (README CONT.) --
    - Docker Directives:
        x. Order of commands do matter.
        a. FROM
            # On what it's based on, e.g. FROM centos:latest
        b. MAINTAINER (DEPRICATED)
            # Email address of the person that maintains the image, shows up when published.
        _. LABEL maintainer="email"
        c. RUN
            # Runs commands building stage.
            # Provides ability to run commands.
            # Execute commands at build time.
            # Its results become part of the built container.
        d. USER
            # Users to be included, must be created before using RUN.
            
            # This means that following will always log you in as the non-root user created
             by the Dockerfile.
            CMD> sudo docker run -it <image name> /bin/bash
            
            # To login as the root, use the following ('-u' is for user, UID '0' means root): 
            CMD> sudo docker exec -u 0 -it <image name> /bin/bash
        e. ENV
            # Used to set up environment.
            # Sets system-wide environment variable.
        f. CMD
            # Runs a command when the container is instantiated.
            # Part of the environment.
            # Not part of image itself.
        g. ENTRYPOINT
            # Basically runs commands whenever a container is instantiated from it.
            # This command will always run, doesn't matter what command has been passed.
        h. EXPOSE
            # Exposes ports.
    
    - Container volume management:
        a. Create a mount outside the container.
            # '-v [dirname]' to create the directory.
            # Can be found at: /var/lib/docker/volumes/[container-id]/_data/
        b. Mount a directory created on host to a container.
            # '-v [path-on-host]:[mount-name]'
    
    - Network:
        a. '172.17.0.0/16' is the default subnet.
        b. Docker network commands - list and inspect:
            CMD> sudo docker network ls
            CMD> sudo docker network inspect [network name]
            CMD> sudo docker network inspect none # Empty.
        c. Docker network commands - create and remove:
            CMD> sudo docker network create
                OPTIONS> --subnet 10.1.0.0/16 --gateway 10.1.0.1 --ip-range=10.1.4.0/24 --driver=bridge --label=[name]
                 [network name/id]
            CMD> sudo docker network rm
                OPTIONS> [network name/id]
        d. Assigning to container:
            CMD> sudo docker run -it --net [network name] --ip 10.1.4.100 image:tag /bin/bash
                OPT-EXPLAINED> --net [network name] (assigns network)
                OPT-EXPLAINE>> --ip [ip-addr] (assigns static ip)
    
    - CONTINUE FROM READMEV3.0
        