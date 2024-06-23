FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip

WORKDIR /assistant

COPY assistant /assistant

RUN pip install -r /requirements.txt

RUN pip install .

CMD ["python3", "__main__.py"]