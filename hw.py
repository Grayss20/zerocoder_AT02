# Напишите функцию, которая считает количество гласных в строке, и создайте тесты для этой функции.

def count_vowels(text: str) -> int:
    vowels = 'ёуеэоаыяию'
    count = 0
    for letter in text.lower():
        if letter in vowels:
            count += 1
    return count
