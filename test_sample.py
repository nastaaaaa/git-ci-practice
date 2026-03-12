from main import (
    validate_kbk,
    check_limit,
    create_request,
    approve_request,
    calculate_total
)


def test_validate_kbk_correct():
    """Правильный КБК"""
    assert validate_kbk("12345678901234") == True


def test_validate_kbk_wrong():
    """Неправильный КБК"""
    assert validate_kbk("abc") == False


def test_check_limit_ok():
    """В пределах лимита"""
    assert check_limit(50000, 100000) == True


def test_check_limit_exceed():
    """Превышение лимита"""
    assert check_limit(150000, 100000) == False


def test_create_request():
    """Создание заявки"""
    req = create_request("Бухгалтерия", 50000, "12345678901234")
    assert req["status"] == "draft"
    assert req["amount"] == 50000


def test_approve_request():
    """Согласование заявки"""
    req = create_request("IT", 30000, "12345678901234")
    approved = approve_request(req)
    assert approved["status"] == "approved"


def test_calculate_total():
    """Подсчёт суммы"""
    requests = [
        {"amount": 50000},
        {"amount": 30000},
        {"amount": 20000}
    ]
    assert calculate_total(requests) == 100000
