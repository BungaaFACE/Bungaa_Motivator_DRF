FROM python:3

WORKDIR /django

COPY ./r.txt ./r.txt

RUN pip install -r ./r.txt

COPY . .