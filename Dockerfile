# Stage 1: Build the Svelte application
FROM node:16 as build-svelte

# Set working directory for Svelte
WORKDIR /app

# Copy Svelte app files
COPY client/package*.json client/
COPY client/ /app/

# Install dependencies and build the Svelte app
RUN npm install && npm run build

# Stage 2: Setup the Flask application
FROM python:3.10-slim

# Set the working directory in the container for Flask
WORKDIR /usr/src/app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files
COPY . .

# Copy built Svelte app from the first stage
COPY --from=build-svelte /app/build /usr/src/app/client/build

# Environment variables can be defined or passed via docker-compose
ENV FLASK_APP=app.web
ENV FLASK_ENV=development

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app
CMD ["flask", "run", "--host=0.0.0.0"]
