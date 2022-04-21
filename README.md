# python-docker-pipeline

To run locally:

`pip3 install -r requirements.txt`


`python3 state_code.py -s South Carolina`


To run via Docker:

```
docker build -t grainger-py .

docker run --rm grainger-py -s {STATE}

docker run --rm grainger-py -s California
```

