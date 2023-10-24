from functions import *


start, end = search_transactions_table()
# print(start)
df = make_dataframe(start, end)
print(df)
month_stats(df)