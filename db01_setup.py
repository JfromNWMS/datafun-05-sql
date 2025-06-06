import sqlite3
from pathlib import Path
import pandas as pd

# Define the database directory in the current root project directory
db_dir = Path("data")
# Create the database directory if it does not exist
db_dir.mkdir(exist_ok = True)
# Define the database file in the database directory
db_file = db_dir.joinpath("project.sqlite3")
# Define a dictionary for execute_sql() messaging
message_dict: dict = {
  '01_drop_tables.sql': ["Tables dropped successfully.", "Error dropping tables: "],
  '02_create_tables.sql': ["Tables created successfully.", "Error creating tables: "],
  '03_insert_records.sql': ["Records inserted successfully.", "Error inserting records: "],
  'delete_records.sql': ["Record deleted successfully.", "Error deleting record: "],
  'update_records.sql': ["Record updated successfully.", "Error updating record: "],
}


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


def execute_sql(sql_file: Path) -> None:
    """Function takes in mandatory arg pathlib.Path object for a SQL script file and
    and executes the script in the database. """
    message = message_dict.get(sql_file.name) or [f"{sql_file} ran successfully.", f"Error running {sql_file}: "]
    try:
        with sqlite3.connect(db_file) as conn:
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print(message[0])
    except sqlite3.Error as e:
        print(message[1], e)
        

def query_sql(sql_file: Path) -> pd.DataFrame:
    """Function takes in mandatory arg pathlib.Path object for a query SQL script file,
    executes the script in the database, and then returns a pd.DataFrame with the results. """
    try:
        with sqlite3.connect(db_file) as conn:
            with open(sql_file, "r") as file:
                sql_script = file.read()
            query_return: pd.DataFrame = pd.read_sql(sql_script, conn)
            print(f"{sql_file.name} ran successfully.\n")
            return query_return
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"{sql_file.name} encountered Error: {e}\n")
        return pd.DataFrame()
    

def main():
    create_database()
    execute_sql(Path('sql_create', '01_drop_tables.sql'))
    execute_sql(Path('sql_create', '02_create_tables.sql'))
    execute_sql(Path('sql_create', '03_insert_records.sql'))


if __name__ == "__main__":
    main()
