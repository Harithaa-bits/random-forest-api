# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy app files
COPY ./app /app
COPY ./models /app/models
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
