from telegram import Update, ChatMemberUpdated
from telegram.ext import Application ,ChatMemberHandler,CommandHandler, MessageHandler, CallbackContext,ContextTypes,filters
from datetime import datetime,timedelta


# Replace 'YOUR_TOKEN' with your bot token from BotFather
TOKEN = '7334795697:AAEm1EATo2oxKU_vxCOcwqge91EsybSUalE'

# Replace 'YOUR_CHAT_ID' with the ID of the group/channel you want to invite users to
CHAT_ID = -1002338444521

async def kickdaily(update:Update,context:CallbackContext):
    await context.bot.kick_chat_member(chat_id=-1002338444521, user_id=1048272535)
    print(f"Kicked ")

kickdaily(Update,CallbackContext)