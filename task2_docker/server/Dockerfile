FROM python:latest

WORKDIR /
COPY server.py /
COPY requirements.txt /

RUN pip install -r requirements.txt

CMD sleep 5 && python server.py
