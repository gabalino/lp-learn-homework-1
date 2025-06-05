"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from os import getenv
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    print('Вызван /start')
    user_name = update._effective_user.first_name
    update.message.reply_text(f'Здравствуй, {user_name}!')


def get_planet(update, context):
    result = ''
    text = update.message.text
    params = text.split()
    if len(params) > 1:
        planet_name = params[1].strip().capitalize()
        if hasattr(ephem, planet_name):
            planet_class = getattr(ephem, planet_name)
            planet = planet_class()
            planet.compute()
            constellation = ephem.constellation(planet)
            result = f'Сегодня {planet_name} находится в созвездии {constellation}'
        else:
            result = 'Неизвестная планета'
    else:
        result = 'Введите /planet <название планеты>'
    update.message.reply_text(result)
    return result


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(token=getenv("TG_BOT_TOKEN"), use_context=True)
    if mybot:
        dp = mybot.dispatcher
        dp.add_handler(CommandHandler("start", greet_user))
        dp.add_handler(CommandHandler("planet", get_planet))
        dp.add_handler(MessageHandler(Filters.text, talk_to_me))

        mybot.start_polling()
        mybot.idle()
    else:
        print('Переменая TG_BOT_TOKEN не найдена!')

if __name__ == "__main__":
    main()
