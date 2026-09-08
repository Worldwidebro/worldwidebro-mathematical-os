FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements (from 60-APIS relative to build context parent)
COPY 60-APIS/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application and required modules
COPY 60-APIS/graph_api.py .
COPY _PIPELINES/ _PIPELINES/
COPY 12-CONTEXT/ 12-CONTEXT/
RUN echo "App and modules copied successfully"

# Set environment
ENV PYTHONUNBUFFERED=1
ENV GRAPH_API_KEY=changeme

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

# Run
CMD ["python", "-m", "uvicorn", "graph_api:app", "--host", "0.0.0.0", "--port", "8000"]
