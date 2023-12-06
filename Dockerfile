FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /randoflix
WORKDIR /randoflix
COPY . /randoflix/
RUN pip install -r requirements.txt