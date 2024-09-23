from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext,ContextTypes,filters

Token: Final = "7334795697:AAEm1EATo2oxKU_vxCOcwqge91EsybSUalE"
Bot_username: Final = "@Batista123bot"


async def mem(update: Update, context: CallbackContext):
    member=context.bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    await print(f'{member.user.first_name} joined the chat')
     

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Batista Boom💥")
    
async def bomb(update: Update, context: CallbackContext):
    await update.message.reply_text("Batista bOOOOOOOM")


def handle_response(text: str)->str:
    processed: str = text.lower()
    if "hello" in processed:
        return "Hello, I am Batista"
    elif "bye" in processed:
        return "Bye, Wiish to never see you agin, bastista Boom!"
    else:
        return "I am Batista, i must break you"
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str=update.message.chat.type
    text: str = update.message.text
    username: str = update.message.from_user.username
    first_name: str = update.message.from_user.first_name
    last_name: str = update.message.from_user.last_name
    
    print(update.message.from_user)
    #print(f'User:({update.message.from_user}) of type ({message_type}) says: ({text})')
    #print(f'Usercchat id ({update.message.chat.id}) in {message_type}:{text}')
    #use update.message to get whatevery u wnat to get from the message
    if message_type=="group":

        if Bot_username in text:
            if username:
                update.message.reply_text(f" @{username}! You are not worthy of my sheer presence")
            elif first_name and last_name:
                update.message.reply_text(f"@{first_name} {last_name}!You are not worthy of my sheer presence")
            new_text: str = f'@{update.message.from_user.first_name}, You are not worthy of my sheer presence'
            response: str = new_text
        else:
            return
    else:
        response: str = handle_response(text)
    
        
    print(f'Bot says: {response}')
    await update.message.reply_text(response)
    
async def error(update: Update, context: CallbackContext):
    print(f'caused error: {context.error}')
if __name__ == "__main__":
    print("Batista is running")
    app = Application.builder().token(Token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bomb", bomb))
    app.add_handler(CommandHandler("mem",))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error)
    
    
    print("Batista is polling")
    app.run_polling(poll_interval=1)