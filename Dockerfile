FROM python:3.10-slim

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000
