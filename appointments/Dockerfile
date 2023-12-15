# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app/appointments

# Install Flask and pymongo
RUN pip install --no-cache-dir Flask 

# Copy the Flask application code to the working directory
COPY . .

# Expose the port that the Flask application will be running on
EXPOSE 7070

# Set the environment variable for the MongoDB URL
# ENV APPOINTMENTS_DB_URL="localhost:27017"

# Run the Flask application
CMD ["python", "app.py"]