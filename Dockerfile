FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TF_ENABLE_ONEDNN_OPTS 3


WORKDIR /app
RUN apt update && apt install git -y
COPY requirements.txt pyproject.toml poetry.lock ./

RUN pip install --upgrade pip
RUN pip3 --no-cache-dir install -r requirements.txt
RUN poetry config virtualenvs.create false
RUN poetry install

ADD . /app/

EXPOSE 8000

CMD ["/usr/local/bin/gunicorn", "-w", "3", "project.wsgi:application", "-b", "0.0.0.0:8000"]