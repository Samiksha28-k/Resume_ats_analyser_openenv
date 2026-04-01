FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install flask numpy

EXPOSE 8000

CMD ["python", "server/app.py"]
