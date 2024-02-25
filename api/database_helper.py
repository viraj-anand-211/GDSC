import asyncio
import aiosqlite
import sqlite3 
from  datetime import datetime

db_file = 'database.db'

def insert_or_update_location(location, value):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # Check if the location already exists
    cursor.execute("SELECT value FROM Data WHERE location = ?", (location,))
    data = cursor.fetchone()
    if data is None:
        # Location does not exist, insert new record
        sql_query = "INSERT INTO Data (location, value) VALUES (?, ?)"
        cursor.execute(sql_query, (location, value))
        conn.commit()
        new_id = cursor.lastrowid  # Get the ID of the new entry
        conn.close()
        return new_id  # Return the ID of the newly created entry
    else:
        # Location exists, update the existing record
        sql_query = "UPDATE Data SET value = ? WHERE location = ?"
        cursor.execute(sql_query, (value, location))
        conn.commit()
        conn.close()
        return None  # Return None if the entry was updated
    
def get_from_database():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # Check if the location already exists
    cursor.execute("SELECT location, value FROM Data")
    data = cursor.fetchall()
    if data is None:
        return None 
    else:
        return data 

def init_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            value TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
