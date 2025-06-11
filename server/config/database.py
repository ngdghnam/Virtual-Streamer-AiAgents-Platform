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
        
        # Switch to the created database
        cursor.execute(f"USE {env_vars.DB_NAME}")
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                student_id VARCHAR(12),
                full_name VARCHAR(100) NOT NULL,
                DOB DATETIME NOT NULL,
                phone VARCHAR(20) NOT NULL,
                personal_email VARCHAR(100) UNIQUE NOT NULL,
                department VARCHAR(60) NOT NULL,
                member_password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        """)
        logger.info("table created successfully or already existed")
        
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