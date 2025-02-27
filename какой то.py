ЗАДАЧА 1
from openpyxl import load_workbook

def get_row_from_excel(file_path, row_index):
    try:
        # Загрузка Excel файла
        workbook = load_workbook(filename='Лист XLSX.xlsx')
        sheet = workbook.active  # Получаем активный лист

        # Получение строки по индексу (индексация с 1)
        row = [cell.value for cell in sheet[row_index + 1]]

        return row
    except Exception as e:
        return f"Произошла ошибка: {e}"

# Пример использования
file_path = input("Введите имя файла (например, data.xlsx): ")
row_index = int(input("Введите номер строки (начиная с 0): "))

result = get_row_from_excel(file_path, row_index)
print(result)





ЗАДАЧА 2 ДЛЯ НЕЁ 1 ФОТКА
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)

y_1 = np.sin(x)
y_2 = np.cos(x)
y_3 = np.tan(x)
plt.plot (x,y_1, y_2, y_3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y_1 = sin(x)')
plt.title('График функции y_2 = cos(x)')
plt.title('График функции y_3 = tan(x)')
plt.grid(True)
plt.show()





ЗАДАЧА 3 ДЛЯ НЕЁ 2 ФОТКИ
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Создание данных для графика
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Пользовательская функция для z
def custom_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2)) + np.cos(x) * np.sin(y)

z = custom_function(x, y)

# Создание 3D графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Построение поверхности
ax.plot_surface(x, y, z, cmap='plasma')

# Настройка меток осей
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Ось Z')

# Отображение графика
plt.show()
