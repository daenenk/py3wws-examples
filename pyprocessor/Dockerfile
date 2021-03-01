FROM DOCKER_REPO/wws/py3wws

LABEL maintainer "author-email"

ARG DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /wws/op
WORKDIR /wws/op

COPY src/ src/   
COPY py3wws.json py3wws.json 

CMD ["python", "src/upper.py", "-vv", "-c", "py3wws.json"]