FROM python:3.12-slim

# Install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV MONGODB_USERNAME="mongouser_name"
ENV MONGODB_PASSWORD="mongouser_password"

EXPOSE 8082

CMD ["python","main.py"]