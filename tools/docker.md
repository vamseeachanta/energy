## Introduction

Docker


## Summary

Docker image can be built using:
- Dockerfile directly and commands to build image and spin up container
- A holistic docker-compose.yml. docker-compose typically integrates steps, commands and application start-up to be used for/on DockerFile

Way Forward:
bring all the commmands from word document into md file

## Dockerfile

For Python examples, see py/docker.md
Other wide variety of images for various applications can be found in:



## Working with Docker

#Log in to your local docker registry
docker login -u <username> -p <password>
 
#Log out of your local docker registry
docker logout


## Working with Docker Image

Running the docker image:
<pre>
docker run -i -t  <image-name>
docker run -i -t  service-temp
</pre>

Running the docker image:
<pre>
docker run -i -t  <image-name> /bin/bash
docker run -i -t  service-temp /bin/bash
</pre>

## Working with Docker Container

To connect to a container in bash mode:
<pre>
docker exec -it <container-name> bash
docker exec -it application-container-1 bash
</pre>

Linux POST request:
<pre>
wget -O- --post-data='{"ID": 30015407220000, "TimeStamp": "2021-03-30 03:47:27.000", "json": true}' --header='Content-Type:application/json' 'http://localhost:5005/api/analysis_using_json'
</pre>

## Useful Commands

### cmd vs. entrypoint


## Docker Compose

Building a docker image:
<pre>
docker compose build
</pre>

Running a docker container:
<pre>
docker compose up
</pre>


## Errors

### General

Error: “You are trying to start Docker but you don’t have enough memory. Free some memory or change your settings.” 

Solution: System with 4GB total ram may not be sufficient to run windows on Docker. Set the memory settings to the lowest memory of 1 GB and check if it runs.

### Clean up space

https://stackoverflow.com/questions/64068185/docker-image-taking-up-space-after-deletion

### SQL Driver Error

https://superuser.com/questions/1355732/installing-microsoft-odbc-driver-to-debian
https://stackoverflow.com/questions/51888064/install-odbc-driver-in-alpine-linux-docker-container
https://stackoverflow.com/questions/42224701/odbc-driver-13-for-sql-server-cant-open-lib-on-pyodbc-while-connecting-on-ubunt

### References


