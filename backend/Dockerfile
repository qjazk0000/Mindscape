FROM python:3.12-slim

# MySQL 클라이언트 컴파일용 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    libpq-dev \
    && apt-get clean

WORKDIR /backend

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]