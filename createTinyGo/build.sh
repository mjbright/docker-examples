#!/bin/bash

docker run -it -v $PWD:/go golang go build -v hello

docker run -it -v $PWD:/go golang go build -v webserver

docker build -t lab/go-hello -f Dockerfile.hello .

docker build -t lab/go-web -f Dockerfile .



