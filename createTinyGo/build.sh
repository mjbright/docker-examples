#!/bin/bash

docker run -ti golang GOPATH=src go build hello

docker run -ti golang GOPATH=src go build webserver


