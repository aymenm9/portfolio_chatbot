FROM python:3.13-alpine

WORKDIR /app

RUN mkdir -p /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0","--port", "8000" ]