from main import (
    validate_kbk,
)


def test_validate_kbk_correct():
    """Правильный КБК"""
    assert validate_kbk("12345678901234") == True


def test_validate_kbk_wrong():
    """Неправильный КБК"""
    assert validate_kbk("abc") == False

