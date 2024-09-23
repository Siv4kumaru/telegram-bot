from telegram import Update, ChatMemberUpdated
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

DATABASE_URL = 'sqlite:///example.db'
engine = create_engine(DATABASE_URL)


async def users():
    Session = sessionmaker(bind=engine)
    session = Session()
    for user in session.query(User).all():
        print(user.userid)
    print(f"********")

    session.close()

async def main():
    await users()

if __name__ == "__main__":
    asyncio.run(main())

    #await context.bot.ban_chat_member(chat_id=-1002338444521, user_id=1048272535)