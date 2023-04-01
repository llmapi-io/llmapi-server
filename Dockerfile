FROM python:3.8.10

WORKDIR /app

COPY backend /app/backend
COPY prepost /app/prepost
COPY server /app/server
COPY utils /app/utils
COPY run_api_server.py /app/
COPY requirements.txt /app/

ENV LANG C.UTF-8

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install -r /app/requirements.txt

CMD [ "python3", "run_api_server.py"]

RUN echo '----- success -----'

