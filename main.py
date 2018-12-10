import bs4
import argparse
import telebot

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type=str)
    args = parser.parse_args()
    bot = telebot.TeleBot(args.token)


    @bot.message_handler(commands=['start', 'go'])
    def start_handler(message):
        bot.send_message(message.chat.id,
                         'Теперь ты настоящий рождественский эльф!\nИмя своего счастливчика узнаешь 11 ' \
                         'декабря в полночь')


    @bot.message_handler(content_types=['text'])
    def text_handler(message):
        text = message.text.lower()
        chat_id = message.chat.id
        if text == "привет":
            bot.send_message(chat_id, 'Привет, я бот - парсер хабра.')
        elif text == "как дела?":
            bot.send_message(chat_id, 'Хорошо, а у тебя?')
        else:
            bot.send_message(chat_id, 'Простите, я вас не понял :(')

    bot.polling()
