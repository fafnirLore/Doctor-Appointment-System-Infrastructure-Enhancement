# Use the official Python image as the base image
FROM python:3.9-slim


# Install MongoDB
# RUN apt-get update && apt-get install -y gnupg2 && \
#     wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add - && \
#     echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list && \
#     apt-get update && apt-get install -y mongodb-org && \
#     rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app/doctors

# Install Flask and pymongo
RUN pip install --no-cache-dir Flask

# Copy the Flask application code to the working directory
COPY . .

# Expose the port that the Flask application will be running on
EXPOSE 9090

# Set the environment variable for the MongoDB URL
ENV APPOINTMENTS_DB_URL="localhost:27017"

# Run the Flask application
CMD ["python", "app.py"]