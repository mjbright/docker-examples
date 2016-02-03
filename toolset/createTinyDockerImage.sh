#!/bin/bash  

TAG=lab/toolset

echo; echo "-- Build helloWorld.exe"
gcc -static helloWorld.c -o helloWorld.exe
ls -al helloWorld.exe

ldd "helloWorld.exe"

echo; echo "-- Build the docker image based upon 'hello-world' as <$TAG>"
docker build -t $TAG ./

echo; echo "-- docker images $TAG"
docker images $TAG

echo; echo "-- docker run $TAG"
docker run $TAG

