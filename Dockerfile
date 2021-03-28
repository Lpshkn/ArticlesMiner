FROM python:3.9.2-slim-buster

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

COPY . /articlesminer
WORKDIR /articlesminer

ENTRYPOINT ["python3", "main.py"]