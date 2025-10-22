# Dockerfile for Hugging Face Space
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port used by HF Spaces
EXPOSE 7860

# Run FastAPI app
CMD ["uvicorn", "inference_app:app", "--host", "0.0.0.0", "--port", "7860"]
