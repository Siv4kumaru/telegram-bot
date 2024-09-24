from telegram import Update, ChatMemberUpdated,Bot
from telegram.ext import Application ,ChatMemberHandler,CommandHandler, MessageHandler, CallbackContext,ContextTypes,filters
from datetime import datetime,timedelta
from db import User
import asyncio
from flask import Flask
from flask_sqlalchemy import SQLAlchemy,session
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker,declarative_base




# Replace 'YOUR_TOKEN' with your bot token from BotFather
TOKEN = '7334795697:AAEm1EATo2oxKU_vxCOcwqge91EsybSUalE'

# Replace 'YOUR_CHAT_ID' with the ID of the group/channel you want to invite users to
CHAT_ID = -1002338444521
bot=Bot(token=TOKEN)
DATABASE_URL = 'sqlite:///example.db'
engine = create_engine(DATABASE_URL)


async def users():
    Session = sessionmaker(bind=engine)
    session = Session()
    for user in session.query(User).all():
        userdate= user.date
        diff=datetime.now()-userdate
        print(f"********")
        print(f"{user.userid} {user.first_name}")
        print(f"days in: {diff.days}")
        if diff.days>=1 and user.active==1:
            print(f"User {user.first_name} is in more than day")
            try:
                # await bot.ban_chat_member(chat_id=-1002338444521, user_id=user.userid)
                # await bot.unban_chat_member(chat_id=-1002338444521, user_id=user.userid)
                user.active=0 
                session.add(user)
                print(f"banned {user.userid} ,{user.first_name} ")
                print(f"********")
            except Exception as e:
                session.rollback()
                print(f"User {user.userid},{user.first_name} is not banned,error:{e}")
                print(f"********")
        elif user.active==0:
            print(f"User {user.userid} is already banned")
            print(f"********")      
        else:
            print(f"User {user.userid} is not banned")
            print(f"********")
    session.commit()
    session.close()

async def main():
    await users()

if __name__ == "__main__":
    asyncio.run(main())

