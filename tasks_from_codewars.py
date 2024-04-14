import pytest
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    prefix = ""
    for chars in zip(*strs):  # Итерируемся параллельно по символам слов
        if len(set(chars)) == 1:  # Проверяем, все ли символы одинаковые
            prefix += chars[0]
        else:
            break  # Если символы не совпадают, прерываем цикл
    return prefix

@pytest.mark.parametrize("input_strs, expected", [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], "")])
def test_longestCommonPrefix(input_strs, expected):
    assert longestCommonPrefix(input_strs) == expected, f"Должна быть строка {expected}"


def multiply(word, separator, count):
    result = word
    for i in range(count):
        result += separator + word
    return result

def test_multiply():
    assert multiply("Тест", "O", 3) == 'ТестOТестOТестOТест', f"Должны быть строка 'ТестOТестOТестOТест'"
"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in 
descending order. Essentially, rearrange the digits to create the highest possible number.
"""


def descending_order(num):
    str_num = str(num)
    sorted_str = ''
    # Sort the characters of the string in descending order
    for char in sorted(str_num, reverse=True):
        sorted_str += char
    # Convert the sorted string back to an integer
    sorted_num = int(sorted_str)
    return sorted_num

@pytest.mark.parametrize("input_num, expected", [
    (42145, 54421),
    (145263, 654321),
    (123456789, 987654321)
])
def test_descending_order(input_num, expected):
    assert descending_order(input_num) == expected, f"Ожидалось {expected}, но получено {descending_order(input_num)}"
