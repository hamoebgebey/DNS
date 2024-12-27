from pyrogram import filters, Client
from DnsXMusic import app
import asyncio
from DnsXMusic.core.call import Yukki
from DnsXMusic.utils.database import *
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError, AlreadyJoinedError

@app.on_message(filters.regex("^مين في الكول$"))
async def strcall(client: Client, message):
    assistant = await group_assistant(Yukki, message.chat.id)
    try:
        # هنا، نحذف الاتصال الصوتي
        # يمكن إزالة أي كود متعلق بالاتصال

        text = "🙃🔔 الارانب المتواجدين في الكول:\n\n"
        participants = await assistant.get_participants(message.chat.id)
        for k, participant in enumerate(participants, start=1):
            user = await client.get_users(participant.user_id)
            mut = "يتحدث 🗣" if not participant.muted else "ساكت 🔕"
            text += f"{k}➤ {user.mention} ➤ {mut}\n"
        
        text += f"\nعددهم: {len(participants)}\n✔️"    
        await message.reply(f"{text}")

    except NoActiveGroupCall:
        await message.reply("ارنب الكول مش مفتوح اصلااا\n🤔")
    except TelegramServerError:
        await message.reply("ارسل الامر تاني في مشكله في سيرفر التلجرام\n🤔")
    except AlreadyJoinedError:
        text = "🙃🔔 الارانب المتواجدين في الكول:\n\n"
        participants = await assistant.get_participants(message.chat.id)
        
        for k, participant in enumerate(participants, start=1):
            user = await client.get_users(participant.user_id)
            mut = "يتحدث 🗣" if not participant.muted else "ساكت 🔕"
            text += f"{k}➤ {user.mention} ➤ {mut}\n"
        
        text += f"\nعددهم: {len(participants)}\n✔️"    
        await message.reply(f"{text}")
