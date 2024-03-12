from functions import *
from postgresql import *
from graph import *

start, end = search_transactions_table()
# print(start)
df = make_dataframe(start, end)

engine = connect_to_psql()

df_to_sql(df, engine)

pandas_df = read_sql()
print(pandas_df)




