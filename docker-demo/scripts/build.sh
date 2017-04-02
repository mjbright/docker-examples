
echo; echo "Build v20:"
docker build -t mjbright/docker-demo:latest -t mjbright/docker-demo:20 .

echo; echo "Build v21:"
docker build -f Dockerfile.21 -t mjbright/docker-demo:latest -t mjbright/docker-demo:21 .

echo; echo "Docker login:"
docker login

echo; echo "push build:20"
docker push mjbright/docker-demo:20

echo; echo "push build:21"
docker push mjbright/docker-demo:21

