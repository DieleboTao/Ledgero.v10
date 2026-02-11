# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY backend/ .

# Set Python path
ENV PYTHONPATH=/app

# Start FastAPI using Render's assigned port
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]
