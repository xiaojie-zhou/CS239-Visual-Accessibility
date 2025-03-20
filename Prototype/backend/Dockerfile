# Use the official Python 3.12 base image
FROM python:3.12

# Install system dependencies required for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app
COPY . /app

# Install Python dependencies globally
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5001

# Start the Flask application
CMD ["python", "app.py"]