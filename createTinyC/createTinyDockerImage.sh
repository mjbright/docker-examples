#!/bin/bash  

TAG=lab/c_prog

echo; echo "-- Build helloWorld"
gcc -static helloWorld.c -o helloWorld
ls -al helloWorld

ldd "helloWorld"

echo; echo "-- Build the docker image <$TAG>"
docker build -t $TAG ./

echo; echo "-- docker images $TAG"
docker images $TAG

echo; echo "-- docker run $TAG"
docker run $TAG

