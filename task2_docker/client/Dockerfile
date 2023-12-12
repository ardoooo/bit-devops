FROM python:latest

WORKDIR /
COPY client.py /
COPY requirements.txt /

RUN pip install -r requirements.txt

CMD ["python", "client.py"]
