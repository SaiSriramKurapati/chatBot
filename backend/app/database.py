from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import yaml

# === Load Configuration from YAML File ===
# This block loads the configuration settings from a YAML file.
# The configuration typically includes database connection strings and other environment-specific settings.
# Get the absolute path to the 'backend' directory
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Construct the full path to the 'config.yml' file
config_path = os.path.join(backend_dir, 'config.yaml')

# Load the YAML configuration
with open(config_path, "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

# === Determine Database URL ===
# This line determines the database connection URL.
# It first checks if a 'DATABASE_URL' environment variable is set.
# If the environment variable is not set, it falls back to using the 'main' database URL specified in the YAML configuration file.
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', cfg['database']['main']) # uncomment this line if you are cloning this repo and running in your local
# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# === Create SQLAlchemy Engine ===
# The engine is the core interface to the database in SQLAlchemy.
# It is responsible for establishing and managing connections to the database.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# === Create a Configured "Session" Class ===
# The sessionmaker factory function is used to create a session class.
# Sessions are used to interact with the database (e.g., querying, adding, deleting data).
# The session is configured not to autocommit transactions automatically and not to autoflush changes.
# The session is bound to the engine, meaning it uses the engine for database operations.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# === Create a Base Class for the ORM Models ===
# The declarative_base function returns a base class that all ORM models will inherit from.
# This base class is used by SQLAlchemy to know which classes are mapped to database tables.
Base = declarative_base()

# === Database Dependency ===
# This function is a dependency that can be used in FastAPI routes to get a database session.
# When called, it provides a session that can be used to interact with the database.
# The session is closed automatically once the operation is complete.
def get_db():
    # Creates a new session from the SessionLocal factory.
    db = SessionLocal()
    try:
        # Yield the session to the caller.
        yield db
    finally:
        # Close the session to free up resources.
        db.close()
