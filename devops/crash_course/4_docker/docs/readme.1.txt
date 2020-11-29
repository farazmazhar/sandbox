-- DOCKER DEEP DIVE --
    - Linux Academy presentations are present in 'docs\Linux Academy'.

    - Installing docker:
        a. Installation on Ubuntu 18.04:
'''
#! /bin/bash
# Set up repo.
sudo apt-get update -y
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

# Installation
sudo apt-get update -y
sudo apt-get install docker-ce -y
apt-cache madison docker-ce
sudo apt-get install docker-ce="5:18.09.1~3-0~ubuntu-bionic"
sudo docker run hello-world
'''
        b. Uninstall Docker:
'''
sudo apt-get remove docker docker-engine docker.io containerd runc
'''

    - Docker login:
        CMD> sudo docker login
        a. Check out following to figure out how to manage credentials better.
            # https://docs.docker.com/engine/reference/commandline/login/#credentials-store

    - Introduction:
        a. Container service.
            # Develop, Deploy, Run.
        b. Uses light weight VM to do its bidding.
        c. Reasons to use:
            # Flexible: Even the most complex applications can be containerized.
            # Lightweight: Containers leverage and share the host kernel.
            # Interchangeable: You can deploy updates and upgrades on-the-fly.
            # Portable: You can build locally, deploy to the cloud, and run anywhere.
            # Scalable: You can increase and automatically distribute container replicas.
            # Stackable: You can stack services vertically and on-the-fly.
            # Makes CI/CD seamless:
                > Applications have no system dependencies.
                > Updates can be pushed to any part of a distributed application
                > Resource density can be optimized.
        d. Docker offers allows you to isolate and standardize build and deployment process.
        e. Images:
            # Executable package that includes everything needed to run an application--the
             code, a runtime, libraries, environment variables, and configuration files
        f. Containers:
            # Runtime instance of an image.
            # Entirely isolated set of packages, libraries, and/or applications which are
             completely independent from its surroundings.
            # Containers allow better utilization of the host machine's resources give that
            the resources are not segregated like they are in the case of VMs.
            # Basically, they are more efficient as the resource management is granular.
            # List docker containers:
                > docker ps
        g. Containers vs VM:
            # A container runs natively on Linux and shares the kernel of the host machine 
             with other containers. It runs a discrete process, taking no more memory than
             any other executable, making it lightweight.
            # A virtual machine (VM) runs a full-blown “guest” operating system with
             virtual access to host resources through a hypervisor. Requiring more resources
             then most applications need.
    
    - Containers:
        a. Hierarchy of an app:
            # Stack.
            # Services.
            # Container. (We are here)
        b. Dockerfile:
            # Portable images.
            # Defines what goes on in the environment inside your container.
            # Dockerfile example: Python example. 
                > Creating a docker file:
                 => Check '../scripts' folder.
                
                > Copy files into a folder.
                CMD> sudo docker build --tag=friendlyhello .
                CMD> sudo docker image ls
                
                > OPTIONAL: Version of can be given like this '--tag=friendlyhello:v0.0.1'.
                CMD> sudo docker run -p 4000:80 friendlyhello
                
                > 4000:80 is mapping 4000 port of host to 80 port of the container.
                CMD> sudo docker run -d -p 4000:80 friendlyhello
                > '-d' means run deattached and '-p' means publish the container's post to host. 
            # Sharing an image:
                > A registry has repositories, a repository has images.
                > Docker CLI uses public registry by default.
                
                > Login into Docker:
                CMD> sudo docker login
                
                > Notation for associating a local image with a repo on registry:
                    * username/repository:tag
                CMD> sudo docker tag image username/repository:tag
                
                > Pushing the image to repo:
                CMD> sudo docker push username/repository:tag
                
                > Pulling and running an image from remote repository:
                CMD> docker run -p 4000:80 username/repository:tag

                > Get mroe info:
                CMD> sudo docker inspect <base image name>
            # Pulling an image:
                CMD> sudo docker pull ubuntu:xenial
                CMD> sudo docker run -i -t ubuntu:xenial
                > '-i' means interactive; '-t' means attach to terminal.
            # Restarting/attaching an image:
                CMD> sudo docker restart <image name/id>
                CMD> sudo docker attach <image name/id>
            # Multiple images:
                CMD> sudo docker run -itd ubuntu:xenial /bin/bash
            # Stop a container:
                CMD> sudo docker stop <image name/id>
            # Search DockerHub:
                CMD> sudo docker search username/repo
            # Packaging a customized container:
                CMD> sudo docker commit -m "message" -a "username?" <image name/id> username/repo:tag 
            # Remove containers:
                CMD> sudo docker container rm <image name/id>
            # Run command outside the container:
                CMD> sudo docker exec <image id/name> /bin/cat /etc/profile
            # Check out output of container:
                CMD> sudo docker logs <image id/name>
            # 
            # DOCKERFILE build:
                CMD> sudo docker build -t="user/repo:tag" .
            # Example DOCKERFILE:
'''
FROM ubuntu:xenial
MAINTAINER user <user@domain.com>
RUN apt-get update -y
RUN apt-get install telnet openssh-server -y
'''

    - Container Architecture:
        a. A client-server application where both daemon and client can be run on the same system or a remote one.
        b. Can communicate via sockets or RESTful APIs.
        c. Components of docker are:
            # Daemon.
            # Client.
            # Docker.io registry.
        d. Leaves behind bloat associated with a full hardware hypervisor.
        e. Only has libraries, and modules that are absolutely requried to run the application.


    - Docker Compose (Services prerequisite):
        a. A tool for defining and running multi-container Docker applications.
        b. YAML script to configure applications services.
        c. Single command to create and start all services from the configuration.
        d. The three-step process:
            # Define your app’s environment with a 'Dockerfile' so it can be reproduced anywhere.
            # Define the services that make up your app in 'docker-compose.yml' so they can be run 
             together in an isolated environment.
            # Run 'docker-compose up' and Compose starts and runs your entire app.
        e. Install Docker Compose:
            # Latest release number from:
                > https://github.com/docker/compose/releases
'''
sudo curl -L https://github.com/docker/compose/releases/download/1.24.0-rc1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo docker-compose --version
'''
        f. Compose has commands for managing the whole lifecycle of your application:
            # Start, stop, and rebuild services.
            # View the status of running services.
            # Stream the log output of running services.
            # Run a one-off command on a service.
        g. Features of Docker compose:
            # Multiple isolated environments on a single host.
            # Preserve volume data when containers are created.
            # Only recreate containers that have changed.
            # Variables and moving a composition between environments.
        h. Common use cases:
            # Development environments.
            # Automated testing environments.
            # Single host deployments.
        i. Webnet:
            # A load balancer.

    - Services:
        a. Hierarchy of an app:
            # Stack.
            # Services. (We are here)
            # Container.

        b. About:
            # In distributed application, different pieces of the app are called 'services'.
            # Services are really just 'containers in production'.
            # Service runs only one image.
            # Service codifies things like:
                > The way image runs.
                > What ports to use.
                > Number of replicas.
            # Scaling/updating services is as easy as updating 'docker-compose.yml' file.

        c. Deploying a docker-compose:
            # A single container running in a service is called a task.

            > Running Docker Swarm:
            CMD> sudo docker swarm init
            
            > Docker stack deploy:
            CMD> sudo docker stack deploy -c docker-compose.yml getstartedlab
            > Note: Updating the 'docker-compose.yml' file and then running above
             command will update the containers in-place without having to kill or
             destroy any containers.
            
            > Check running services:
            CMD> sudo docker service ls
            
            > Tasks can be listed by listing all containers:
            CMD> sudo docker container ls -q
    
        d. Tearing down app and swarm:
            CMD> sudo docker stack rm getstartedlab
            CMD> sudo docker swarm leave --force

    - Swarms:
        a. Group of machines, running Docker and joined into a cluster.
        b. Docker commands run on the Swarm manager (after calling 'docker swarm init').
        c. Machines in swarm can be physical or virtual, referred to as nodes.
        d. Strategies imployed by the manager:
            # Emptiest node (least utilized node is used).
            # Global (each machine gets at least one instance of a specified container).
        e. Swarm mangers are the only machines:
            # That can execute your commands.
            # Allow machines to join a swarm as workers.
        f. Workers are only there to provide capacity and can't authorize anything or 
         execute any command.
        g. Creating a swarm:
            > Start a swarm:
            CMD> sudo docker swarm init

            > Join a swarm:
            CMD> sudo docker swarm join

            # Install docker machine:
'''
base=https://github.com/docker/machine/releases/download/v0.16.0 &&
curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
sudo install /tmp/docker-machine /usr/local/bin/docker-machine

# Check docker machine version
sudo docker-machine version

# Requires VirtualBox to run 
sudo apt-get install virtualbox
sudo docker-machine create --driver virtualbox default
'''

            > Create VMs (example's sake?):
            CMD> sudo docker-machine create --driver virtualbox myvm1
            CMD> sudo docker-machine create --driver virtualbox myvm2

            > List the VMs:
            CMD> sudo docker-machine ls
        
    - Stacks:
        a. visit: https://docs.docker.com/get-started/part5/
    
    - Deploy your app:
        a. visit: https://docs.docker.com/get-started/part6/

    - CONTINUE FROM READMEV2.0

