#!/bin/bash

docker run -it -v $PWD:/go golang go build -v hello

docker run -it -v $PWD:/go golang go build -v webserver


