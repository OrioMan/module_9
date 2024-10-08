# 1 Вариант

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']

first_result = [len(s) for s in first_strings if len(s) >= 5]
print(first_result)  # Это должно быть [10, 8, 8]


second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]
print(second_result)

combined_strings = first_strings + second_strings
third_result = {s: len(s) for s in combined_strings if len(s) % 2 == 0}
print(third_result)



# 2 вариант
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк из first_strings (> 5 символов)
first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. Список пар кортежей одинаковой длины
second_result = [(first, second) for first in first_strings for second in second_strings if len(first) == len(second)]

# 3. Словарь с чётной длиной строк
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)
