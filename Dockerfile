FROM python:3.6-alpine

COPY . ./app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python app.py