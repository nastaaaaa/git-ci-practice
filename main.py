# Система управления заявками на расходы
# gos.obr.budget.control

def validate_kbk(kbk):
    """Проверка КБК (14-20 цифр)"""
    if not kbk.isdigit():
        return False
    
