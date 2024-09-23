from telegram import Update, ChatMemberUpdated
from telegram.ext import Application ,ChatMemberHandler,CommandHandler, MessageHandler, CallbackContext,ContextTypes,filters
from typing import Optional, Tuple
from datetime import datetime,timedelta,timezone
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.exc import IntegrityError
from db import User


DATABASE_URL = 'sqlite:///example.db'
engine = create_engine(DATABASE_URL)


# async def start(update: Update, context: CallbackContext):

#     await context.bot.send_message(chat_id=update.effective_user.id, text="Welcome to the group!")

# async def user_created(upup : ChatMemberUpdated, context: ContextTypes.DEFAULT_TYPE):
#     print(upup)


async def start(update:Update, context: CallbackContext):
    print(update.message.chat.id)
    expire_time = timedelta(seconds=10)
    expire_date = datetime.now() + expire_time
    
    # Create the invite link with expiration and member limit
    link= await context.bot.create_chat_invite_link(
        chat_id=-1002338444521, 
        expire_date=expire_date,  # Set None for unlimited or a specific expiration timestamp
        member_limit=1  # Limit to only 1 user
    )
    print(f"Here is your one-member join link (expires in 10 seconds): {link.invite_link}") 

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
        def get_time_in_ist(utctime: datetime) -> datetime:
        
            
            # IST is UTC + 5 hours 30 minutes
            ist_offset = timedelta(hours=5, minutes=30)
            
            # Return IST time as a datetime object
            return utctime + ist_offset
        date_joined = get_time_in_ist(date_joined)


        # Print user information
        print(f"UserName: {username}, FirstName: {first_name}, LastName: {last_name}, Date: {date_joined}")
        existing_user = session.query(User).filter(User.userid == userId).first()

        if existing_user:
            print(f"{userId} already exists in the database. Updating user information.")
            existing_user.username = username
            existing_user.first_name = first_name
            existing_user.last_name = last_name
            existing_user.date = date_joined
        else:
            new_user = User(
                userid=userId,
                username=username,
                first_name=first_name,
                last_name=last_name,
                date=date_joined
            )

            session.add(new_user)
        try:
            session.commit()
            print(f"Inserted {userId} into the database.")
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
    await context.bot.ban_chat_member(chat_id=-1002338444521, user_id=1048272535)
    await context.bot.unban_chat_member(chat_id=-1002338444521, user_id=1048272535)
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
