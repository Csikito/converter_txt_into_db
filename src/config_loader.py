from configparser import ConfigParser
from sqlalchemy import create_engine
import pymysql


def load_database_config():
    """
    Load database connection configuration from the 'config.ini' file.

    Reads the 'config.ini' file using the ConfigParser module and extracts
    the database connection settings from the 'Database' section.

    Returns:
    dict: A dictionary containing the database connection settings with keys:
        - 'host': Hostname of the database server.
        - 'user': Database user.
        - 'password': Password for the database user.
        - 'database': Database name.

    Example:
        {
            'host': 'localhost', 'user': 'myuser', 
            'password': 'mypassword', 'database': 'mydatabase'
        }
    """

    # Read the configuration file
    config = ConfigParser()
    config.read('config/config.ini')

    # Creating a MySQL connection using pymysql and SQLAlchemy
    # mysql+pymysql://user:password@host:3306/database
    engine = create_engine(f"mysql+pymysql://{config.get('Database', 'user')}:{config.get('Database', 'password')}@{config.get('Database', 'host')}:3306/{config.get('Database', 'database')}")

    return engine
