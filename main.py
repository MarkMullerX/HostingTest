from pyrogram import Client
import os

print("it's 2 version")

# Create a new Pyrogram client
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot = Client("my_bot", api_id=api_id, api_hash=api_hash)

# Define a handler for receiving messages
@bot.on_message()
async def handle_message(client, message):
    # await bot.send_message(message.from_user.username)
    message.reply_text("Hello, " + message.from_user.username)

# Start the Pyrogram client
bot.run()
