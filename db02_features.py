from pathlib import Path
from db01_setup import execute_sql


def main() -> None:
    for file_path in Path("sql_features").iterdir():
        try:
            execute_sql(file_path)
        except Exception as e:
            print(f"Error executing {file_path}: {e}")


if __name__ == "__main__":
    main()
    