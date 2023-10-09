# database_access.py
import sqlite3

class SequenceDatabase:
    def __init__(self, db_file):
        self.db_file = db_file

    def create_table(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sequences (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    sequence TEXT
                )
            ''')
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def insert_sequence(self, name, sequence):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO sequences (name, sequence) VALUES (?, ?)", (name, sequence))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")

    def get_all_sequences(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute("SELECT name, sequence FROM sequences")
            rows = cursor.fetchall()
            conn.close()
            return rows
        except sqlite3.Error as e:
            print(f"Error retrieving data: {e}")
            return []

if __name__ == "__main__":
    db_file = "sequence_database.db"
    db = SequenceDatabase(db_file)
    db.create_table()

    # Example: Inserting a sequence
    db.insert_sequence("Sequence 1", "AGCTACGTA")
    db.insert_sequence("Sequence 2", "TACGTACGT")
    
    # Example: Retrieving all sequences
    sequences = db.get_all_sequences()
    print("All Sequences:")
    for name, sequence in sequences:
        print(f"Name: {name}, Sequence: {sequence}")
