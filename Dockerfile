FROM python:3.9.5-slim-buster
WORKDIR /app/
COPY *.py /app/
COPY requirements.txt /app/
RUN pip install -U pip && pip install -r requirements.txt
ARG port=8080
EXPOSE ${port}
ENTRYPOINT python app.py