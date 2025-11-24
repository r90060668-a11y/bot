import telebot
import os
import random
import time

# Твой токен
BOT_TOKEN = '8224326431:AAFMXZyRPrXXtTV04Y979w61EkvvUb0iYC0'

bot = telebot.TeleBot(BOT_TOKEN)

# Название папки. Она должна лежать РЯДОМ с файлом main.py
GIF_FOLDER = 'gifs'

@bot.message_handler(commands=['куб', 'random'])
def send_random_cube(message):
    try:
        # 1. Проверяем папку
        if not os.path.exists(GIF_FOLDER):
            bot.reply_to(message, f"Ошибка хостинга: не найдена папка '{GIF_FOLDER}'. Проверь GitHub.")
            return

        # 2. Ищем файлы
        files = os.listdir(GIF_FOLDER)
        gifs = [f for f in files if f.endswith('.gif')]

        if not gifs:
            bot.reply_to(message, "Папка с гифками пустая!")
            return

        # 3. Выбираем случайную гифку
        random_gif_name = random.choice(gifs)
        full_path = os.path.join(GIF_FOLDER, random_gif_name)

        # 4. Определяем ID темы (Topic)
        # Бот смотрит, из какой темы пришло сообщение
        topic_id = message.message_thread_id

        # 5. Отправляем
        with open(full_path, 'rb') as animation:
            bot.send_animation(
                chat_id=message.chat.id,
                animation=animation,
                caption="🎲 Кубик брошен!",
                message_thread_id=topic_id  # <-- ВОТ ЭТО заставляет бота писать в нужную тему
            )

    except Exception as e:
        print(f"Ошибка: {e}")
        # Можно не отвечать пользователю ошибкой, чтобы не спамить в чат

print("Бот запущен! Читаю файлы из папки gifs...")
# Бесконечный цикл, чтобы бот не падал при ошибках сети
bot.infinity_polling()