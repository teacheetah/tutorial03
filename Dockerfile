FROM python:3.8-slim

RUN mkdir -p /teacheetah

COPY . /teacheetah

WORKDIR /teacheetah

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:init_app", "--worker-class", "aiohttp.GunicornWebWorker", "--access-logfile", "-"]
