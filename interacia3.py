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
        matrix = []
        print(f"Введите элементы матрицы {size}x{size} через пробел:")
        for i in range(size):
            row = list(map(int, input().split()))
            if len(row) != size:
                print(f"Ошибка: введите ровно {size} элементов.")
                return None
            matrix.append(row)
        return np.array(matrix)

    def display_matrix(self, matrix, name):
        print(f"{name}:")
        print(matrix)

    def sum_matrices(self, matrix1, matrix2):
        return matrix1 + matrix2

    def calculate_determinant(self, matrix):
        return np.linalg.det(matrix)

    def main(self):
        while True:
            print("\nМеню:")
            print("1. Ввод исходных данных")
            print("2. Выполнение алгоритма")
            print("3. Вывод результата")
            print("4. Завершение работы программы")

            choice = input("Выберите пункт меню: ")

            if choice == '1':
                size = int(input("Введите размер квадратных матриц: "))
                print("Выберите способ ввода данных:")
                print("1. Вручную")
                print("2. Сгенерировать случайным образом")
                input_method = input("Выберите способ ввода: ")

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

if __name__ == "__main__":
    matrix_ops = MatrixOperations()
    matrix_ops.main()
