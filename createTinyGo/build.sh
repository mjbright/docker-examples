#!/bin/bash

press() {
    echo $*
    echo "Press <return> to continue"
    read _DUMMY
    [ "$_DUMMY" = "q" ] && exit 0
    [ "$_DUMMY" = "Q" ] && exit 0
}

docker images | grep ^lab/
IDS=$(docker images | grep ^lab/ | awk '{print $1;}')
if [ ! -z "$IDS" ];then
    press "Cleaning up old images"
    docker rmi $IDS
fi

echo
press "About to build exectuables using Go-compiler in 'golang' container"
CMD="docker run -it -v $PWD:/go golang go build -v hello"
echo $CMD; $CMD
echo "----"
ls -alh hello

CMD="docker run -it -v $PWD:/go golang go build -v webserver"
echo $CMD; $CMD
echo "----"
ls -alh webserver

echo
press "About to build our own images including these new binaries"
echo
echo "-- Building image including hello binary"
CMD="docker build -t lab/go-hello -f Dockerfile.hello ."
echo $CMD; $CMD

echo
echo "-- Building image including webserver binary"
CMD="docker build -t lab/go-web -f Dockerfile.webserver ."
echo $CMD; $CMD

echo
docker images | grep ^lab/



