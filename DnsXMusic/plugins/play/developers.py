import asyncio
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import app

@app.on_message(
    filters.command(["السورس", "ياسورس", "يا سورس", "سورس"]) & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/d0a2e1e5a0dd7ddbd6512.mp4",
        caption="""◉ 𝙽𝙰𝙼𝙴 : ❪[Sᴏᴜʀᴄᴇ ғʀ𝟹ᴏɴ](https://t.me/sorcefraon)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @PV_FR3ON ❫
◉ 𝙸𝙳      : ❪ 5490392130 ❫
◉ 𝙱𝙸𝙾    : ❪ صلي علي الحبيب محمد ✨♥ ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("᳒ᴅᴇᴠ ҒᎡ3ΌΝ", url="https://t.me/PV_FR3ON"),
                ],
                [
                    InlineKeyboardButton("☭ ՏΌႮᎡᏟᎬ  ҒᎡ3ΌΝ ☭", url="https://t.me/sorcefraon"),
                ],
            ]
        ),
    )
