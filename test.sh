#!/bin/bash

docker container stop modeltest
docker container rm modeltest
docker image rm modeltest
docker build -t modeltest .
docker run --rm -i -t -p 8000:8000 --name=modeltest modeltest 
