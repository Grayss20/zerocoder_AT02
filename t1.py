import pytest
from m1 import is_palindrome


def test_is_palindrome_true():
    assert is_palindrome("racecar") == True


def test_is_palindrome_false():
    assert is_palindrome("hello") == False


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("racecar", True),
        ("hello", False),
        ("", True),
        ("level", True),
        ("aa", True),
        ("ab", False),
        ("aba", True),
        ("abba", True),
        ("abcba", True),
        ("abccba", True),
    ]
)
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected
