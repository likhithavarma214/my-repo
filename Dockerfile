FROM python:3.8

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    openssl \
    libssl-dev

RUN pip install flask==0.12

COPY . /app
WORKDIR /app

CMD ["python", "app.py"]
