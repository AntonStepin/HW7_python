import checks
from calculate import start_modul
from history import history


def controller ():
    user_input = checks.checks_for_user_input("Введите уравнение в одну строку: ")
    user_input = checks.check_for_logic(user_input)
    print(user_input)
    result = start_modul(str(user_input))
    history(user_input, result)
    return result


