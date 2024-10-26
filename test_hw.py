# Проверьте, что функция правильно считает гласные в строке, содержащей только гласные.
# Проверьте, что функция возвращает 0 для строки, не содержащей гласных.
# Проверьте, что функция правильно считает гласные в смешанных строках (включая прописные и строчные буквы).

import pytest
from hw import count_vowels


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("аоеёооо", 7),
        ("грмвх", 0),
        ("Ехали цыгане тёмным лесом!", 10),

    ],
)
def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected
