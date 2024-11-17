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
        self.connection.commit()

    def add_quiz(self, id, title, description):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Quiz(id, title, description) VALUES (?, ?, ?)", [id, title, description])
        self.connection.commit()
        cursor.close()

    def add_que(self, Question_id, Quiz_id, Content):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Questions(Question_id, Quiz_id, Content) VALUES (?, ?, ?)", [Question_id, Quiz_id, Content])
        self.connection.commit()
        cursor.close()

    def get_quiz(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Quiz")
        res = cursor.fetchall()
        return res

    def get_que(self, Quiz_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Questions WHERE Quiz_id = ?", [Quiz_id])
        res = cursor.fetchall()
        cursor.close()
        return res