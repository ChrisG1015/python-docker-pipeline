
docker build -t grainger-py .

docker run --rm grainger-py -s {STATE}

docker run --rm grainger-py -s California
