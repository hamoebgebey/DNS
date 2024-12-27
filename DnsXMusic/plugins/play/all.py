import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

# دالة لإدارة أوامر خاصة بالمستخدمين
@app.on_message(command(["المالك", "صاحب الخرابه", "المنشي"], "") & filters.group)
async def gak_owne(client: Client, message: Message):
    if len(message.command) >= 2:
        return 
    
    chat_id = message.chat.id
    f = "administrators"
    
    async for member in client.iter_chat_members(chat_id, filter=f):
        if member.status == "creator":
            id = member.user.id
            key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
            m = await client.get_chat(id)
            if m.photo:
                photo = await app.download_media(m.photo.big_file_id)
                return await message.reply_photo(
                    photo,
                    caption=f"🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{m.first_name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{m.username}\n🎃 ¦𝙸𝙳 :{m.id}\n💌 ¦𝙱𝙸𝙾 :{m.bio}\n✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :{message.chat.id}",
                    reply_markup=key
                )
            else:
                return await message.reply("• " + member.user.mention)

@app.on_message(command(["اسمي", "اسمي اي"]) & filters.group)
async def get_username(client: Client, message: Message):
    await message.reply_text(f"❤️‍🔥 اسمك »»  {message.from_user.mention()}") 

# قائمة للحفاظ على حالة المنشن
active_mentions = []

@app.on_message(command(["@all", "تاك", "تاك للكل"]) & ~filters.private)
async def mention_all(client: Client, message: Message):
    if message.chat.id in active_mentions:
        return await message.reply_text("التاك قيد التشغيل حالياً،")
        
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status not in ["administrator", "creator"]:
        await message.reply("يجب أن تكون مشرفاً لاستخدام الأمر 🖱️")
        return
    
    await message.reply_text("جاري بدأ المنشن، لإيقاف الأمر اضغط \n /cancel أو اكتب بس منشن")
    i = 0
    txt = ""
    zz = message.text

    # معالجة الصورة إذا كانت موجودة
    if message.photo:
        photo_id = message.photo.file_id
        photo = await client.download_media(photo_id)
        zz = message.caption
    
    # إزالة العبارات الزائدة من النص
    zz = zz.replace("@all", "").replace("تاك", "").replace("نادي الكل", "")
    
    active_mentions.append(message.chat.id)
    
    try:
        async for user in client.iter_chat_members(message.chat.id):
            if message.chat.id not in active_mentions:
                return
            if not user.user.is_deleted:
                i += 1
                txt += f" {user.user.mention} ،"
                
                if i == 5:
                    if not message.photo:
                        await client.send_message(message.chat.id, f"{zz}\n{txt}")
                    else:
                        await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
                    i = 0
                    txt = ""
                    await asyncio.sleep(2)
    except FloodWait as e:
        await asyncio.sleep(e.x)
   
    active_mentions.remove(message.chat.id)

@app.on_message(command(["بس المنشن", "/cancel", "بس منشن"]))
async def stop_mention(client: Client, message: Message):
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status not in ["administrator", "creator"]:
        await message.reply("**يجب أن تكون مشرفاً لاستخدام الأمر 🖱️")
        return
    
    if message.chat.id not in active_mentions:
        await message.reply("المنشن متوقف بالفعل")
        return 

    active_mentions.remove(message.chat.id)
    await message.reply("تم إيقاف المنشن بنجاح ✅")
