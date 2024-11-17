# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry add gunicorn
RUN poetry install

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV FLASK_APP=app.py

# Run gunicorn server
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "app:app"]