# Use the official Python image
FROM python:3.11-slim

# Keep Python output visible in container logs
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY garden_advice.py ./

# Run the console application when the container starts
CMD ["python", "-u", "garden_advice.py"]
