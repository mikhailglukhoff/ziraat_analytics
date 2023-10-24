import os

import pandas as pd

from constants import *


def rename_xlsx_file():
    # rename file for successful opening

    try:
        old_name = 'Hesap_Hareketleri_09102023.xlsx'
        new_name = 'data.xlsx'
        os.rename(old_name, new_name)
    except FileNotFoundError:
        print('File not found or already renamed to data.xlsx')


def search_transactions_table():
    # search neccessary data, using search from constants

    df_search = pd.read_excel(data)

    # searching for 'search_string_start'
    row_index_start = df_search[df_search.apply(lambda row: search_string_start in row.to_string(), axis=1)].index

    # searching for 'search_string_end'
    row_index_end = df_search[df_search.apply(lambda row: search_string_end in row.to_string(), axis=1)].index
    return row_index_start, row_index_end


def make_dataframe(row_index_start, row_index_end):
    # making a final Dataframe
    start_row = row_index_start[0] + 1
    end_row = row_index_end[0] - 1
    skip_rows = end_row - start_row
    df = pd.read_excel(data, header=start_row, nrows=skip_rows)
    # convert 'Date' column to datetime objects with right formatting
    df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y')
    return df


def balance(df):
    # balance
    total = df['Transaction Amount'].sum()
    print('Balance: ', round(total, 2))
    return total


def sum_of_incomes(df):
    # sum of incomes
    income_total = df[df['Transaction Amount'] > 0]['Transaction Amount'].sum()
    print('Total income: ', abs(round(income_total, 2)))
    return income_total


def sum_of_outcomes(df):
    # sum of outcomes
    outcome_total = df[df['Transaction Amount'] < 0]['Transaction Amount'].sum()
    print('Total outcome: ', abs(round(outcome_total, 2)))
    return outcome_total


def total_days(df):
    # number of days
    total_days = (df['Date'].max() - df['Date'].min()).days
    print('Total, days: ', total_days)


def max_income(df):
    # max income
    max_income = df['Transaction Amount'].idxmax()
    max_income_row = df.iloc[max_income]
    print('Max income: ', max_income_row)
    return max_income_row


def max_outcome(df):
    # max outcome
    max_outcome = df['Transaction Amount'].idxmin()
    max_outcome_row = df.iloc[max_outcome]
    print('Max outcome: ', max_outcome_row)
    return max_outcome_row


def average_income(df):
    # average income
    av_income = df[df['Transaction Amount'] > 0]['Transaction Amount'].mean()
    print('Average income: ', abs(round(av_income, 2)))
    return av_income


def average_outcome(df):
    # average outcome
    av_outcome = df[df['Transaction Amount'] < 0]['Transaction Amount'].mean()
    print('Average outcome: ', abs(round(av_outcome, 2)))
    return av_outcome


def median_income(df):
    # median income
    av_income = df[df['Transaction Amount'] > 0]['Transaction Amount'].median()
    print('Average income: ', abs(round(av_income, 2)))
    return av_income


def median_outcome(df):
    # median outcome
    av_outcome = df[df['Transaction Amount'] < 0]['Transaction Amount'].median()
    print('Average outcome: ', abs(round(av_outcome, 2)))
    return av_outcome


def month_stats(df):
    desired_year = None
    desired_month = None

    while desired_year is None or not (2000 <= desired_year <= 2099):
        try:
            desired_year = int(input('input a year: '))
        except ValueError:
            print("Пожалуйста, введите год в виде числа.")

    while desired_month is None or not (1 <= desired_month <= 12):
        try:
            desired_month = int(input('input a year: '))
        except ValueError:
            print("Пожалуйста, введите год в виде числа.")

    # Фильтруйте данные по заданному году и месяцу
    filtered_data = df[(df['Date'].dt.year == desired_year) & (df['Date'].dt.month == desired_month)]

    print(filtered_data)
    # Фильтруйте строки, где значение "Transaction Amount" отрицательное
    income_transactions = filtered_data[filtered_data['Transaction Amount'] > 0]
    total_income_amount = income_transactions['Transaction Amount'].sum()

    outcome_transactions = filtered_data[filtered_data['Transaction Amount'] < 0]
    total_outcome_amount = outcome_transactions['Transaction Amount'].sum()

    print("Amount of incomes:", abs(round(total_income_amount, 2)))
    print("Amount of outcomes:", abs(round(total_outcome_amount, 2)))
