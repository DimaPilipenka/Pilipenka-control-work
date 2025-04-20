"""
Контрольная работа по основам Python.

Пожалуйста, реализуйте решение для каждой из 20 задач ниже.
Каждая задача представлена комментарием с описанием и пустой функцией с аннотациями типов.
Вам нужно написать код внутри каждой функции, чтобы она соответствовала описанию
и возвращала значение указанного типа.

Импортировать можно только стандартные модули Python (например, math, random, datetime, collections, typing).
"""

import math
import random
import datetime
from collections import Counter, defaultdict, deque # Разрешено использовать эти модули
# Импортируем типы для аннотаций
from typing import List, Tuple, Dict, Any, Optional, Set, Union

# === Задача 1: Обработка вложенных списков ===
# def flatten_and_filter(nested_list: List[Any], min_value: int) -> List[int]:
#     """
#     Принимает список, который может содержать целые числа и другие списки (с произвольной глубиной вложенности).

#     Задача:
#     1. Преобразовать вложенный список `nested_list` в одномерный (плоский) список, содержащий только целые числа из исходной структуры.
#     2. Оставить в плоском списке только те числа, которые строго больше значения `min_value`.
#     3. Удалить дубликаты чисел.
#     4. Вернуть итоговый список чисел, отсортированный по возрастанию.

#     Пример:
#     flatten_and_filter([[1, 2, [3, 4, [5]]], 6, [7, 8]], 3) вернет [4, 5, 6, 7, 8]
#     flatten_and_filter([10, [12, [1, [15]]], 8, []], 10) вернет [12, 15]
#     flatten_and_filter([1, [2, [3]]], 5) вернет []
#     flatten_and_filter([], 0) вернет []
#     """
#     # Ваше решение здесь
#     result: List[int] = [] # Пример инициализации переменной нужного типа
#     # ... ваш код ...
#     return result


def flatten_and_filter(nested_list: List[Any], min_value: int) -> List[int]:
    def flatten(lst: List[Any]) -> List[int]:
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            elif isinstance(item, int):
                flat_list.append(item)
        return flat_list

    # Плоский список с целыми числами
    flat_list = flatten(nested_list)
    
    # Удаляем числа, которые меньше или равны min_value и убираем дубликаты
    filtered_set: Set[int] = {num for num in flat_list if num > min_value}
    
    # Возвращаем отсортированный список
    return sorted(filtered_set)

# === Задача 2: Анализ текста ===
# def analyze_text_complexity(text: str) -> Dict[str, float]:
#     """
#     Анализирует сложность текста, вычисляя несколько метрик.

#     Задача:
#     1. Очистить текст от знаков препинания: '.', ',', '!', '?', ':', ';', '"'. Дефисы внутри слов (например, "веб-разработка") должны сохраняться.
#     2. Привести весь текст к нижнему регистру.
#     3. Разделить текст на слова (по пробелам).
#     4. Посчитать общее количество слов (`total_words`).
#     5. Посчитать количество уникальных слов (`unique_words`).
#     6. Вычислить коэффициент лексического разнообразия (`lexical_diversity`) как отношение `unique_words / total_words`. Если `total_words` равно 0, коэффициент равен 0.0.
#     7. Вычислить среднюю длину слова (`average_word_length`). Считаются только буквы. Сумма длин всех слов (только буквы) / `total_words`. Если `total_words` равно 0, средняя длина равна 0.0.
#     8. Вернуть словарь с четырьмя ключами: 'total_words', 'unique_words', 'lexical_diversity', 'average_word_length'. Значения должны быть числами (int для *_words, float для остального), но для совместимости возвращаем все как float.

#     Пример:
#     text = "Это пример текста, для примера! Текста простого."
#     # Очищенный и в нижнем регистре: "это пример текста для примера текста простого"
#     # Слова: ["это", "пример", "текста", "для", "примера", "текста", "простого"]
#     # total_words: 7
#     # unique_words: 5 ("это", "пример", "текста", "для", "простого")
#     # lexical_diversity: 5 / 7
#     # average_word_length: (3 + 6 + 6 + 3 + 7 + 6 + 8) / 7 = 39 / 7
#     analyze_text_complexity(text) вернет примерно {'total_words': 7.0, 'unique_words': 5.0, 'lexical_diversity': 0.714..., 'average_word_length': 5.571...}
#     analyze_text_complexity("") вернет {'total_words': 0.0, 'unique_words': 0.0, 'lexical_diversity': 0.0, 'average_word_length': 0.0}
#     """
#     # Ваше решение здесь
#     result: Dict[str, float] = {
#         'total_words': 0.0,
#         'unique_words': 0.0,
#         'lexical_diversity': 0.0,
#         'average_word_length': 0.0
#     }
#     # ... ваш код ...
#     return result

import string

def analyze_text_complexity(text: str) -> Dict[str, float]:
    # Шаг 1: Очистка текста от знаков препинания
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Шаг 2: Приведение текста к нижнему регистру
    cleaned_text = cleaned_text.lower()
    
    # Шаг 3: Разделение текста на слова
    words = cleaned_text.split()
    
    # Шаг 4: Общее количество слов
    total_words = len(words)
    
    # Шаг 5: Количество уникальных слов
    unique_words_set = set(words)
    unique_words = len(unique_words_set)
    
    # Шаг 6: Коэффициент лексического разнообразия
    lexical_diversity = unique_words / total_words if total_words > 0 else 0.0
    
    # Шаг 7: Средняя длина слова (считаем только буквы)
    total_letters = sum(len(word) for word in words)
    average_word_length = total_letters / total_words if total_words > 0 else 0.0
    
    # Шаг 8: Формируем результат
    result: Dict[str, float] = {
        'total_words': float(total_words),
        'unique_words': float(unique_words),
        'lexical_diversity': float(lexical_diversity),
        'average_word_length': float(average_word_length)
    }
    
    return result



# # === Задача 3: Группировка строк по первой букве ===
# def group_by_first_letter(strings: List[str]) -> Dict[str, List[str]]:
#     """
#     Группирует непустые строки из списка по их первой букве.

#     Задача:
#     1. Обработать список строк `strings`.
#     2. Игнорировать пустые строки и строки, которые начинаются не с буквы латинского или русского алфавита.
#     3. Создать словарь, где ключами являются первые буквы слов (в нижнем регистре).
#     4. Значениями словаря должны быть списки строк, начинающихся на соответствующую букву. Строки в этих списках должны быть отсортированы в алфавитном порядке (лексикографически).
#     5. Вернуть полученный словарь.

#     Пример:
#     group_by_first_letter(["Apple", "Ant", "Banana", "Avocado", " ", "123", "Bat", "Яблоко", "ананас"])
#     вернет {'a': ['Ant', 'Apple', 'Avocado'], 'b': ['Banana', 'Bat'], 'я': ['Яблоко'], 'а': ['ананас']}
#     group_by_first_letter([]) вернет {}
#     group_by_first_letter(["", "1a", "a1"]) вернет {'a': ['a1']}
#     """
#     # Ваше решение здесь
#     result: Dict[str, List[str]] = defaultdict(list) # Удобно использовать defaultdict
#     # ... ваш код ...
#     # Не забудьте отсортировать списки перед возвратом
#     for key in result:
#         result[key].sort()
#     return dict(result) # Возвращаем обычный dict





from collections import defaultdict

def group_by_first_letter(strings: List[str]) -> Dict[str, List[str]]:
    result: defaultdict = defaultdict(list)  # Используем defaultdict для удобства

    for string in strings:
        # Проверяем, не пустая ли строка и начинается ли она с буквы
        if string and (string[0].isalpha()):  # isalpha проверяет, является ли первый символ буквой
            first_letter = string[0].lower()  # Приводим первую букву к нижнему регистру
            result[first_letter].append(string)  # Добавляем строку в список по первой букве

    # Сортируем списки по алфавиту
    for key in result:
        result[key].sort()

    return dict(result)  # Возвращаем обычный dict




# # === Задача 5: Поиск ближайших дней рождений ===
# def find_upcoming_birthdays(contacts: Dict[str, str], days_limit: int) -> List[Dict[str, Any]]:
#     """
#     Находит контакты, у которых день рождения будет в ближайшие `days_limit` дней от сегодняшнего дня.

#     Параметры:
#     - `contacts`: Словарь, где ключ - имя контакта (str), значение - дата рождения в формате 'YYYY-MM-DD' (str).
#     - `days_limit`: Целое число (>= 0), количество дней вперед для поиска (включая сегодня).

#     Задача:
#     1. Определить текущую дату (использовать `datetime.date.today()`).
#     2. Для каждого контакта:
#         а) Преобразовать строку с датой рождения в объект `datetime.date`.
#         б) Определить дату *следующего* дня рождения этого контакта (он может быть в этом году или в следующем).
#            - Учесть високосные годы: если человек родился 29 февраля, а следующий год не високосный, его днем рождения в тот год считается 28 февраля.
#         в) Рассчитать, через сколько дней наступит этот следующий день рождения (`days_until`) от сегодняшней даты.
#         г) Если `0 <= days_until < days_limit`, то добавить информацию об этом контакте в результат.
#     3. Вернуть список словарей. Каждый словарь должен содержать:
#        - 'name': имя контакта (str)
#        - 'birthday_date': дата *следующего* дня рождения (объект `datetime.date`)
#        - 'days_until': количество дней до этого дня рождения (int)
#     4. Итоговый список должен быть отсортирован по возрастанию количества дней до дня рождения (`days_until`).

#     Пример (предположим сегодня 2024-10-26):
#     contacts = {"Alice": "1990-10-28", "Bob": "1985-11-01", "Charlie": "2000-02-29", "David": "1995-10-26"}
#     days_limit = 7
#     # Alice: следующий ДР 2024-10-28 (через 2 дня). Подходит.
#     # Bob: следующий ДР 2024-11-01 (через 6 дней). Подходит.
#     # Charlie: следующий ДР 2025-02-28 (т.к. 2025 не високосный). Далеко. Не подходит.
#     # David: следующий ДР 2024-10-26 (через 0 дней). Подходит.
#     find_upcoming_birthdays(contacts, 7) вернет (отсортированный список):
#     [
#         {'name': 'David', 'birthday_date': datetime.date(2024, 10, 26), 'days_until': 0},
#         {'name': 'Alice', 'birthday_date': datetime.date(2024, 10, 28), 'days_until': 2},
#         {'name': 'Bob', 'birthday_date': datetime.date(2024, 11, 1), 'days_until': 6}
#     ]
#     """
#     # Ваше решение здесь
#     # Подсказка: datetime.date, datetime.timedelta, обработка високосных лет.
#     result: List[Dict[str, Any]] = []
#     # ... ваш код ...
#     # result.sort(key=lambda x: x['days_until']) # Сортировка перед возвратом
#     return result

from datetime import date, timedelta
from typing import Dict, List, Any

def find_upcoming_birthdays(contacts: Dict[str, str], days_limit: int) -> List[Dict[str, Any]]:
    today = date.today()
    result = []

    for name, birthday_str in contacts.items():
        birth_date = date.fromisoformat(birthday_str)
        
        # Определяем следующий день рождения
        next_birthday_year = today.year
        next_birthday = birth_date.replace(year=next_birthday_year)

        if next_birthday < today:  # Если день рождения уже прошел в этом году
            next_birthday_year += 1
            next_birthday = birth_date.replace(year=next_birthday_year)

        # Обработка случая 29 февраля
        if birth_date.month == 2 and birth_date.day == 29:
            if (next_birthday_year % 4 != 0) or (next_birthday_year % 100 == 0 and next_birthday_year % 400 != 0):
                next_birthday = date(next_birthday_year, 2, 28)

        days_until = (next_birthday - today).days

        if 0 <= days_until < days_limit:
            result.append({
                'name': name,
                'birthday_date': next_birthday,
                'days_until': days_until
            })

    result.sort(key=lambda x: x['days_until'])  # Сортировка по количеству дней до дня рождения
    return result


# # === Задача 6: Поиск пути в сетке ===
# def find_path_in_grid(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
#     """
#     Ищет кратчайший путь в сетке от точки start до точки end.

#     Параметры:
#     - `grid`: Сетка (матрица) в виде списка списков целых чисел. 0 - проходимая ячейка, 1 - стена.
#     - `start`: Кортеж (row, col) - координаты начальной точки.
#     - `end`: Кортеж (row, col) - координаты конечной точки.
#     * Координаты (row, col) означают: row - индекс строки (сверху вниз, начиная с 0), col - индекс столбца (слева направо, начиная с 0). (0, 0) - верхний левый угол.

#     Правила:
#     - Двигаться можно только по горизонтали и вертикали (на одну ячейку за шаг).
#     - Нельзя проходить через стены (ячейки со значением 1).
#     - Нельзя выходить за пределы сетки.

#     Задача:
#     1. Найти кратчайший путь (по количеству шагов) от `start` до `end`.
#     2. Проверить корректность `start` и `end`:
#         - Если `start` или `end` находятся вне сетки (индексы выходят за границы).
#         - Если `start` или `end` указывают на ячейку-стену (значение 1).
#         В этих случаях путь невозможен, вернуть `None`.
#     3. Если `start` совпадает с `end`:
#         - Если ячейка `start` проходима (значение 0), вернуть `[start]`.
#         - Если ячейка `start` является стеной, вернуть `None` (согласно п.2).
#     4. Если путь от `start` к `end` существует и они разные, вернуть его в виде списка кортежей координат (row, col), включая `start` и `end`. Порядок должен быть от `start` к `end`.
#     5. Если путь не существует (например, `end` недостижим из `start`), вернуть `None`.

#     Подсказка: Используйте алгоритм Поиска в ширину (BFS). Вам понадобится очередь (например, `collections.deque`) для хранения ячеек к посещению и способ отслеживать посещенные ячейки и путь к ним (например, словарь `parent[cell] = previous_cell`, чтобы восстановить путь от `end` к `start`).

#     Пример:
#     grid = [[0, 0, 0, 1],
#             [1, 1, 0, 0],
#             [0, 0, 0, 1],
#             [0, 1, 1, 0],
#             [0, 0, 0, 0]]
#     start = (0, 0)
#     end = (4, 3)
#     # Ожидаемый кратчайший путь:
#     find_path_in_grid(grid, start, end) вернет [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3)]

#     grid2 = [[0, 1],
#              [1, 0]]
#     find_path_in_grid(grid2, (0, 0), (1, 1)) вернет None # Пути нет
#     find_path_in_grid(grid2, (0, 0), (0, 0)) вернет [(0, 0)] # Старт=конец, проходимо
#     find_path_in_grid(grid2, (0, 1), (0, 0)) вернет None # Старт на стене
#     find_path_in_grid(grid, (0, 0), (10, 10)) вернет None # end вне сетки
#     """
#     # Ваше решение здесь


from typing import List, Tuple, Optional
from collections import deque

def find_path_in_grid(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    rows, cols = len(grid), len(grid[0]) if grid else 0
    
    # Проверка корректности start и end
    if (not (0 <= start[0] < rows and 0 <= start[1] < cols) or 
        not (0 <= end[0] < rows and 0 <= end[1] < cols) or 
        grid[start[0]][start[1]] == 1 or 
        grid[end[0]][end[1]] == 1):
        return None

    # Если start совпадает с end
    if start == end:
        return [start] if grid[start[0]][start[1]] == 0 else None

    # BFS для поиска кратчайшего пути
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Вниз, вправо, вверх, влево

    while queue:
        current = queue.popleft()
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            if (0 <= neighbor[0] < rows and 
                0 <= neighbor[1] < cols and 
                neighbor not in visited and 
                grid[neighbor[0]][neighbor[1]] == 0):
                
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

                # Проверяем, достигли ли мы конечной точки
                if neighbor == end:
                    # Восстанавливаем путь
                    path = []
                    while neighbor is not None:
                        path.append(neighbor)
                        neighbor = parent[neighbor]
                    return path[::-1]  # Возвращаем путь в правильном порядке

    # Если путь не найден
    return None


# === Задача 7: Генератор случайных паролей ===
#def generate_secure_password(length: int, use_digits: bool, use_special_chars: bool) -> str:
    """
    Генерирует случайный пароль заданной длины с учетом требований к символам.

    Параметры:
    - `length`: Требуемая длина пароля (целое число).
    - `use_digits`: Если True, пароль должен содержать хотя бы одну цифру (0-9).
    - `use_special_chars`: Если True, пароль должен содержать хотя бы один спецсимвол из набора `!@#$%^&*()-_=+[]{}|;:',.<>?`.

    Требования к паролю:
    1. Длина пароля должна быть ровно `length`.
    2. Пароль всегда должен содержать хотя бы одну латинскую букву в нижнем регистре.
    3. Пароль всегда должен содержать хотя бы одну латинскую букву в верхнем регистре.
    4. Если `use_digits` is True, должен содержать хотя бы одну цифру.
    5. Если `use_special_chars` is True, должен содержать хотя бы один спецсимвол из указанного набора.
    6. Остальные символы пароля (если нужны для достижения длины `length`) должны быть случайными из всех разрешенных категорий (lowercase, uppercase, digits если `use_digits`, special если `use_special_chars`).
    7. Итоговый пароль должен быть хорошо перемешан.

    Ограничения и ошибки:
    - Минимальная длина пароля определяется обязательными символами. Как минимум 2 (upper + lower). Если `use_digits`, то 3. Если `use_special_chars`, то 3. Если оба, то 4.
    - Если запрошенная `length` меньше необходимого минимума для выполнения условий, функция должна возбуждать исключение `ValueError`.

    Подсказка:
    1. Определите минимально необходимую длину. Проверьте `length`.
    2. Сгенерируйте по одному обязательному символу из каждой требуемой категории.
    3. Сформируйте набор всех возможных символов для заполнения оставшейся части пароля.
    4. Сгенерируйте недостающее количество символов (`length` - количество_обязательных) из этого набора.
    5. Соберите все символы (обязательные + случайные) в один список.
    6. Тщательно перемешайте список (`random.shuffle`).
    7. Соедините символы списка в строку.

    Пример:
    generate_secure_password(12, True, True) может вернуть что-то вроде "aB3!cDefGHiJ" (длина 12, есть upper, lower, digit, special)
    generate_secure_password(8, True, False) может вернуть "P@ssW0rd" (нет, спецсимволы не нужны) -> "P4ssW0rd"
    generate_secure_password(5, False, False) может вернуть "PaSsW"
    generate_secure_password(3, True, True) вызовет ValueError (нужно минимум 4 символа)
    """
    # Ваше решение здесь
    

import random
import string

def generate_secure_password(length: int, use_digits: bool, use_special_chars: bool) -> str:
    """
    Генерирует случайный пароль заданной длины с учетом требований к символам.
    """
    # Определение минимально необходимой длины
    min_length = 2  # минимум 2 для lower и upper
    if use_digits:
        min_length += 1  # минимум 3 (lower, upper, digit)
    if use_special_chars:
        min_length += 1  # минимум 3 (lower, upper, special)
    
    if length < min_length:
        raise ValueError(f"Минимальная длина пароля должна быть не менее {min_length}")

    # Генерация обязательных символов
    password_chars = []
    password_chars.append(random.choice(string.ascii_lowercase))  # одна строчная буква
    password_chars.append(random.choice(string.ascii_uppercase))  # одна заглавная буква
    
    if use_digits:
        password_chars.append(random.choice(string.digits))  # одна цифра
    if use_special_chars:
        password_chars.append(random.choice("!@#$%^&*()-_=+[]{}|;:',.<>?"))  # один спецсимвол

    # Определение всех возможных символов для заполнения оставшейся части пароля
    possible_chars = string.ascii_lowercase + string.ascii_uppercase
    if use_digits:
        possible_chars += string.digits
    if use_special_chars:
        possible_chars += "!@#$%^&*()-_=+[]{}|;:',.<>?"
    
    # Генерация недостающих символов
    while len(password_chars) < length:
        password_chars.append(random.choice(possible_chars))

    # Перемешивание символов
    random.shuffle(password_chars)

    # Соединение символов в строку
    return ''.join(password_chars)



# # === Задача 8: Слияние интервалов ===
# def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
#     """
#     Объединяет перекрывающиеся или соприкасающиеся интервалы в списке.

#     Параметры:
#     - `intervals`: Список кортежей, где каждый кортеж `(start, end)` представляет интервал `[start, end]`.

#     Задача:
#     1. Отсортировать интервалы по их началу (`start`).
#     2. Пройти по отсортированным интервалам, объединяя те, которые перекрываются или соприкасаются.
#        - Интервалы `(a, b)` и `(c, d)` (где `a <= c`) перекрываются или соприкасаются, если `c <= b`.
#        - При слиянии новый интервал будет `(a, max(b, d))`.
#     3. Вернуть список объединенных интервалов, отсортированных по началу.

#     Пример:
#     merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)])
#     # Сортируем: [(1, 3), (2, 6), (8, 10), (15, 18)]
#     # (1, 3) и (2, 6): 2 <= 3 -> сливаем в (1, max(3, 6)) = (1, 6)
#     # Текущий результат: [(1, 6)]
#     # (1, 6) и (8, 10): 8 > 6 -> не сливаем. Добавляем (8, 10).
#     # Текущий результат: [(1, 6), (8, 10)]
#     # (8, 10) и (15, 18): 15 > 10 -> не сливаем. Добавляем (15, 18).
#     # Итог: [(1, 6), (8, 10), (15, 18)]
#     вернет [(1, 6), (8, 10), (15, 18)]

#     merge_intervals([(1, 4), (4, 5)])
#     # Сортируем: [(1, 4), (4, 5)]
#     # (1, 4) и (4, 5): 4 <= 4 -> сливаем в (1, max(4, 5)) = (1, 5)
#     # Итог: [(1, 5)]
#     вернет [(1, 5)]

#     merge_intervals([(10, 12), (1, 3), (5, 8), (2, 6)])
#     # Сортируем: [(1, 3), (2, 6), (5, 8), (10, 12)]
#     # (1, 3) и (2, 6): 2 <= 3 -> (1, 6)
#     # (1, 6) и (5, 8): 5 <= 6 -> (1, 8)
#     # (1, 8) и (10, 12): 10 > 8 -> не сливаем.
#     # Итог: [(1, 8), (10, 12)]
#     вернет [(1, 8), (10, 12)]

#     merge_intervals([]) вернет []
#     merge_intervals([(1, 5)]) вернет [(1, 5)]
#     """
#     # Ваше решение здесь

from typing import List, Tuple

def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Объединяет перекрывающиеся или соприкасающиеся интервалы в списке.
    """
    if not intervals:
        return []

    # 1. Сортируем интервалы по их началу
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        # 2. Проверяем, перекрываются или соприкасаются ли интервалы
        if start <= current_end:
            # Если да, объединяем их
            current_end = max(current_end, end)
        else:
            # Если нет, добавляем текущий интервал в результат и переходим к следующему
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    
    # Добавляем последний интервал
    merged.append((current_start, current_end))
    
    return merged


# # === Задача 9: Сбор дождевой воды ===
# def trap_rain_water_simple(heights: List[int]) -> int:
#     """
#     Вычисляет, сколько единиц воды может быть собрано между столбиками гистограммы после дождя.

#     Параметры:
#     - `heights`: Список неотрицательных целых чисел, представляющих высоты столбиков гистограммы. Ширина каждого столбика равна 1.

#     Задача:
#     1. Представить `heights` как гистограмму.
#     2. Рассчитать общее количество единиц воды, которое может быть удержано в "углублениях" этой гистограммы.
#     3. Вода над конкретным столбиком `i` удерживается, если есть столбики выше слева и справа от него. Уровень воды над столбиком `i` определяется самым низким из двух "ограничивающих" столбиков: максимальной высоты слева от `i` и максимальной высоты справа от `i`.
#     4. Количество воды над столбиком `i` равно `max(0, min(max_left_height, max_right_height) - heights[i])`.
#     5. Общее количество воды - это сумма воды над всеми столбиками. Крайние столбики (индекс 0 и n-1) не могут удерживать воду сами по себе.

#     Подсказка:
#     Можно заранее вычислить для каждого индекса `i` максимальную высоту слева (`max_left[i]`) и максимальную высоту справа (`max_right[i]`). Затем пройти по `heights` и посчитать воду для каждого `i` по формуле. Либо использовать метод двух указателей (один с начала, другой с конца).

#     Пример:
#     heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#     # max_left =  [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3] (max высота до i, не включая i)
#     # max_right = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0] (max высота после i, не включая i)
#     # water = [max(0, min(L, R) - H) for i]
#     # i=0: min(0, 3) - 0 = 0
#     # i=1: min(0, 3) - 1 = -1 -> 0
#     # i=2: min(1, 3) - 0 = 1
#     # i=3: min(1, 3) - 2 = -1 -> 0
#     # i=4: min(2, 3) - 1 = 1
#     # i=5: min(2, 3) - 0 = 2
#     # i=6: min(2, 3) - 1 = 1
#     # i=7: min(2, 2) - 3 = -1 -> 0
#     # i=8: min(3, 2) - 2 = 0
#     # i=9: min(3, 2) - 1 = 1
#     # i=10: min(3, 1) - 2 = -1 -> 0
#     # i=11: min(3, 0) - 1 = -1 -> 0
#     # Сумма: 0+0+1+0+1+2+1+0+0+1+0+0 = 6
#     trap_rain_water_simple([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) вернет 6

#     heights = [4, 2, 0, 3, 2, 5]
#     # max_left = [0, 4, 4, 4, 4, 4]
#     # max_right = [5, 5, 5, 5, 5, 0]
#     # water:
#     # i=0: min(0, 5)-4 = 0
#     # i=1: min(4, 5)-2 = 2
#     # i=2: min(4, 5)-0 = 4
#     # i=3: min(4, 5)-3 = 1
#     # i=4: min(4, 5)-2 = 2
#     # i=5: min(4, 0)-5 = 0
#     # Сумма: 0+2+4+1+2+0 = 9
#     trap_rain_water_simple([4, 2, 0, 3, 2, 5]) вернет 9
#     trap_rain_water_simple([1, 2, 3]) вернет 0
#     trap_rain_water_simple([]) вернет 0
#     """
#     # Ваше решение здесь

from typing import List

def trap_rain_water_simple(heights: List[int]) -> int:
    """
    Вычисляет, сколько единиц воды может быть собрано между столбиками гистограммы после дождя.
    """
    n = len(heights)
    if n == 0:
        return 0

    # Массивы для хранения максимальных высот слева и справа
    max_left = [0] * n
    max_right = [0] * n

    # Заполнение max_left
    max_left[0] = heights[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], heights[i])

    # Заполнение max_right
    max_right[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], heights[i])

    # Вычисление количества воды
    total_water = 0
    for i in range(n):
        water_at_i = max(0, min(max_left[i], max_right[i]) - heights[i])
        total_water += water_at_i

    return total_water



# # === Задача 10: Валидация структуры данных ===
# def validate_data_structure(data: Any, schema: Dict[str, type]) -> bool:
#     """
#     Проверяет, соответствует ли структура данных `data` заданной `schema`.

#     Параметры:
#     - `data`: Произвольные данные, которые должны быть словарем для успешной валидации.
#     - `schema`: Словарь, описывающий ожидаемую структуру:
#         - Ключи: Имена полей (str), которые должны присутствовать в `data`.
#         - Значения: Ожидаемые типы данных (type) для соответствующих ключей в `data` (например, `str`, `int`, `list`, `dict`, `bool`).

#     Задача:
#     1. Проверить, является ли `data` словарем (`isinstance(data, dict)`). Если нет, вернуть `False`.
#     2. Проверить, что все ключи, перечисленные в `schema`, присутствуют в `data`. Если хотя бы один ключ из `schema` отсутствует в `data`, вернуть `False`.
#     3. Для каждого ключа из `schema` проверить, что тип значения в `data` (`data[key]`) соответствует типу, указанному в `schema` (`schema[key]`). Используйте `isinstance(data[key], schema[key])`. Если тип не совпадает хотя бы для одного ключа, вернуть `False`.
#     4. Наличие в `data` дополнительных ключей, не упомянутых в `schema`, допускается и не влияет на результат валидации.
#     5. Если все проверки (1, 2, 3) пройдены успешно, вернуть `True`.

#     Пример:
#     schema = {"name": str, "age": int, "is_active": bool, "items": list}

#     validate_data_structure({"name": "Alice", "age": 30, "is_active": True, "items": [1, 2]}, schema) вернет True
#     validate_data_structure({"name": "Bob", "age": "25", "is_active": False, "items": []}, schema) вернет False (age имеет тип str, а не int)
#     validate_data_structure({"name": "Charlie", "is_active": True, "items": []}, schema) вернет False (отсутствует ключ 'age')
#     validate_data_structure({"name": "David", "age": 40, "is_active": False, "items": {}, "city": "NY"}, schema) вернет False (items имеет тип dict, а не list)
#     validate_data_structure({"name": "Eve", "age": 22, "is_active": True, "items": ["a"], "extra": 1}, schema) вернет True (дополнительный ключ 'extra' разрешен)
#     validate_data_structure(None, schema) вернет False (data не словарь)
#     validate_data_structure({}, schema) вернет False (отсутствуют все ключи)
#     """
#     # Ваше решение здесь
#     pass

from typing import Any, Dict

def validate_data_structure(data: Any, schema: Dict[str, type]) -> bool:
#Шаг 1: Проверьте, являются ли данные словарем
    if not isinstance(data, dict):
        return False
    
    # Проверьте, все ли ключи схемы присутствуют в данных
    for key in schema:
        if key not in data:
            return False
    
    # Убедиться, что значение каждого ключа соответствует ожидаемому типу
    for key, expected_type in schema.items():
        if not isinstance(data[key], expected_type):
            return False
    
  
    return True



# # === Задача 11: Расшифровка сообщения (Шифр Виженера) ===
# def decode_caesar_variant(encoded_text: str, key_word: str) -> str:
#     """
#     Декодирует текст, зашифрованный с использованием ключевого слова (похоже на шифр Виженера).

#     Параметры:
#     - `encoded_text`: Зашифрованный текст. Содержит только латинские буквы (a-z, A-Z) и пробелы.
#     - `key_word`: Ключевое слово. Содержит только латинские буквы в нижнем регистре (a-z). Не может быть пустым.

#     Правила шифрования (нужно выполнить обратную операцию - декодирование):
#     - Шифруются только буквы, пробелы остаются на своих местах.
#     - Сдвиг для каждой буквы шифруемого текста определяется буквой из `key_word`. Буквы `key_word` используются циклически.
#     - Величина сдвига равна порядковому номеру буквы `key_word` в алфавите (a=0, b=1, ..., z=25).
#     - Шифрование выполняется по формуле: `new_code = (original_code + shift) % 26`. Коды 0-25 соответствуют a-z или A-Z.
#     - Регистр букв при шифровании сохраняется (т.е. 'H' сдвигается так же, как 'h', но результатом будет буква в верхнем регистре).

#     Задача:
#     1. Реализовать декодирование `encoded_text` с использованием `key_word`.
#     2. Формула декодирования: `original_code = (encoded_code - shift + 26) % 26`.
#     3. Использовать буквы `key_word` циклически для определения `shift` только для букв в `encoded_text`. Пробелы не используют букву ключа.
#     4. Сохранять регистр букв и положение пробелов.
#     5. Вернуть раскодированный текст.

#     Пример:
#     key_word = "key" (сдвиги: k=10, e=4, y=24)
#     encoded = "Rijvs Tzwjn"
#     decode_caesar_variant(encoded, "key")
#     # R(17) - k(10) = 7 -> H
#     # i(8) - e(4) = 4 -> e
#     # j(9) - y(24) = -15 + 26 = 11 -> l
#     # v(21) - k(10) = 11 -> l
#     # s(18) - e(4) = 14 -> o
#     # Пробел -> Пробел
#     # T(19) - y(24) = -5 + 26 = 21 -> W
#     # Давайте проверим другой пример: "Lipps Asvph" с ключом "lemon"
#     # L(11)-l(11)=0 -> A
#     # i(8)-e(4)=4 -> e
#     # p(15)-m(12)=3 -> d
#     # p(15)-o(14)=1 -> b
#     # s(18)-n(13)=5 -> f
#     # Пробел
#     # A(0)-l(11)=-11+26=15 -> P
#     # s(18)-e(4)=14 -> o
#     # v(21)-m(12)=9 -> j
#     # p(15)-o(14)=1 -> b
#     # h(7)-n(13)=-6+26=20 -> u
#     # Результат: "Aedbf Pojbu" (Непохоже на осмысленный текст. Может, шифровалось ATTACK AT DAWN?)
#     # Шифруем "Hello World" ключом "key" (k=10, e=4, y=24)
#     # H(7)+k(10)=17->R
#     # e(4)+e(4)=8->i
#     # l(11)+y(24)=35%26=9->j
#     # l(11)+k(10)=21->v
#     # o(14)+e(4)=18->s
#     # Пробел
#     # W(22)+y(24)=46%26=20->U
#     # o(14)+k(10)=24->Y
#     # r(17)+e(4)=21->V
#     # l(11)+y(24)=35%26=9->J
#     # d(3)+k(10)=13->N
#     # Зашифровано: "Rijvs UYVJN"
#     decode_caesar_variant("Rijvs UYVJN", "key") вернет "Hello World"
#     decode_caesar_variant("Tbi Owi", "abc") # a=0, b=1, c=2
#     # T(19)-a(0)=19->T (Сохраняем регистр!) -> S
#     # b(1)-b(1)=0->a
#     # i(8)-c(2)=6->g
#     # Пробел
#     # O(14)-a(0)=14->O
#     # w(22)-b(1)=21->v (Сохраняем регистр!) -> u
#     # i(8)-c(2)=6->g
#     # Результат: "Sag Oug" (Похоже на "Say Oui", но g вместо y? y(24)+c(2)=26%26=0->A. Да, видимо так шифровалось "Say Oua"?)
#     # Пусть будет так:
#     decode_caesar_variant("Tbi Owa", "abc") вернет "Say Ouy" ( T(19)-a(0)=S(18), b(1)-b(1)=a(0), i(8)-c(2)=g(6). O(14)-a(0)=O(14), w(22)-b(1)=v(21), a(0)-c(2)=-2+26=y(24) ) - > Sag Ovy? Что-то сложно с примерами. Главное - реализовать логику декодирования.

#     вернет раскодированный текст (str).
#     """
#     # Ваше решение здесь
#     # Подсказка: используйте ord() и chr(). Помните о базах 'a' и 'A'.
#     # Следите за индексом ключа key_word_index, увеличивая его только при обработке буквы.
#     pass

def decode_caesar_variant(encoded_text: str, key_word: str) -> str:
    key_shifts = [ord(c) - ord('a') for c in key_word]
    key_length = len(key_shifts)
    key_index = 0
    result = []
    
    for c in encoded_text:
        if c == ' ':
            result.append(' ')
            continue
        if c.isalpha():
            # Определите основу для прописных или строчных букв
            base = ord('A') if c.isupper() else ord('a')
            current_code = ord(c) - base
            shift = key_shifts[key_index]
            original_code = (current_code - shift + 26) % 26
            original_char = chr(original_code + base)
            result.append(original_char)
            # Переход к следующему ключевому символу
            key_index = (key_index + 1) % key_length
    return ''.join(result)





# # === Задача 12: Уплощение словаря ===
# def flatten_dict(nested_dict: Dict[str, Any], separator: str = '_') -> Dict[str, Any]:
#     """
#     Преобразует вложенный словарь в одноуровневый ("плоский") словарь.

#     Параметры:
#     - `nested_dict`: Вложенный словарь для преобразования.
#     - `separator`: Строка, используемая для соединения ключей при формировании пути. По умолчанию '_'.

#     Задача:
#     1. Обойти `nested_dict`.
#     2. Для каждого ключа:
#         - Если значение не является словарем, добавить в результирующий словарь пару `{"путь": значение}`, где `путь` - это составной ключ.
#         - Если значение является словарем, рекурсивно вызвать функцию для этого вложенного словаря, передавая текущий путь как префикс для ключей.
#     3. Ключи в плоском словаре формируются путем соединения ключей от корня до значения через `separator`.

#     Пример:
#     flatten_dict({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}, 'f': 4})
#     # a -> 'a': 1
#     # b -> {'c': 2, 'd': {'e': 3}} -> рекурсия с префиксом 'b'
#     #   c -> 'b_c': 2
#     #   d -> {'e': 3} -> рекурсия с префиксом 'b_d'
#     #     e -> 'b_d_e': 3
#     # f -> 'f': 4
#     вернет {'a': 1, 'b_c': 2, 'b_d_e': 3, 'f': 4}

#     flatten_dict({'x': {'y': {'z': 'value'}}, 'w': 1}, separator='.')
#     вернет {'x.y.z': 'value', 'w': 1}

#     flatten_dict({}) вернет {}
#     flatten_dict({'a': {'b': {}}, 'c': 1}) вернет {'c': 1} (пустые словари игнорируются)
#     """
#     # Ваше решение здесь
#     # Подсказка: Используйте рекурсию. Передавайте текущий префикс пути в рекурсивные вызовы.
#     flat_map: Dict[str, Any] = {}
#     # ... ваш код ...
#     return flat_map


from typing import Dict, Any

def flatten_dict(nested_dict: Dict[str, Any], separator: str = '_') -> Dict[str, Any]:
    flat_map: Dict[str, Any] = {}
    
    def helper(current_dict: Dict[str, Any], prefix: str) -> None:
        for key, value in current_dict.items():
            new_key = f"{prefix}{separator}{key}" if prefix else key
            if isinstance(value, dict):
                helper(value, new_key)
            else:
                flat_map[new_key] = value
    
    helper(nested_dict, "")
    return flat_map






# # === Задача 13: Поиск "одиноких" чисел ===
# def find_lonely_numbers(numbers: List[int]) -> List[int]:
#     """
#     Находит "одинокие" числа в списке целых чисел.

#     Определение "одинокого" числа `x`:
#     Число `x` из списка `numbers` считается "одиноким", если одновременно выполняются два условия:
#     1. Число `x` встречается в списке `numbers` ровно один раз.
#     2. Ни число `x-1`, ни число `x+1` НЕ присутствуют в списке `numbers`.

#     Задача:
#     1. Найти все "одинокие" числа в списке `numbers`.
#     2. Вернуть список этих чисел, отсортированный по возрастанию.

#     Подсказка:
#     - Удобно использовать `collections.Counter` для подсчета частоты каждого числа.
#     - Также удобно преобразовать список в множество (`set`) для быстрой проверки наличия `x-1` и `x+1`.

#     Пример:
#     numbers = [10, 6, 5, 8]
#     # Уникальные: {10, 6, 5, 8}. Все встречаются 1 раз.
#     # Проверяем соседей (используем set(numbers) = {10, 6, 5, 8} для проверки):
#     # Для 10: 9 нет, 11 нет. -> Одинок.
#     # Для 6: 5 есть. -> Не одинок.
#     # Для 5: 6 есть. -> Не одинок.
#     # Для 8: 7 нет, 9 нет. -> Одинок.
#     find_lonely_numbers([10, 6, 5, 8]) вернет [8, 10]

#     numbers = [1, 3, 5, 3]
#     # Counter: {1: 1, 3: 2, 5: 1}
#     # Set: {1, 3, 5}
#     # Проверяем числа с частотой 1: 1, 5.
#     # Для 1: 0 нет, 2 нет (в сете {1, 3, 5}). -> Одинок.
#     # Для 5: 4 нет, 6 нет (в сете {1, 3, 5}). -> Одинок.
#     find_lonely_numbers([1, 3, 5, 3]) вернет [1, 5]

#     find_lonely_numbers([1, 1, 2, 3, 3]) вернет [2] (2 встречается 1 раз, 1 нет, 3 есть. А, 1 и 3 ЕСТЬ. Значит 2 не одинок)
#     # Counter: {1: 2, 2: 1, 3: 2}
#     # Set: {1, 2, 3}
#     # Проверяем 2: частота 1. Проверяем соседей: 1 есть, 3 есть. -> Не одинок.
#     # Результат: []
#     find_lonely_numbers([1, 1, 2, 3, 3]) вернет []

#     find_lonely_numbers([100]) вернет [100] (частота 1, 99 нет, 101 нет)
#     find_lonely_numbers([]) вернет []
#     """
#     # Ваше решение здесь
#     pass

from typing import List
from collections import Counter

def find_lonely_numbers(numbers: List[int]) -> List[int]:
    count = Counter(numbers)
    num_set = set(numbers)
    lonely = []
    
    for num in count:
        if count[num] == 1:
            if (num - 1 not in num_set) and (num + 1 not in num_set):
                lonely.append(num)
    
    return sorted(lonely)






# # === Задача 14: RLE Кодирование (Run-Length Encoding) ===
# def run_length_encode(data: str) -> str:
#     """
#     Выполняет Run-Length Encoding (RLE) для строки.

#     Правила кодирования:
#     - Последовательности одинаковых символов заменяются на символ и количество его повторений.
#     - Если символ встречается подряд только один раз, количество 1 НЕ добавляется.
#     - Пустая строка кодируется в пустую строку.

#     Задача:
#     1. Пройти по строке `data`.
#     2. Определить последовательности одинаковых символов.
#     3. Сформировать закодированную строку согласно правилам.
#     4. Вернуть закодированную строку.

#     Пример:
#     run_length_encode("AAABBCDDDDE")
#     # A: 3 раза -> A3
#     # B: 2 раза -> B2
#     # C: 1 раз -> C
#     # D: 4 раза -> D4
#     # E: 1 раз -> E
#     вернет "A3B2CD4E"

#     run_length_encode("XYZ") вернет "XYZ"
#     run_length_encode("KKKLLMNPPP") вернет "K3L2MNP3"
#     run_length_encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW") # Пример с LeetCode
#     # W: 12 -> W12
#     # B: 1 -> B
#     # W: 12 -> W12
#     # B: 3 -> B3
#     # W: 24 -> W24
#     # B: 1 -> B
#     # W: 14 -> W14
#     вернет "W12BW12B3W24BW14"
#     run_length_encode("") вернет ""
#     """
#     # Ваше решение здесь
#     pass

def run_length_encode(data: str) -> str:
    if not data:
        return ""
    encoded = []
    prev_char = data
    count = 1
    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded.append(prev_char)
            if count > 1:
                encoded.append(str(count))
            prev_char = char
            count = 1
    # Добавляем последний символ
    encoded.append(prev_char)
    if count > 1:
        encoded.append(str(count))
    return ''.join(encoded)




# # === Задача 15: RLE Декодирование (Run-Length Decoding) ===
# def run_length_decode(encoded_data: str) -> str:
#     """
#     Декодирует строку, закодированную с помощью RLE (как в Задаче 15).

#     Правила декодирования:
#     - Строка состоит из символов, за которыми МОЖЕТ следовать число (одна или несколько цифр).
#     - Если за символом следует число, оно указывает, сколько раз этот символ должен повториться.
#     - Если за символом НЕ следует число (т.е. следующий символ - не цифра или конец строки), этот символ повторяется один раз.
#     - Пустая строка декодируется в пустую строку.

#     Задача:
#     1. Пройти по закодированной строке `encoded_data`.
#     2. Определить символ и (если есть) число его повторений.
#     3. Построить раскодированную строку.
#     4. Вернуть раскодированную строку.

#     Пример:
#     run_length_decode("A3B2CD4E")
#     # A, цифра 3 -> "AAA"
#     # B, цифра 2 -> "BB"
#     # C, не цифра -> "C"
#     # D, цифра 4 -> "DDDD"
#     # E, конец строки -> "E"
#     вернет "AAABBCDDDDE"

#     run_length_decode("XYZ") вернет "XYZ"
#     run_length_decode("K3L2MNP3") вернет "KKKLLMNPPP"
#     run_length_decode("A12BC")
#     # A, цифра 1, цифра 2 -> число 12 -> "AAAAAAAAAAAA"
#     # B, не цифра -> "B"
#     # C, конец строки -> "C"
#     вернет "AAAAAAAAAAAABC"
#     run_length_decode("") вернет ""
#     """
#     # Ваше решение здесь
#     # Подсказка: Используйте цикл и, возможно, вложенный цикл или isdigit() для чтения числа.
#     pass


def run_length_decode(encoded_data: str) -> str:
    decoded = []
    i = 0
    n = len(encoded_data)
    while i < n:
        char = encoded_data[i]
        j = i + 1
        while j < n and encoded_data[j].isdigit():
            j += 1
        if j == i + 1:
            count = 1
        else:
            count = int(encoded_data[i+1:j])
        decoded.append(char * count)
        i = j
    return ''.join(decoded)





# # === Задача 16: Поиск групп анаграмм ===
# def find_anagram_groups(words: List[str]) -> List[List[str]]:
#     """
#     Группирует слова из списка по анаграммам.

#     Анаграммы — это слова, состоящие из одного и того же набора букв (регистр игнорируется при сравнении, но сохраняется в результате).

#     Параметры:
#     - `words`: Список строк для группировки.

#     Задача:
#     1. Обработать список `words`. Игнорировать пустые строки.
#     2. Сгруппировать слова так, чтобы в каждой группе были анаграммы друг друга.
#        Ключ для группировки: отсортированная строка из букв слова в нижнем регистре.
#     3. Вернуть список списков. Каждый внутренний список представляет собой группу анаграмм.
#     4. Слова внутри каждой группы должны быть отсортированы лексикографически (в алфавитном порядке).
#     5. Порядок самих групп в итоговом списке не важен.

#     Пример:
#     words = ["eat", "tea", "tan", "ate", "nat", "bat", ""]
#     # eat -> aet -> group 'aet': ["eat"]
#     # tea -> aet -> group 'aet': ["eat", "tea"]
#     # tan -> ant -> group 'ant': ["tan"]
#     # ate -> aet -> group 'aet': ["eat", "tea", "ate"]
#     # nat -> ant -> group 'ant': ["tan", "nat"]
#     # bat -> abt -> group 'abt': ["bat"]
#     # "" -> игнорируем
#     # Группы: {'aet': ["eat", "tea", "ate"], 'ant': ["tan", "nat"], 'abt': ["bat"]}
#     # Сортируем слова внутри групп: {'aet': ["ate", "eat", "tea"], 'ant': ["nat", "tan"], 'abt': ["bat"]}
#     find_anagram_groups(words) вернет [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']] (порядок групп может быть другим)

#     words = ["listen", "silent", "enlist", "google", "gogole"]
#     # listen -> eilnst
#     # silent -> eilnst
#     # enlist -> eilnst
#     # google -> eggloo
#     # gogole -> eggloo
#     # Группы: {'eilnst': ["listen", "silent", "enlist"], 'eggloo': ["google", "gogole"]}
#     # Сортируем: {'eilnst': ["enlist", "listen", "silent"], 'eggloo': ["gogole", "google"]}
#     find_anagram_groups(words) вернет [['enlist', 'listen', 'silent'], ['gogole', 'google']]

#     find_anagram_groups(["a"]) вернет [["a"]]
#     find_anagram_groups([]) вернет []
#     """
#     # Ваше решение здесь
#     # Подсказка: Используйте словарь, где ключ - отсортированная версия слова в нижнем регистре, а значение - список оригинальных слов.
#     groups: Dict[str, List[str]] = defaultdict(list)
#     # ... ваш код ...
#     result = [sorted(anagram_list) for anagram_list in groups.values()]
#     return result

from typing import List
from collections import defaultdict

def find_anagram_groups(words: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in words:
        if not word:
            continue
        key = ''.join(sorted(word.lower()))
        groups[key].append(word)
    return [sorted(group) for group in groups.values()]







# # === Задача 17: Скользящее среднее ===
# def moving_average(data: List[Union[int, float]], window_size: int) -> List[Optional[float]]:
#     """
#     Вычисляет скользящее среднее для числового ряда с заданным размером окна.

#     Параметры:
#     - `data`: Список чисел (int или float).
#     - `window_size`: Размер окна (целое положительное число).

#     Задача:
#     1. Вычислить среднее арифметическое для каждого "окна" размером `window_size` в данных `data`.
#     2. Окно "скользит" по данным: первое окно включает элементы с индексами от `0` до `window_size - 1`, второе - от `1` до `window_size`, и так далее, до последнего возможного окна.
#     3. Результат должен быть списком той же длины, что и `data`.
#     4. Для первых `window_size - 1` позиций, для которых невозможно сформировать полное окно, значение среднего должно быть `None`.
#     5. Для всех последующих позиций `i` (начиная с `window_size - 1`), значением является среднее арифметическое среза `data[i - window_size + 1 : i + 1]`.
#     6. Вернуть список со значениями скользящего среднего (тип `float`) или `None`.

#     Ограничения:
#     - Если `window_size <= 0` или `window_size > len(data)`, вернуть список, заполненный `None` той же длины, что и `data`.

#     Пример:
#     moving_average([1.0, 2.0, 3.0, 4.0, 5.0], 3)
#     # Окно 3. Первые 3-1=2 элемента -> None.
#     # i=2: Окно data[0:3] = [1.0, 2.0, 3.0]. Среднее = 6.0 / 3 = 2.0
#     # i=3: Окно data[1:4] = [2.0, 3.0, 4.0]. Среднее = 9.0 / 3 = 3.0
#     # i=4: Окно data[2:5] = [3.0, 4.0, 5.0]. Среднее = 12.0 / 3 = 4.0
#     вернет [None, None, 2.0, 3.0, 4.0]

#     moving_average([1, 1, 1, 10, 1, 1, 1], 4)
#     # Окно 4. Первые 3 элемента -> None.
#     # i=3: data[0:4] = [1, 1, 1, 10]. Среднее = 13 / 4 = 3.25
#     # i=4: data[1:5] = [1, 1, 10, 1]. Среднее = 13 / 4 = 3.25
#     # i=5: data[2:6] = [1, 10, 1, 1]. Среднее = 13 / 4 = 3.25
#     # i=6: data[3:7] = [10, 1, 1, 1]. Среднее = 13 / 4 = 3.25
#     вернет [None, None, None, 3.25, 3.25, 3.25, 3.25]

#     moving_average([1, 2], 3) вернет [None, None]
#     moving_average([1, 2, 3], 1) вернет [1.0, 2.0, 3.0]
#     moving_average([], 3) вернет []
#     """
#     # Ваше решение здесь
#     # Подсказка: Используйте цикл и срезы списка. Не забудьте про обработку краев.
#     pass

from typing import List, Union, Optional

def moving_average(data: List[Union[int, float]], window_size: int) -> List[Optional[float]]:
    if not data:
        return []
    
    n = len(data)
    result = [None] * n
    
    if window_size <= 0 or window_size > n:
        return result
    
    for i in range(window_size - 1, n):
        start = i - window_size + 1
        end = i + 1
        current_window = data[start:end]
        avg = sum(current_window) / window_size
        result[i] = avg
    
    return result





# # === Задача 18: Сумма цифр до одной (Цифровой корень) ===
# def sum_digits_until_single(number: int) -> int:
#     """
#     Рекурсивно складывает цифры неотрицательного целого числа до тех пор,
#     пока результат не станет однозначным числом (от 0 до 9).

#     Параметры:
#     - `number`: Неотрицательное целое число.

#     Задача:
#     1. Если `number` меньше 10, вернуть само `number`.
#     2. Если `number` больше или равно 10:
#         а) Вычислить сумму его цифр.
#         б) Рекурсивно вызвать эту же функцию с полученной суммой.
#     3. Вернуть итоговый однозначный результат.

#     Пример:
#     sum_digits_until_single(16) -> 1 + 6 = 7 (7 < 10, возвращаем 7)
#     sum_digits_until_single(942) -> 9 + 4 + 2 = 15 (15 >= 10) -> sum_digits_until_single(15) -> 1 + 5 = 6 (6 < 10, возвращаем 6)
#     sum_digits_until_single(493193) -> 4+9+3+1+9+3 = 29 -> sum_digits_until_single(29) -> 2+9 = 11 -> sum_digits_until_single(11) -> 1+1 = 2 (2 < 10, возвращаем 2)
#     sum_digits_until_single(5) вернет 5
#     sum_digits_until_single(0) вернет 0

#     Подсказка: Удобно использовать целочисленное деление (`//`) и остаток от деления (`%`) для получения цифр числа. Можно реализовать как с помощью рекурсии, так и с помощью цикла `while`.
#     """
#     # Ваше решение здесь
#     pass

def sum_digits_until_single(number: int) -> int:
    if number < 10:
        return number
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return sum_digits_until_single(total)








# #19 задача 
# # === Задача 19: Поворот квадратной матрицы на месте ===
# def rotate_matrix_inplace(matrix: List[List[int]]) -> None:
#     """
#     Поворачивает квадратную матрицу (список списков целых чисел) на 90 градусов по часовой стрелке.
#     Модификация происходит "на месте" (in-place), то есть исходный объект `matrix` изменяется.

#     Параметры:
#     - `matrix`: Квадратная матрица (список списков), где все вложенные списки имеют одинаковую длину, равную длине внешнего списка.

#     Задача:
#     1. Проверить, является ли матрица квадратной. Если `matrix` пуста или не квадратная (например, `[[1,2],[3]]` или `[[1],[2,3]]`), функция должна завершиться, не изменяя `matrix` и не вызывая ошибок (или можно возбудить `ValueError`, но для простоты лучше просто ничего не делать).
#     2. Если матрица квадратная, повернуть ее на 90 градусов по часовой стрелке, изменяя исходный объект `matrix`.
#     3. Функция ничего не возвращает (`None`).

#     Подсказка:
#     Поворот на 90 градусов по часовой стрелке можно выполнить за два шага:
#     1. Транспонирование матрицы: элемент `matrix[i][j]` меняется местами с `matrix[j][i]`.
#     2. Отражение (reverse) каждой строки матрицы по горизонтали.

#     Пример:
#     matrix = [[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]]
#     rotate_matrix_inplace(matrix)
#     # После транспонирования:
#     # [[1, 4, 7],
#     #  [2, 5, 8],
#     #  [3, 6, 9]]
#     # После отражения строк:
#     # [[7, 4, 1],
#     #  [8, 5, 2],
#     #  [9, 6, 3]]
#     # В итоге `matrix` должна стать [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

#     matrix = [[1, 2],
#               [3, 4]]
#     rotate_matrix_inplace(matrix)
#     # Транспонирование: [[1, 3], [2, 4]]
#     # Отражение строк: [[3, 1], [4, 2]]
#     # В итоге `matrix` должна стать [[3, 1], [4, 2]]

#     matrix = []
#     rotate_matrix_inplace(matrix) # matrix остается []

#     matrix = [[1, 2]]
#     rotate_matrix_inplace(matrix) # matrix остается [[1, 2]] (не квадратная)
#     """
#     # Ваше решение здесь
#     pass


from typing import List

def rotate_matrix_inplace(matrix: List[List[int]]) -> None:
    n = len(matrix)
    # Проверка на квадратность матрицы
    if n == 0:
        return
    for row in matrix:
        if len(row) != n:
            return
    
    # Транспонирование матрицы (меняем элементы местами относительно главной диагонали)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
     # Отражение каждой строки матрицы
    for row in matrix:
        row.reverse()
