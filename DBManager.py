import sqlite3
class DBManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)


    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Quiz (
        "id"	INT PRIMARY KEY,
        "Title"	varchar(255),
        "Description" TEXT
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Questions (
            "Question_id" INT PRIMARY KEY,
            "Quiz_id" INT,
            "Content" TEXT
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Options (
            Option_id INT PRIMARY KEY,
            Question_id INT,
            Content TEXT,
            IS_CORRECT BOOLEAN
        );        
        """)