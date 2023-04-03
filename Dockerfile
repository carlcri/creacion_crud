FROM alpine:latest

RUN apk add --update python3

RUN apk add py3-pip

ADD requirements.txt /

RUN pip3 install -r requirements.txt

ADD main.py /

ADD .clients.csv /

CMD ["python","./main.py"]
