# task 2
#2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv
import pandas as pd

df = pd.read_csv('dz.csv')
average_salary = df.groupby('City')['Salary'].mean()

print(average_salary)
