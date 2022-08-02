
from tabnanny import check


def checks_for_user_input(messege_for_user1: str):
    check = 0
    while check == 0:
        user_input = input(f"{messege_for_user1}")
        for char in user_input :
            if not char.isdigit() and not char in ["+","-","*","/","(",")"]:
                check = 0
                break
            elif char.isdigit() or char in ["+","-","*","/","(",")"]:
                check = 1
    return user_input

def check_for_logic(user_input:str):
    numbers = 0
    chars = 0
    minus = 0
    exponent = 0
    temp_exponent="" # требуется для определения возведения в степень
    temp_number = "" # набирает символы знака
    double_char = 0 #ловит дубли знаков кроме *
    for char in user_input:
        if char.isdigit():
            temp_number += char
            if double_char>0: double_char-=1
            if len(temp_exponent) == 2:
                exponent +=1
                temp_exponent=""
                double_char -=1
        elif char in ["+", "*", "/"]:
            chars+=1
            if temp_number:
                numbers+=1
                temp_number=""
            if char =="*":
                temp_exponent+=char
        elif char == "-":
            minus+=1
            if temp_number:
                numbers+=1
                temp_number=""
        if char in ["+", "*", "/", "-"]:
                double_char+=1
                try:
                    if user_input[user_input.index(char)+1] == "(":
                        double_char-=1
                except:
                    double_char*=1
    if temp_number: numbers+=1
    if chars > numbers and numbers <= (chars - minus - exponent) or double_char !=0:
        return checks_for_user_input("Некорректное уравнение. Введите еще раз: ")
    return user_input
  
    
        
    

