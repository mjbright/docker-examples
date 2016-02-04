#!/bin/bash  

TAG=lab/toolset

cp ../createTinyC/helloWorld helloWorld
cp ../createTinyGo/hello         helloWorldGo

ls -altr 

echo; echo "-- Build the docker image based upon 'hello-world' as <$TAG>"
docker build -t $TAG ./

echo; echo "-- docker images $TAG"
docker images $TAG

echo; echo "-- docker run $TAG"
docker run $TAG

