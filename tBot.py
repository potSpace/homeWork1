import logging, ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет пользователь! \nНа данный момент я могу сказать тебе в каком созвездии находится планета')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater('1433375511:AAFwZCR9ug0UhdW7jA4IkUqoqVTsoKyQNy4', use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot starting')
    mybot.start_polling()
    mybot.idle()


current_datetime = datetime.now()

planets = {
    'Mercury': ephem.Mercury(current_datetime),
    'Venus': ephem.Venus(current_datetime),
    'Mars': ephem.Mars(current_datetime),
    'Jupiter': ephem.Jupiter(current_datetime),
    'Saturn': ephem.Saturn(current_datetime),
    'Uranus': ephem.Uranus(current_datetime),
    'Neptune': ephem.Neptune(current_datetime),
    'Меркурий': ephem.Mercury(current_datetime),
    'Венера': ephem.Venus(current_datetime),
    'Марс': ephem.Mars(current_datetime),
    'Юпитер': ephem.Jupiter(current_datetime),
    'Сатурн': ephem.Saturn(current_datetime),
    'Уран': ephem.Uranus(current_datetime),
    'Нептун': ephem.Neptune(current_datetime)
    
}

def planet(update, context):
    user_text = update.message.text
    search_name = update.message.text.split(' ')
    planet_name = search_name[1].capitalize()
    print(planet_name)
    
    if planet_name in planets:
        x = planets.get(planet_name)
        constellation = ephem.constellation(x)
        print(constellation)
        update.message.reply_text(f'Планета {planet_name} находится в созвездии {constellation}')
    
    elif planet_name in ['Earht' , 'Земля']:
        update.message.reply_text(f'{planet_name} не может входить в созвездие')
        
    elif planet_name in ['Pluto', 'Плутон']:
        update.message.reply_text(f'{planet_name} не является планетой')

    else:
        update.message.reply_text('Введи планету из солнечной системы')




main()