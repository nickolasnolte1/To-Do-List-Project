
FROM python:3.9-slim


WORKDIR /app


COPY . /app

RUN pip install Flask flask_sqlalchemy


RUN apt-get update && apt-get install -y sqlite3


EXPOSE 8080

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Run the Flask application
CMD ["flask", "run"]