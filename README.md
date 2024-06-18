


# Docker Setup [Recommend]

This section describes how to use Docker Compose to set up and run the application. This method is recommended for development environments where Docker is preferred for managing application components.

## Prerequisites

- Docker installed on your machine.
- Docker Compose installed on your machine.

## First Time Setup

1. **Build and Run the Application**:
    Use Docker Compose to build and start all services defined in the `docker-compose.yml` file:

    ```bash
    docker-compose up --build
    ```

    This command builds the images if they do not exist and starts the containers. It runs the database initialization command and then starts the Flask application.

2. **Accessing the Application**:
    - The main web application will be accessible at `http://localhost:80`
    - Local file operations and additional services will be accessible at `http://localhost:8050`

## Stopping the Application

To stop all services and remove containers, use the following command:

```bash
docker-compose down
```

## Running Individual Services

You may want to run individual services manually for debugging or development purposes:

- **Initialize the Database**:
    ```bash
    docker-compose run --rm app flask --app app.web init-db
    ```

- **Start the Flask Development Server**:
    ```bash
    docker-compose up app
    ```

- **Start the Worker Service**:
    ```bash
    docker-compose up worker
    ```

- **Start the Redis Service**:
    ```bash
    docker-compose up redis
    ```

## Environment Variables

Ensure that all necessary environment variables are set up correctly in your `docker-compose.yml`. For sensitive data, consider using Docker secrets or external environment files (`.env`).

- here is the environment variables in the docker-compose file
    - "FLASK_APP",
    - "FLASK_ENV",
    - "SECRET_KEY",
    - "SQLALCHEMY_DATABASE_URI",
    - "OPENAI_API_KEY",
    - "REDIS_URI",
    - "PINECONE_API_KEY",
    - "PINECONE_ENV_NAME",
    - "PINECONE_INDEX_NAME",
    - "UPLOAD_URL",
    - "LANGFUSE_PUBLIC_KEY",
    - "LANGFUSE_SECRET_KEY",
    - "OPENAI_API_BASE_URL"



### Notes:

1. **Sensitive Data**: Make sure to replace any sensitive API keys and secrets with placeholders or environment variables managed outside of source control, especially in production environments.

2. **Commands**: Adjust the commands according to your actual setup needs, especially if you have specific scripts or tasks defined in your application.

3. **Docker Compose File**: The `command` in your Docker Compose for the `app` service is currently set to run both the database initialization and the Flask server sequentially. This is typically fine for development but reconsider if this approach fits your production deployment strategy.

By integrating this Docker setup into your README, you provide clear guidance on how to use Docker to manage and run your application effectively, ensuring a consistent environment across different setups.



# First Time Setup

## Using Pipenv [Recommended]

```
# Install dependencies
pipenv install

# Create a virtual environment
pipenv shell

# Initialize the database
flask --app app.web init-db

```

## Using Venv [Optional]

These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv.

```
# Create the venv virtual environment
python -m venv .venv

# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
flask --app app.web init-db
```

# Running the app [Pipenv]

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
flask --app app.web init-db
```

# Running the app [Venv]

_These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv._

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
flask --app app.web init-db
```




