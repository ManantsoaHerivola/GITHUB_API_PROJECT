import sqlite3

def create_connection(db_path):
    """
    Create a connection to the SQLite database specified by db_path.

    Args:
        db_path (str): The path to the database file.

    Returns:
        sqlite3.Connection: An object connection to the database, or None if an error occurs.
    """
    try:
        connection = sqlite3.connect(db_path)
        print("Connection to the database succeeded")
        return connection
    except sqlite3.Error as e:
        print(f"Error when connecting to the database: {e}")
        return None

def create_table(connection):
    """
    Create tables named 'repositories' and 'commits' in the database if they don't exist.

    Args:
        connection (sqlite3.Connection): Active connection to the database.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS repositories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            url TEXT NOT NULL,
            language TEXT,
            forks INTEGER,
            stars INTEGER,
            open_issues INTEGER,
            watchers INTEGER,
            created_at TEXT,
            updated_at TEXT
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS commits (
            id INTEGER PRIMARY KEY,
            commit_message TEXT,
            author TEXT,
            date TEXT,
            url TEXT,
            repo_id INTEGER,
            FOREIGN KEY (repo_id) REFERENCES repositories (id)
        );
        """)
        connection.commit()
        print("Tables created successfully or already exist.")
    except sqlite3.Error as e:
        print(f"Error while creating tables: {e}")

def initialize_db(db_path):
    """
    Initialize the db: create a connection and the necessary tables.

    Args:
        db_path (str): The path to the db file.
    """
    connection = create_connection(db_path)
    if connection:
        create_table(connection)
        connection.close()
        print("Initialized DB successfully.")
    else:
        print("DB initialization impossible.")

if __name__ == "__main__":
    from config import DB_PATH
    initialize_db(DB_PATH)