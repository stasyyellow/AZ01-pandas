# task 1
import pandas as pd

df = pd.read_csv('City-Happiness-Index-2024.csv')

print("Первые 5 строк данных:")
print(df.head())

print("\nИнформация о данных:")
print(df.info())

print("\nСтатистическое описание данных:")
print(df.describe())
