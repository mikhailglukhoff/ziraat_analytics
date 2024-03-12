import matplotlib.pyplot as plt


def boxplot(pandas_df):
    import matplotlib as plt
    plt.figure(figsize=(10, 6))
    plt.bar(payment_count, payment_sum)
    plt.xlabel('Количество платежей')
    plt.ylabel('Сумма платежей')
    plt.title('График количества платежей по сумме')
    plt.show()

    import matplotlib.pyplot as plt

    # Здесь представьте, что у вас есть данные из SQL-запроса
    months = [1, 2, 3, 4, 5]  # Месяцы
    payment_count = [10, 15, 12, 20, 18]  # Количество платежей
    payment_sum = [1000, 1500, 1200, 2000, 1800]  # Суммы платежей
