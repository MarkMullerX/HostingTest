from pyrogram import Client

print("test")

# Create a new Pyrogram client
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot = Client("my_bot", api_id=api_id, api_hash=api_hash)

# Define a handler for receiving messages
@bot.on_message()
def handle_message(client, message):
    message.reply_text("Hello, World!")

# Start the Pyrogram client
bot.run()
