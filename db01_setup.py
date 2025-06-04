import sqlite3
import pandas as pd
from pathlib import Path

# Define the database file in the current root project directory
db_file = Path("data", "project.sqlite3")


def create_database() -> None:
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)


def insert_data_from_csv() -> None:
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = Path("data", "authors.csv")
        book_data_path = Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)


message_dict: dict = {
  '01_drop_tables.sql': ["Tables dropped successfully.", "Error dropping tables:"],
  '02_create_tables.sql': ["Tables created successfully.", "Error creating tables:"],
  '03_insert_records.sql': ["Records inserted successfully.", "Error inserting records:"],
  'delete_records.sql': ["Record deleted successfully.", "Error deleting record:"],
  'update_records.sql': ["Record updated successfully.", "Error updating record:"],
  'query_aggregation.sql': ["Query ran successfully.", "Error running query:"],
  'default': ["Script ran successfully.", "Error running script:"]
}


def execute_sql(sql_file: Path) -> None:
    try:
        with sqlite3.connect(db_file) as conn:
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print(message_dict.get(sql_file.name, message_dict['default'])[0])
    except sqlite3.Error as e:
        print(message_dict.get(sql_file.name, message_dict['default'])[1], e)
        

def query_sql(sql_file: Path) -> pd.DataFrame:
    try:
        with sqlite3.connect(db_file) as conn:
            with open(sql_file, "r") as file:
                sql_script = file.read()
            query_return: pd.DataFrame = pd.read_sql(sql_script, conn)
            print(message_dict.get(sql_file.name, message_dict['default'])[0])
            return query_return
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(message_dict.get(sql_file.name, message_dict['default'])[1], e)
        return pd.DataFrame()

def main():
    create_database()
    execute_sql(Path('sql_create', '01_drop_tables.sql'))
    execute_sql(Path('sql_create', '02_create_tables.sql'))
    #insert_data_from_csv()
    execute_sql(Path('sql_create', '03_insert_records.sql'))


if __name__ == "__main__":
    main()
