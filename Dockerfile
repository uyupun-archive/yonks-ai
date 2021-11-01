FROM python:3.8

COPY requirements.txt /

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
