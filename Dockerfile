# Базовый образ с Python 3.12
FROM python:3.12-bullseye

# Отключение создания файлов .pyc и буферизации вывода
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Установка рабочей директории
WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && \
    apt-get install -y python3-dev gcc musl-dev && \
    rm -rf /var/lib/apt/lists/*

# Копирование файлов проекта
ADD pyproject.toml /app/

# Установка pip и uv
RUN pip install --upgrade pip
RUN pip install uv

# Установка зависимостей проекта с использованием uv
RUN uv install --no-dev

# Копирование оставшихся файлов проекта
COPY . /app/

# Установка команды для запуска приложения (опционально, если используете FastAPI/uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
