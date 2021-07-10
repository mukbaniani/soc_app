FROM python:3.8.5
ENV PYTHONBUFFERED=1
WORKDIR /usr/src/app
COPY req.txt req.txt
RUN pip3 install -r req.txt
COPY . .