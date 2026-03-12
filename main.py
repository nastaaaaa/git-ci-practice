# Система управления заявками на расходы
# gos.obr.budget.control

def validate_kbk(kbk):
    """Проверка КБК (14-20 цифр)"""
    if not kbk.isdigit():
        return False
    if len(kbk) < 14 or len(kbk) > 20:
        return False
    return True


def check_limit(amount, limit):
    """Проверка суммы в пределах лимита"""
    return amount <= limit


def create_request(department, amount, kbk):
    """Создание заявки"""
    return {
        "department": department,
        "amount": amount,
        "kbk": kbk,
        "status": "draft"
    }


def approve_request(request):
    """Согласование заявки"""
    request["status"] = "approved"
    return request


def calculate_total(requests):
    """Подсчёт общей суммы"""
    total = 0
    for req in requests:
        total += req["amount"]
    return total
