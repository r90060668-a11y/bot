import telebotimport telebot
import random
import os

# Твой токен
BOT_TOKEN = '8224326431:AAFMXZyRPrXXtTV04Y979w61EkvvUb0iYC0'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['куб'])
def roll_dice(message):
    try:
        # 1. Генерируем случайное число от 1 до 20 (D20)
        result = random.randint(1, 20)
        
        # 2. Форматируем красивый ответ со смайликами
        response_text = f"🎲 Бросок D20! \n\n🔥 Выпало число: **{result}**!"
        
        # 3. Получаем ID темы (ветки)
        # Если это обычный чат, topic_id будет None, и это сработает
        topic_id = message.message_thread_id
        
        # 4. Отправляем сообщение
        bot.send_message(
            chat_id=message.chat.id, 
            text=response_text,
            parse_mode='Markdown', # Включаем жирный шрифт для числа
            message_thread_id=topic_id # Это гарантирует работу в темах
        )
        
    except Exception as e:
        print(f"Ошибка: {e}")

print("Бот запущен! (Режим: Текст, D20)")
bot.infinity_polling()