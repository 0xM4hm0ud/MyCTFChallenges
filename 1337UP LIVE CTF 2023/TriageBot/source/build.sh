#!/bin/bash

docker rm -f bot
docker build -t bot .
docker run --name=bot --rm -it bot