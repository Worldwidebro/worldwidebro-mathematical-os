FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

ENV BROWSERCLAW_ENDPOINT=https://api.browseros.com/mcp
ENV BROWSERCLAW_API_KEY=

EXPOSE 5678

CMD ["python", "server.py"]
