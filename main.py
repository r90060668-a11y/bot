import telebot
import random
import os

# --- ТОКЕН БОТА ---
BOT_TOKEN = '8224326431:AAFMXZyRPrXXtTV04Y979w61EkvvUb0iYC0'
bot = telebot.TeleBot(BOT_TOKEN)

# --- ОБРАБОТЧИК КОМАНДЫ /куб ---
@bot.message_handler(commands=['куб'])
def roll_dice(message):
    # Генерируем случайное число от 1 до 20
    result = random.randint(1, 20)
    
    # Форматируем красивый текст (жирный шрифт и смайлики)
    response_text = f"🎲 Бросок D20! \n\n🔥 Выпало число: **{result}**!"
    
    # Получаем ID темы (ветки). Это ключевой момент для работы в темах.
    topic_id = message.message_thread_id
    
    # Отправляем сообщение
    bot.send_message(
        chat_id=message.chat.id, 
        text=response_text,
        parse_mode='Markdown', 
        message_thread_id=topic_id # Передает ID темы
    )

# --- ЗАПУСК БОТА ---
print("Бот запущен! Ожидание команды /куб...")
bot.infinity_polling()