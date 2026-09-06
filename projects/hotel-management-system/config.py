"""Environment-based application configuration."""
import os

DB_CONFIG = {
    "host": os.getenv("HOTEL_DB_HOST", "localhost"),
    "user": os.getenv("HOTEL_DB_USER", "root"),
    "password": os.getenv("HOTEL_DB_PASSWORD", ""),
    "database": os.getenv("HOTEL_DB_NAME", "management"),
}
