-- DOCKER DEEP DIVE (README CONT.) --
    - Inspect Container Process:
        a. Listing processes:
            CMD> sudo docker exec [container name/id] /bin/ps aux
            CMD> sudo docker top [container name/id]
        b. Make container keep running:
            > If you start a container using the following, it'll open two /bin/bash and now
             'exit' command won't stop the container.
            CMD> sudo docker exec -i -t [container name/id] /bin/bash

            > Stats; constantly updating.
            CMD> sudo docker stats [container name/id]

    - Previous Container Management:
        a. Removing containers:
            CMD> sudo docker rm [container name/id] [container name/id] ...
                OPTIONS> -f, --force (force)
        b. Removing containers from host:
            # Stop docker service and delete the container directory present in following:
                > rm -rf /var/lib/docker/containers/[container dir]
            # Note: without stopping, it might cause issues.
    
    - Controlling Port Exposure on Containers:
        a. Expose ports:
            # '-p [host-port]:[container-port]' -> Publish a container's port(s) to the host.
            # '-P' -> Publish all exposed ports to random ports
    
    - Naming Containers:
        a. No spacing.
        b. No strange special characters.
        c. Assigning a name at run time (for both running and stopped):
            # '--name [container name]'
            CMD> sudo docker rename [old name/id] [new name]
        d. Docker Events:
            # Displays events happening in Docker.
            CMD> docker events
                OPTIONS> --since '1h' --filter [container/event/image/label/type/volume/network/daemon]=[value]

    - Managing and Removing Base Images:
        a. Removing an image:
            # Removing the base image, of which a container is running, will result in an error.
                * Either stop/delete the cointainers first or use the force.
            # If an image ID has multiple references, using that image ID will result in conflict.
                * Using force will remove all the images referring the given image ID.
            CMD> docker rmi [image-name]:[tag]
                OPTIONS> --force 
    
    - Saving and Loading Docker Images:
        a. Pulling an image:
            CMD> sudo docker pull [image0name]:[tag]
        b. Committing a container to an image:
            CMD> sudo docker commit [container] [image-name]:[tag]
        c. Saving an image:
            CMD> sudo docker save [image-name]:[tag] > [filename].tar
            CMD> sudo docker --output [filename].tar [image-name]:[tag]
            # Using 'gzip' on top of '.tar' will compress it even more.
        d. Loading a saved image:
            CMD> sudo docker load --input [filename].tar(.gz) [image-name]:[tag]
        
    - Image History:
        a. Use following:
            CMD> sudo docker history [image-name]:[tag]
                OPTIONS> --quite --no-trunc

    - Tags:
        a. Tagging an image with a different tag:
            CMD> sudo docker tag [image-name/id] [user|host/image-name]:[tag]
        b. Limitation: 128 characters, and can't start with '.' or '-'.
    
    - Pushing to Docker Hub.
        a. Create a repo on Docker Hub.
        b. Use Docker Login:
            CMD> sudo docker login 
            CMD> sudo docker logout
        c. Push to the Hub:
            CMD> sudo docker push [username]/[repo]

    - CONTINUE FROM READMEV4.0


            
