import argparse
import telebot
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type=str)
    parser.add_argument('--admin', type=int)
    args = parser.parse_args()
    bot = telebot.TeleBot(args.token)

    id_map = {}
    id_match = {}

    answers = ['Свято наближається', 'Обзываться нехорошо', 'Олени уже летят', 'Запахло мандаринками']


    @bot.message_handler(commands=['start', 'go'])
    def start_handler(message):
        bot.send_message(message.chat.id,
                         'Теперь ты настоящий рождественский эльф!\nИмя своего счастливчика узнаешь 11 ' \
                         'декабря')
        user_info = message.chat.first_name
        if message.chat.last_name is not None:
            user_info += " " + message.chat.last_name
        if message.chat.username is not None:
            user_info += " (@" + message.chat.username + ")"
        id_map[message.chat.id] = user_info


    @bot.message_handler(commands=['shuffle'])
    def shuffle_handler(message):
        if message.chat.id == args.admin:
            shuffled = list(id_map.keys())
            random.shuffle(shuffled)
            for i, id in enumerate(shuffled):
                id_match[id] = shuffled[(i + 1) % len(shuffled)]
        else:
            bot.send_message(message.chat.id, "Зачем ломаешь???")


    @bot.message_handler(commands=['share'])
    def share_handler(message):
        if message.chat.id == args.admin:
            for key, value in id_match.items():
                bot.send_message(key, 'Санта определил твою цель: ' + id_map[value])
        else:
            try:
                bot.send_message(message.chat.id, 'Санта определил твою цель: ' + id_map[id_match[message.chat.id]])
            except KeyError:
                bot.send_message(message.chat.id, 'Санта еще думает')


    @bot.message_handler(content_types=['text'])
    def text_handler(message):
        bot.send_message(message.chat.id, random.choice(answers))


    bot.polling()
