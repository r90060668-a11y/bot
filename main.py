import telebot
import random
import os

# Твой токен (8224326431:AAFMXZyRPrXXtTV04Y979w61EkvvUb0iYC0)
# P.S. Если бот начнет себя странно вести, не забудь отозвать токен и создать новый!
BOT_TOKEN = '8224326431:AAFMXZyRPrXXtTV04Y979w61EkvvUb0iYC0'

bot = telebot.TeleBot(BOT_TOKEN)

# --- СПИСОК ВСЕХ ТВОИХ 20 ID ---
CUBES = [
    # Первая десятка ID
    'CgACAgIAAxkBAAEFBHxpIWhikhT6s9Z2tMohqjJACywbYQACxIkAAk-PEEkLswxM8m4MMDYE', 
    'CgACAgIAAxkBAAEFBI9pIWocxlU48wjnVAZM2V7G4NF_aAAC4IkAAk-PEEm4LEZq3pmj1zYE', 
    'CgACAgIAAxkBAAEFBJVpIWq-m4XDNceNQvZ238Whatvr3wAC7okAAk-PEEnPwCGceprWUDYE',  
    'CgACAgIAAxkBAAEFBJ1pIWuHcrgHUJqoGyhJ-7olhoj6ZAACB4oAAk-PEEmdHaFkelb8PTYE', 
    'CgACAgIAAxkBAAEFBKVpIWxTDstR_3zQzYrTLkH7sA7a8AACFIoAAk-PEEkyJ_SK1SuUmjYE', 
    'CgACAgIAAxkBAAEFBK5pIW0nfaUH_IoHRFNpPFKuoKdLTwACIIoAAk-PEEmzIzR2ybGTajYE', 
    'CgACAgIAAxkBAAEFBLVpIW3fAn8JZhyRrSAY4PumWw6JDQACMooAAk-PEEkeeG8ytmRUpDYE',  
    'CgACAgIAAxkBAAEFBLZpIW6OxJmaz9QfKgs2S3ecAz9ZbwACP4oAAk-PEEm9l9yVDwyP5DYE', 
    'CgACAgIAAxkBAAEFBL1pIW84HL3UEkbUaBTVT1HG2LBxFwACRYoAAk-PEElGv5HdFHt6OjYE', 
    'CgACAgIAAxkBAAEFBMRpIW_PROsLHIyEFdpB0-RXk__ktgACUooAAk-PEEmxiUy-WbjIeDYE', 
    # Вторая десятка ID
    'CgACAgIAAxkBAAEFF3BpI04Y-cOGFxC3qTKm_f9blAHYWgAC-4MAAlMVGUkky6JS-UolSjYE', 
    'CgACAgIAAxkBAAEFF3FpI04ZniEwqUdip5cyvtgJypGksAAC_IMAAlMVGUnJDqEIQGPXUzYE', 
    'CgACAgIAAxkBAAEFF3hpI04gBOYgiOxoAkA0SDSxus6aUgAC5IgAArfjIUkGQ9E5Mg9rrjYE', 
    'CgACAgIAAxkBAAEFF3JpI04a2KZ_gjCV7O2487AEUz4q_QAC_oMAAlMVGUkPUxzAGAtz8jYE', 
    'CgACAgIAAxkBAAEFF3hpI04gBOYgiOxoAkA0SDSxus6aUgAC5IgAArfjIUkGQ9E5Mg9rrjYE', # Дубликат, но оставим для ровного счета
    'CgACAgIAAxkBAAEFF3NpI04a9fotFma6_fK5OPsCfB7awQAC_4MAAlMVGUkGbav_Zb0F5DYE', 
    'CgACAgIAAxkBAAEFF3RpI04b4E7klD_onip4dkV7_k82vwACAoQAAlMVGUlKlnJLV6TvLDYE', 
    'CgACAgIAAxkBAAEFF3VpI04bpfopUZqtwM_KTKcUbsHR3AACA4QAAlMVGUkxRDtVvv9azzYE', 
    'CgACAgIAAxkBAAEFF3ZpI04cu9BGSSvRxtYESNk63FluLgACBIQAAlMVGUmvWmt8FWuA-jYE', 
    'CgACAgIAAxkBAAEFF3dpI04ddSzoHNeLZJJWYJFGAZeY0gACBYQAAlMVGUlj4EUQZk7vRjYE' 
]

# Список красивых фраз со смайликами
PHRASES = [
    "🎲 Бросок судьбы! ✨",
    "✨ Смотрим, что выпало!",
    "🔥 Твой результат на кону!",
    "🍀 Удача на твоей стороне!",
    "🔮 Звезды сказали...",
    "💫 Время решать!",
    "🎯 Кубик брошен!"
]

@bot.message_handler(commands=['куб', 'random'])
def send_random_cube(message):
    try:
        # Выбираем случайный кубик и случайную фразу
        random_gif = random.choice(CUBES)
        random_caption = random.choice(PHRASES)
        
        # Получаем ID темы (Topic) из сообщения. Это важно для работы в ветках!
        topic_id = message.message_thread_id
        
        # Отправляем гифку
        bot.send_animation(
            chat_id=message.chat.id, 
            animation=random_gif, 
            caption=random_caption,
            message_thread_id=topic_id # <-- Это гарантирует работу в темах
        )
        
    except Exception as e:
        # В случае ошибки выводим ее в консоль Render
        print(f"Ошибка при обработке команды: {e}")

print("Бот запущен! Готов работать в темах с ID-файлами.")
bot.infinity_polling()