import os
import telebot
import requests
from dotenv import load_dotenv

load_dotenv()
# Replace YOUR_API_TOKEN with your actual Telegram API token
bot = telebot.TeleBot(os.getenv("telegramAPItoken"))

# Define the standard answers
answers = {
    'Hello': 'Hi there!',
    'hello': 'Hi there!',
    'How are you?': 'I am doing well, thanks for asking.'
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, I'm the ESD Tour Bot! Enter your Booking ID to get your tour information")

# Define the message handler function
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    chat_id = message.chat.id

    try:
        booking_id = int(text)
    except ValueError:
        bot.reply_to(message, "Invalid booking ID. Please enter a valid integer ID.")
        return
    
    payload = {'chat_id': chat_id, 'bid': booking_id}
    requests.post('http://127.0.0.1:5010/receive_chat_id', json=payload)
    
    if text in answers:
        bot.reply_to(message, answers[text])
    
# Start the bot
bot.polling()