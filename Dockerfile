# Use Python base image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy project files to container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Django will run on
EXPOSE 8000

# Run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
