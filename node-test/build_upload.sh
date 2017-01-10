
docker login

docker build -t mjbright/node-test:v1 .

docker push mjbright/node-test:v1

docker build -f Dockerfile.2 -t mjbright/node-test:v2 .
docker push mjbright/node-test:v2

#docker run -p 80:80 --name web -d node-hello


