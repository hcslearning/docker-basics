FROM alpine:3.12.0

WORKDIR /usr/src/app
COPY . .
RUN rm Dockerfile
RUN apk add --update py3-pip
RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 5000

CMD ["python3", "./hello.py"]
 


