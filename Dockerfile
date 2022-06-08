FROM python:3.10-slim

WORKDIR /app

COPY Pipfile.lock Pipfile.lock
RUN pip install pipenv && pipenv requirements > requirements.txt && pip install -r requirements.txt

COPY . .

CMD python .
