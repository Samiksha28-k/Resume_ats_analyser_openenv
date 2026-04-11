FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install uv
RUN uv sync

EXPOSE 7860

CMD ["uv", "run", "inference.py"]
