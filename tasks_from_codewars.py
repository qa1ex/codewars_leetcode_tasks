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


"""
Create a function that always returns True/true for every item in a given list.
However, if an element is the word 'flick', switch to always returning the opposite boolean value.
"""
def flick_switch(lst):
    bool_lst = []
    bool_flag = True  # Initial boolean value
    for item in lst:
        if item == 'flick':
            bool_flag = not bool_flag  # Toggle the boolean flag
        bool_lst.append(bool_flag)  # Append the current boolean value
    return bool_lst

@pytest.mark.parametrize("input_list, expected", [
    (['codewars', 'flick', 'code', 'wars'], [True, False, False, False]),
    (['flick', 'chocolate', 'adventure', 'sunshine'], [False, False, False, False]),
    (['bicycle', 'jarmony', 'flick', 'sheep', 'flick'], [True, True, False, False, True]),
])
def test_flick_switch(input_list, expected):
    assert flick_switch(input_list) == expected, f"Ожидалось: {expected}, но получено: {flick_switch(input_list)}"