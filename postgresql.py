from sqlalchemy import create_engine, select, distinct
from sqlalchemy.orm import sessionmaker, Session
import pandas as pd

import classes
from constants import psql_data, sql_query
from classes import Ziraat


def connect_to_psql():
    # creating url for database connecting
    db_url = f"postgresql://{psql_data['user']}:{psql_data['password']}@localhost:5432/{psql_data['database']}"
    try:
        engine = create_engine(db_url)
        print(f'Connect to {db_url} is successful')
    except Exception as e:
        print(f'Unable to connect to {db_url}: {e}')
        engine = None

    return engine


def df_to_sql(df, engine):
    df.to_sql('ziraat', engine, if_exists='replace', index=True, index_label='Index')
    print('psql table filled successfully')
    return True


def read_sql():
    engine = connect_to_psql()
    print('Connected to database')
    pandas_df = pd.read_sql(sql_query, con=engine)
    print('pd was created successfully')
    return pandas_df

