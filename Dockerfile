FROM python:3.11-slim
LABEL authors="slavat-huma"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN chmod +x /app/entrypoint.sh
CMD ["/bin/bash", "-c", "./entrypoint.sh"]
