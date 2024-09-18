from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext,ContextTypes,filters

Token: Final = "7334795697:AAEm1EATo2oxKU_vxCOcwqge91EsybSUalE"
Bot_username: Final = "@Batista123bot"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Batista Boom💥")
    
async def bomb(update: Update, context: CallbackContext):
    await update.message.reply_text("Batista bOOOOOOOM")

async def kick(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if the user has permission to kick members
    admin_status = await update.effective_chat.get_member(update.effective_user.id)
    
    if admin_status.status not in ['administrator', 'creator']:
        await update.message.reply_text("You don't have permission to kick members.")
        return

    
    print(update.effective_chat)
    if context.args:
        username = context.args[0].lstrip('@')  # Remove the '@' if present

        
        try:
            # Try to get the member by username
            member_status = await update.effective_chat.get_member(username)
            
            print(member_status)
            user_id = member_status.user.id
            print(user_id)
            print(update.effective_chat)
            
            # Kick the member
            await update.effective_chat.kick_member(user_id)
            await update.message.reply_text(f"Kicked {username} from the group.")
        
        except Exception as e:
            await update.message.reply_text(f"Failed to kick {username}: {str(e)}")
    else:
        await update.message.reply_text("Please provide a username to kick.")

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
    app.add_handler(CommandHandler("kick", kick))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error)
    
    
    print("Batista is polling")
    app.run_polling(poll_interval=1)