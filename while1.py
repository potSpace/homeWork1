# 8 и 9 строку скопировал из репозитария, иначе не запускалась функция

def hello_user():
     while True:
         ask_user = input('Как дела? ')
         if ask_user == 'Хорошо':
             break
if __name__ == "__main__":
    hello_user()