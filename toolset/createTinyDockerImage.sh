#!/bin/bash  

TAG=lab/toolset

cp ../createTinyC/helloWorld.exe helloWorld.exe
cp ../createTinyGo/hello         helloWorldGo.exe

ls -altr *.exe

echo; echo "-- Build the docker image based upon 'hello-world' as <$TAG>"
docker build -t $TAG ./

echo; echo "-- docker images $TAG"
docker images $TAG

echo; echo "-- docker run $TAG"
docker run $TAG

