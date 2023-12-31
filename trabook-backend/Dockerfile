# Use the official Python image as a base
FROM python:3.10

# Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create and activate the virtual environment
RUN rm -rf venv && \
    python3 -m venv venv --without-pip && \
    . venv/bin/activate && \
    pip install --no-cache-dir --upgrade pip && \
    python3 -m ensurepip --default-pip

# Install project dependencies
RUN . venv/bin/activate && \
    pip install gunicorn && \
    pip install -r reqs.txt

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run Django using Gunicorn
CMD ["venv/bin/gunicorn", "trabook-backend.wsgi:application", "--bind", "0.0.0.0:8000"]
