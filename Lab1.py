numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим индекс пропущенного элемента
missing_index = numbers.index(None)

# Убираем пропущенный элемент из списка для расчета среднего
numbers_without_missing = [num for num in numbers if num is not None]

# Вычисляем среднее арифметическое
average = sum(numbers_without_missing) / len(numbers_without_missing)

# Заменяем пропущенный элемент на среднее арифметическое
numbers[missing_index] = average

# Выводим измененный список
print("Измененный список:", numbers)



# TODO заменить значение пропущенного элемента средним арифметическим

