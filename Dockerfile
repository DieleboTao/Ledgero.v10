# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend folder content into /app
COPY backend/ .

# Expose port for FastAPI
EXPOSE 8000

# Set Python path so imports work
ENV PYTHONPATH=/app

# Start the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
