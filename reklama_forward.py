import telebot
from telebot.types import Message

# Replace with your bot token
BOT_TOKEN = "5890470756:AAGDFzpvGNZrVAZb8Q3U0m5MDhiM32U2u2g"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=["text", "photo", "video", "audio", "document", "sticker", "voice", "location"])
def handle_message(message: Message):
    try:
        if message.forward_date:
            bot.forward_message(message.chat.id, message.chat.id, message.message_id)
        else:
            if message.content_type == "text":
                bot.send_message(message.chat.id, message.text)
            elif message.content_type in ["photo", "video", "audio", "document", "sticker", "voice", "location"]:
                bot.send_message(message.chat.id, "This is a non-forwarded non-text message.")
    except Exception as e:
        bot.send_message(message.chat.id, f"An error occurred: {e}")
print("Bot is running...")
bot.polling(non_stop=True)
