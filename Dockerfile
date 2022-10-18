FROM python:3.10

COPY . .

CMD echo "EXECUTED=true" >> $GITHUB_ENV

RUN python main.py
