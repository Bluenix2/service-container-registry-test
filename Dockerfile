FROM python:3.10

COPY . .

RUN echo "EXECUTED=true" >> $GITHUB_ENV
