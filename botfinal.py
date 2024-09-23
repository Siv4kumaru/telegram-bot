from telegram import Update, ChatMemberUpdated
from telegram.ext import Application ,ChatMemberHandler,CommandHandler, MessageHandler, CallbackContext,ContextTypes,filters
from typing import Optional, Tuple
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.exc import IntegrityError
from db import User

# async def start(update: Update, context: CallbackContext):

#     await context.bot.send_message(chat_id=update.effective_user.id, text="Welcome to the group!")

# async def user_created(upup : ChatMemberUpdated, context: ContextTypes.DEFAULT_TYPE):
#     print(upup)
DATABASE_URL = 'sqlite:///example.db'
engine = create_engine(DATABASE_URL)


async def start(update:ChatMemberUpdated, context: CallbackContext):
    print(update.message.date)

async def startu(newmem: ChatMemberUpdated, context: ContextTypes.DEFAULT_TYPE) -> None:
    new_members = newmem
    user=new_members.message.new_chat_members

    Session = sessionmaker(bind=engine)
    session = Session()

        # Create a new User instance

    for i in range(len(user)):

        userId = user[i].id
        username = user[i].username
        first_name = user[i].first_name
        last_name = user[i].last_name
        date_joined = new_members.message.date


        # Print user information
        print(f"UserName: {username}, FirstName: {first_name}, LastName: {last_name}, Date: {date_joined}")
        
        new_user = User(
            userid=userId,
            username=username,
            first_name=first_name,
            last_name=last_name,
            date=date_joined
        )
        # if session.filter(User.userid==userId):
        #     print("User already exists")
        session.add(new_user)
        try:
            session.commit()
            print(f"Inserted {username} into the database.")
        except IntegrityError:
            session.rollback()
            print(f"User {username} already exists in the database.")
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

    session.close()
    

    # print(new_members.message.new_chat_members.User.last_name)
    # print(new_members.message.new_chat_members.User.username)   
    # print(new_members.message.date)


# async def getmembers(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     for i in range(await context.bot.get_chat_member_count( -1002338444521)):
#         print(await context.bot.get_chat_member(-1002338444521, i))
    




async def kick(update: Update, context: CallbackContext):
    await context.bot.ban_chat_member(chat_id=-1002338444521, user_id=1265311417)
    print(f"Kicked ")

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7334795697:AAEm1EATo2oxKU_vxCOcwqge91EsybSUalE").build()

    # Keep track of which chats the bot is in
    application.add_handler(CommandHandler("start", start))

    
    application.add_handler(CommandHandler("kick", kick))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, startu))

    application.run_polling(poll_interval=1)

if __name__ == "__main__":
    main()
