# Use official Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy project files
COPY . /app

# Set the Python module path
ENV PYTHONPATH=/app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
