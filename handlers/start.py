# Copyright (C) 2021 By PratheekProjects
from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋 𝙃𝙀𝙇𝙇𝙊 𝙏𝙃𝙀𝙍𝙀 {message.from_user.mention}</b> ❗ 𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙈𝙔 𝘽𝙊𝙏💞

𝙏𝙃𝙄𝙎 𝙄𝙎 𝘼 𝘽𝙊𝙏 𝘿𝙀𝙎𝙄𝙂𝙉𝙀𝘿 𝙏𝙊 𝙋𝙇𝘼𝙔 𝙈𝙐𝙎𝙄𝘾 𝙄𝙉 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋𝙎!

𝙏𝙃𝙄𝙎 𝙄𝙎 𝘼 𝙋𝙐𝘽𝙇𝙄𝘾 𝙋𝙍𝙊𝙅𝙀𝘾𝙏 𝙊𝙁 [shyxd](https://t.me/I_follow_no_one) & [Killer](https://t.me/Shykiller)....𝙈𝘼𝘿𝙀 𝙒𝙄𝙏𝙃 ❤️.

𝙃𝙀𝙍𝙀 𝘼𝙍𝙀 𝙎𝙊𝙈𝙀 𝘾𝙈𝘿𝙎 𝙏𝙊 𝙐𝙎𝙀 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏 """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "💕 Sᴜᴍᴍᴏɴ Mᴇ​ 💕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "Hᴏᴡ Tᴏ Usᴇ Mᴇ​ ❓", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "📘 Cᴏᴍᴍᴀɴᴅs", callback_data="cbcmds")
                ],[
                    InlineKeyboardButton(
                        "​​Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ 👥", url=f"https://t.me/{GROUP_SUPPORT}")
                ],[
                ],[
                    InlineKeyboardButton(
                        "🥀 Oᴡɴᴇʀ 1", url=f"https://t.me/I_follow_no_one"
                    ),
                    InlineKeyboardButton(
                        "✨ Oᴡɴᴇʀ 2", url=f"https://t.me/Shykiller")
                ],[
                    InlineKeyboardButton(
                        "🤖 𝑴𝒂𝒌𝒆 𝒀𝒐𝒖𝒓 𝑶𝒘𝒏 𝑩𝒐𝒕 🤖", url="https://github.com/devellyf/ShyboyXD"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("👥 Gʀᴏᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"👋 𝙃𝙀𝙇𝙇𝙊 {message.from_user.mention}, 𝙄'𝙢 {BOT_NAME}\n\n😎 𝙔𝙀𝘼 𝙄𝙆, 𝘽𝙊𝙏 𝙄𝙎 𝙒𝙊𝙍𝙆𝙄𝙉𝙂 𝙁𝙄𝙉𝙀\n🥀 𝙊𝙒𝙉𝙀𝙍: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n⏳ 𝙑𝙀𝙍𝙎𝙄𝙊𝙉: `v{__version__}`\n🤖 𝙋𝙔𝙍𝙊 𝙑𝙀𝙍𝙎𝙄𝙊𝙉: `{pyrover}`\n⚡ 𝙋𝙔𝙏𝙃𝙊𝙉 𝙑𝙀𝙍𝙎𝙄𝙊𝙉: `{__python_version__}`\n🥱 𝙐𝙋𝙏𝙄𝙈𝙀: `{uptime}`\n\n**Thanks For Using Me ❤️**"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""👋 **Hello** {message.from_user.mention()} !

» **Press The Button Below To Read The Explanation And See The List Of Available Commands!**

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="❓ Basic Guide", callback_data="cbguide")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"🥀 `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 Bot Status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
