FROM python:3.12-slim-bookworm

LABEL org.opencontainers.image.source="https://github.com/Robooto/conversation-starter"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends libbrotli1 \
    && dpkg --compare-versions "$(dpkg-query -W -f='${Version}' libbrotli1)" ge '1.0.9-2+deb12u1' \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 80

WORKDIR /app
COPY ./app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
