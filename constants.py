data = 'data.xlsx'

search_string_start = 'Date'
search_string_end = 'Amount Owed'

# ['Date', 'Invoice No.', 'Explanation', 'Transaction Amount', 'Balance']

psql_data = {
    'user': 'postgres',
    'password': 'postgres',
    'database': 'ziraat'
}

""""
    Date" timestamp without time zone,
   "Invoice No." text,
   "Explanation" text,
   "Transaction Amount" double precision,
   "Balance" double precision
   """

sql_query = "SELECT * FROM ziraat"

ziraat_ai_data = {'secret_key': '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',
                  }
