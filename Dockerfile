# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory inside Docker
WORKDIR /app

# Copy all project files to Docker image
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run your Flask app
CMD ["python", "app.py"]
