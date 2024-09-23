from flask import Flask, redirect, url_for, render_template
import asyncio
from telegram import Bot
from datetime import timedelta
from telegram import Update
from telegram.ext import Application ,ChatMemberHandler,CommandHandler, MessageHandler, CallbackContext,ContextTypes,filters
app = Flask(__name__)



# Replace 'YOUR_TOKEN' with your bot token from BotFather
TOKEN = '7334795697:AAEm1EATo2oxKU_vxCOcwqge91EsybSUalE'

# Replace 'YOUR_CHAT_ID' with the ID of the group/channel you want to invite users to
CHAT_ID = -1002338444521

# Initialize the bot
bot = Bot(token=TOKEN)

async def create_invite_link():
    expire_time = timedelta(seconds=10)

    # Create the invite link with expiration and member limit
    link= await bot.create_chat_invite_link(
        chat_id=-1002338444521, 
        expire_date=None,  # Set None for unlimited or a specific expiration timestamp
        member_limit=1  # Limit to only 1 user
    )
    print(f"Here is your one-member join link (expires in 10 seconds): {link.invite_link}") 
    return link.invite_link
# Create the invite link

@app.route('/')
def index():
    # Serve the HTML with the button
    return render_template('index.html')

@app.route('/get-invite')
def get_invite():
    # Run the async function and get the invite link
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    invite_link = loop.run_until_complete(create_invite_link())
    return redirect(invite_link)


if __name__ == '__main__':
    app.run(debug=True)

# Output the join link

# Main async function to run the coroutine
async def main():
    await create_invite_link()


