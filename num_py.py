import numpy as np
from icecream import ic

# 1
# Створіть масив NumPy із 10 випадкових цілих чисел. Виконайте наступні операції:
#   Знайдіть середнє, медіану та стандартне відхилення масиву.
#    Замініть всі парні числа у масиві на 0.

arr1 = np.random.randint(100, size=(10))
mean = np.mean(arr1)
median = np.median(arr1)
std = np.std(arr1)

# 2 Індексація та зрізка в NumPy:
#
# Створіть 2D масив NumPy (матрицю) розміром (3, 3) із випадковими цілими числами.
# Виведіть перший рядок матриці.
# Виведіть останній стовпець матриці.
# Виведіть діагональні елементи матриці.

arr2 = np.random.randint(0, 100, size=(3, 3))
row1 = arr2[0]
col3 = arr2[:, -1]
diag = arr2.diagonal()

# 3
# Створіть 2D масив NumPy розміром (3, 3) та 1D масив розміром (3,).
# Використайте broadcasting для додавання 1D масиву до кожного рядка 2D масиву.

arr3 = np.random.randint(0, 100, size=(3, 3))
arr4 = np.random.randint(0, 100, size=(3))
arr34 = arr3 + arr4

# 4
# Створіть 2D масив NumPy розміром (5, 5) з випадковими цілими числами.
#   Знайдіть та виведіть всі унікальні елементи у масиві.
#   виведіть всі рядки, сума елементів у яких більша за певне значення. (значення оберіть самі)

arr5 = np.random.randint(0, 100, size=(5, 5))
unique = np.unique(arr5)
sum = np.sum(arr5, axis=1)
arr5_filter = arr5[sum > 250]

# 5 Створіть 1D масив NumPy, що містить цілі числа від 1 до 20 (включно).
#   Використайте оператор shape, щоб перетворити 1D масив у 2D масив розміром (4, 5).
#   Переконайтеся, що отриманий перетворений масив має бажаний розмір.

arr6 = np.arange(1, 21)
arr6.shape = (4, 5)

ic(arr1, mean, median, std)
ic(arr2, row1, col3, diag)
ic(arr3, arr4, arr34)
ic(arr5, unique, arr5_filter)
ic(arr6)