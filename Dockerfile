FROM python:3.11-slim
LABEL authors="slavat-huma"

COPY . /app
WORKDIR /app

RUN pip install uv && \
    uv venv --python 3.11 && \
    uv sync

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
