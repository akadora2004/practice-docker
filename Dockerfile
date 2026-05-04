FROM python:3.11-slim

WORKDIR /practice-docker

RUN pip install flask

COPY . /practice-docker

CMD [ "python", "-u", "main.py" ]

