from datetime import datetime
from time import time

def history (user_input:str, result):
    date = datetime.now()
    with open ("history.txt", "a") as history:
        history.writelines(f"{date}: | {user_input} = {result} |\n")

