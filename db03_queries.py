import pandas as pd
from pathlib import Path
from db01_setup import query_sql


def main() -> None:
    for file_path in Path("sql_queries").iterdir():
        try:
            if file_path.name == "query_aggregation.sql":
                print(query_sql(file_path).iloc[0,0],'\n')    
            else:
                print(query_sql(file_path), '\n')
        except Exception as e:
            print(f"Error executing {file_path}: {e}\n")


if __name__ == "__main__":
    main()