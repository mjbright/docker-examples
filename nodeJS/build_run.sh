
docker build -t node-hello .

docker run -p 80:80 --name web -d node-hello


