import mysql.connector 
from config.environment import Settings
from config.logger import logger

env_vars = Settings()

my_database = mysql.connector.connect(
    host=env_vars.DB_HOST or "localhost",
    user=env_vars.DB_USER,
    password=env_vars.DB_PASSWORD,
    database=env_vars.DB_NAME
)

def create_database(): 
    cursor = my_database.cursor()
    
    try:
        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {env_vars.DB_NAME}")
        logger.info(f"Database {env_vars.DB_NAME} created or already exists")
        
        # Commit the changes
        my_database.commit()
        
    except mysql.connector.Error as err:
        logger.info(f"Database initialization failed: {err}")
        raise Exception(f"Database initialization failed: {err}")
    finally:
        # Close cursor and my_database
        cursor.close()
        my_database.close()
    

def check_connection():
    try:
        cursor = my_database.cursor()
        cursor.execute("SELECT 1")  # Simple query to test connection
        result = cursor.fetchone()
        cursor.close()
        
        if result and result[0] == 1:
            logger.info("Connected to database successfully")
            return True
        else:
            logger.info("Connection test failed")
            return False
    except mysql.connector.Error as err:
        logger.info(f"Database connection error: {err}")
        return False
    except Exception as e:
        logger.info(f"Unexpected error: {e}")
        return False