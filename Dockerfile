FROM python:3.8

RUN mkdir -p /opt/bot/
WORKDIR /opt/bot/

RUN pip install pipenv

COPY . /opt/bot/

RUN pipenv sync

CMD ["pipenv", "run", "python", "run.py"]