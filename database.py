import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "student_predictions.db"
)


def create_table():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            hours_studied REAL,
            attendance REAL,
            previous_scores REAL,
            predicted_score REAL
        )
    """)
    try:
            cursor.execute(
                            "ALTER TABLE predictions ADD COLUMN student_name TEXT"
                       )
            connection.commit()
    except sqlite3.OperationalError:
            pass        
    


def save_prediction(
    student_name,
    hours_studied,
    attendance,
    previous_scores,
    predicted_score
):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO predictions
        (student_name,hours_studied, attendance, previous_scores, predicted_score)
        VALUES (?, ?, ?, ?,?)
    """, (
        student_name,
        hours_studied,
        attendance,
        previous_scores,
        predicted_score
    ))

    connection.commit()
    connection.close()


def get_predictions():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id,student_name,
        hours_studied,attendance,
                previous_scores,
        predicted_score
           FROM predictions
           ORDER BY id DESC
    """)

    data = cursor.fetchall()
    connection.close()

    return data


if __name__ == "__main__":
    create_table()
    print("Database created successfully!")
def delete_predictions():  
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM predictions")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='predictions'")

    connection.commit()
    connection.close()