import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from DnsXMusic import app 

@app.on_message(filters.voice_chat_started)
async def stcall(client: Client, message: Message): 
    start_text = "🎉 الكول اتفتح 🙈"
    await message.reply_text(start_text)

@app.on_message(filters.voice_chat_ended)
async def encall(client: Client, message: Message): 
    end_text = "👋 قفلت الكول ليه، ربنا يسمحك 😔😭"
    await message.reply_text(end_text)

@app.on_message(filters.voice_chat_members_invited)
async def zoharyy(client: Client, message: Message): 
    inviter = message.from_user.mention
    invited_users = message.voice_chat_members_invited.users

    if invited_users:
        user_mentions = " ".join([f"[{user.first_name}](tg://user?id={user.id})" for user in invited_users])
        text = f"-{inviter} قام بدعوة: {user_mentions}"
    else:
        text = f"-{inviter} قام بدعوة أعضاء إلى الكول."

    try:
        await message.reply(text)
    except Exception as e:
        print(f"Error replying to message: {e}")
