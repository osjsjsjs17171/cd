#tg = @SUKUNAAxSOLO
#TG = @SUKUNAAxSOLO
import random

# Initialize your bot with the token
bot = telebot.TeleBot("7292476162:AAHB4JaVg3V2LL85EaUZnv6XaMvyKba22qU")

emojis = ["👍", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🎉", "🤩", "🙏", 
          "👌", "😍", "❤‍🔥", "🌚", "💯", "🤣", "💔", "😐", "🇮🇳", "😈", "😴", 
          "😭", "🤓", "😇", "🤝", "🤗", "🫡", "🤪", "🗿", "🆒", "💘", "😘", 
          "😎", "🇳🇵"]
          

@bot.message_handler(func=lambda message: True)
def react_to_message(message):
    try:
        chat_id = message.chat.id
        message_id = message.message_id
        random_emoji = random.choice(emojis)
        
        bot.set_message_reaction(
            chat_id=chat_id,
            message_id=message_id,
            reaction=[telebot.types.ReactionTypeEmoji(random_emoji)],
            is_big=True
        )
    except Exception as e:
        print(f"Error setting reaction: {e}")
print("Bot is running...")
# Start the bot
bot.polling() #24/7


#by @SUKUNAAxSOLO



JUST NORMALLY YOU NEEDED VPS OR RDP FOR FOR HOSTING THO ISME FREE WALE K LOYE BHI BATAO RAA HU


FREE USERS = 