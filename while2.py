fhrases = {
    'Как дела?': 'Хорошо!',
    'Что делаешь?': 'Программирую',
    'Получается?': 'Конечно!',
    'Удачи': 'И тебе'
}


def ask_user(fhrases_dict):
    while True:
        ask_user = input('Задай мне вопрос: ')
        if ask_user in fhrases:
          print(fhrases[ask_user])

if __name__ == "__main__":
    ask_user(fhrases)