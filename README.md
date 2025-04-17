# Example Telegram Bot

Welcome to the **Example Telegram Bot**! This is a fully ready-to-use template for building a Telegram bot with **Python**, **aiogram**, **PostgreSQL**, and **SQLAlchemy**. It includes all the basic features you need to create and manage a bot with minimal setup. Just clone the repository, configure the database, and you're good to go.

This template is designed to help you focus on building out your bot's features without having to worry about the underlying setup. It's the perfect starting point for your Telegram bot project.

## Features

- **User Registration**: The bot greets new users, collects their information (name, age), and stores it in the PostgreSQL database.
- **Admin Panel**: Easily manage dynamic and static buttons, update the welcome message, and access user details through the admin panel.
- **PostgreSQL Integration**: The project integrates PostgreSQL for database storage, using **SQLAlchemy** as the ORM to simplify database operations.
- **Poetry for Dependency Management**: Use **Poetry** to manage dependencies and keep everything tidy.
- **State Machine Support**: The bot supports finite state machines (FSM), making it easier to manage multi-step interactions like adding/removing buttons or handling registration.
- **Customizable Welcome Message**: Admins can modify the welcome message sent to new users, and this is saved for future use.

## Requirements

- Python 3.12+
- PostgreSQL (Make sure you have a PostgreSQL instance running)
- Poetry (for managing dependencies)
- Docker (optional, if you want to run the bot in a containerized environment)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yarolys/ExampleTelegramBot.git
cd ExampleTelegramBot
```

### 2. Install Dependencies

Make sure **Poetry** is installed. If it's not, you can follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

Then, run:

```bash
poetry install
```

This will install all the required dependencies listed in the `pyproject.toml` file.

### 3. Set Up PostgreSQL

Ensure that you have a **PostgreSQL** instance running. Create a new database for your bot, and update the `DATABASE_URL` in `src/config.py` with your connection details:

```python
DATABASE_URL = "postgresql://username:password@localhost/dbname"
```

Replace `username`, `password`, and `dbname` with your actual database credentials.

### 4. Database Migrations (Optional)

If you're setting up the database for the first time or need to run migrations, you can do so using **Alembic**.

1. First, ensure that **Alembic** is installed by running:

    ```bash
    poetry add alembic
    ```

2. To run migrations, use the following command:

    ```bash
    poetry run alembic upgrade head
    ```

This will apply the latest migrations to your PostgreSQL database.

### 5. Configure Your Telegram Bot

Create a new bot with [BotFather](https://core.telegram.org/bots#botfather) on Telegram. Once created, copy the token and update it in `src/config.py`:

```python
API_TOKEN = "your-telegram-bot-token"
```

### 6. Run the Bot

Once everything is configured, you can run the bot using:

```bash
poetry run python src/run.py
```

### 7. Optional: Docker Setup

If you want to run the bot in a Docker container, you can use the provided Docker setup.

1. Build and start the Docker containers:

    ```bash
    docker-compose up --build
    ```

2. The bot will now be running in a Docker container, and you can interact with it on Telegram.

## Project Structure

Here’s a breakdown of the key files and directories:

```bash
.
├── alembic.ini              # Alembic configuration for database migrations
├── docker-compose.yaml      # Docker Compose file for container setup
├── dockerfile               # Dockerfile for building the bot's image
├── logs/                    # Logs directory (contains bot logs)
├── poetry.lock              # Poetry lock file to ensure consistent dependencies
├── pyproject.toml           # Poetry project configuration
├── run.py                   # Main entry point for running the bot
└── src/
    ├── config.py            # Bot configuration file (API token, DB settings, etc.)
    ├── database/            # Database-related files (models, connection, migrations)
    │   ├── connection.py    # PostgreSQL database connection
    │   ├── models/          # Database models (user, buttons, etc.)
    │   ├── migrations/      # Alembic migration scripts
    │   └── __init__.py      # Initialization for the database module
    ├── handlers/            # Handlers for bot commands and interactions
    │   ├── start.py         # Bot start handler (greets users, etc.)
    ├── schemas.py           # Schemas for data validation
    └── utils/               # Utility scripts (filters, keyboards, etc.)
        ├── filter.py        # Filtering logic
        └── keyboard/        # Keyboard configuration (admin, user, etc.)
            ├── admin.py     # Admin panel keyboard setup
            └── user.py      # User-related keyboard setup
```

## Customization

You can easily customize the following:

- **Welcome Message**: Update the default welcome message via the admin panel.
- **Buttons**: Add, remove, or update buttons through the admin panel.
- **Bot Commands and Handlers**: Modify the behavior of the bot by editing the handler files under `src/handlers/`.
- **Database Models**: Modify the database models to store additional information about users or settings.

## Contribution

Feel free to contribute by opening issues or submitting pull requests if you have improvements or fixes.