import pandas as pd
from icecream import ic

# 1 Створіть DataFrame Pandas із щонайменше 5 рядками та 3 стовпцями. Стовпці можуть представляти різні атрибути (наприклад, Ім'я, Вік, Місто).

df1 = pd.DataFrame(
    [
        ["John", 25, "New York"],
        ["Bob", 30, "Chicago"],
        ["Alice", 29, "Boston"],
        ["Mary", 28, "Los Angeles"],
        ["Kate", 27, "San Francisco"],
    ],
    index=[1, 2, 3, 4, 5],
    columns=["Name", "Age", "City"],
)

# 2 Додайте новий стовпець до DataFrame, який представляє числове значення.

df1["Salary"] = [1000, 2000, 3000, 4000, 5000]

# 3  Відфільтруйте DataFrame, щоб показати лише рядки, де числове значення більше певного порогу (ви можете визначити поріг).

filter = df1[df1["Salary"] > 3000]

# 4  Завантажте набір даних за допомогою Pandas (ви можете використовувати будь-який набір даних у форматі CSV або wine.csv).

df2 = pd.read_csv("C:/Users/Admin/PycharmProjects/hw1/wine.csv")

# 5  Відобразіть перші 5 рядків набору даних.

head = df2.head(5)

# 6 Розрахуйте та виведіть загальну статистику для числових стовпців у наборі даних.

describe = df2.describe()

# 7 Знайдіть та виведіть унікальні значення у категорійному стовпці.

unique = df2["1"].unique()

ic(
    df1,
    filter,
    head,
    describe,
    unique,
)
