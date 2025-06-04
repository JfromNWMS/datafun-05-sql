import pandas as pd
from pathlib import Path
from db01_setup import query_sql


def main() -> None:
    print(query_sql(Path('sql_queries', 'query_aggregation.sql')).iloc[0,0])
    print(query_sql(Path('sql_queries', 'query_filter.sql')))
    print(query_sql(Path('sql_queries', 'query_sorting.sql')))
    print(query_sql(Path('sql_queries', 'query_group_by.sql')))
    #files = [file_name for file_name in ]


if __name__ == "__main__":
    main()