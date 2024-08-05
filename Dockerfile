# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install Flask
RUN pip install Flask

# Create a directory for the application
WORKDIR /app

# Copy the application files to the container
COPY SafetyDance.py /app

# Expose port 80
EXPOSE 80

# Run the application
CMD ["python", "SafetyDance.py"]
