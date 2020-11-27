#как проверить что работатет?

def hello_user():
 while True:
     try:
         ask_user = input('Как дела? ')
         if ask_user == 'Хорошо':
             break
     except KeyboardInterrupt:
         print('Пока')
         break 
if __name__ == "__main__":
    hello_user()