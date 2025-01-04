import numpy as np
import random

class MatrixOperations:
    def __init__(self):
        self.matrix1 = None
        self.matrix2 = None
        self.result = None

    def generate_random_matrix(self, size):
        return np.random.randint(0, 10, size=(size, size))

    def input_matrix(self, size):
        # Заглушка для ввода матрицы
        print(f"Заглушка: Ввод матрицы {size}x{size}")
        return self.generate_random_matrix(size)

    def display_matrix(self, matrix, name):
        # Заглушка для отображения матрицы
        print(f"Заглушка: Отображение матрицы {name}")
        pass

    def sum_matrices(self, matrix1, matrix2):
        # Заглушка для суммирования матриц
        print("Заглушка: Суммирование матриц")
        return matrix1 + matrix2

    def calculate_determinant(self, matrix):
        # Заглушка для вычисления определителя матрицы
        print("Заглушка: Вычисление определителя матрицы")
        return np.linalg.det(matrix)

    def main(self):
        while True:
            print("\nМеню:")
            print("1. Ввод исходных данных")
            print("2. Выполнение алгоритма")
            print("3. Вывод результата")
            print("4. Завершение работы программы")

            # Заглушка для выбора пункта меню
            choice = '1'  # Заглушка: всегда выбираем пункт 1

            if choice == '1':
                size = 3  # Заглушка: размер матрицы 3x3
                print("Выберите способ ввода данных:")
                print("1. Вручную")
                print("2. Сгенерировать случайным образом")
                input_method = '2'  # Заглушка: всегда выбираем случайный ввод

                if input_method == '1':
                    self.matrix1 = self.input_matrix(size)
                    self.matrix2 = self.input_matrix(size)
                elif input_method == '2':
                    self.matrix1 = self.generate_random_matrix(size)
                    self.matrix2 = self.generate_random_matrix(size)
                else:
                    print("Неверный выбор.")
                    continue

                if self.matrix1 is not None and self.matrix2 is not None:
                    self.display_matrix(self.matrix1, "Матрица 1")
                    self.display_matrix(self.matrix2, "Матрица 2")
                    self.result = None  # Сброс результата

            elif choice == '2':
                if self.matrix1 is not None and self.matrix2 is not None:
                    self.result = self.sum_matrices(self.matrix1, self.matrix2)
                    print("Алгоритм выполнен.")
                else:
                    print("Сначала введите исходные данные.")

            elif choice == '3':
                if self.result is not None:
                    print("Результат:")
                    self.display_matrix(self.result, "Сумма матриц")
                    determinant = self.calculate_determinant(self.result)
                    print(f"Определитель результата: {determinant}")
                else:
                    print("Сначала выполните алгоритм.")

            elif choice == '4':
                print("Завершение работы программы.")
                break

            else:
                print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")

            # Заглушка для завершения цикла после одного прохода
            break

if __name__ == "__main__":
    matrix_ops = MatrixOperations()
    matrix_ops.main()
