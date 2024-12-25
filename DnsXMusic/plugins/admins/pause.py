#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from DnsXMusic import app
from DnsXMusic.core.call import Dns
from DnsXMusic.utils.database import is_music_playing, music_off
from DnsXMusic.utils.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(filters.command(["resume"]) | filters.command(["الغاء الكتم","توقف"],prefixes= ["/", "!","","#"]) & filters.group)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Dns.pause_stream(chat_id)
    await message.reply_text(_["admin_2"].format(message.from_user.mention))
