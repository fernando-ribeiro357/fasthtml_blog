FROM python:3.11-alpine


COPY ./src /usr/src/app
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "uvicorn", "app.main:app","--host", "0.0.0.0"]
