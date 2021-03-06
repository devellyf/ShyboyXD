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
        f"""<b>π πππππ πππππ {message.from_user.mention}</b> β ππππΎπππ ππ ππ π½πππ

ππππ ππ πΌ π½ππ πΏπππππππΏ ππ πππΌπ πππππΎ ππ ππππ ππππππ!

ππππ ππ πΌ πππ½πππΎ ππππππΎπ ππ [shyxd](https://t.me/I_follow_no_one) & [Killer](https://t.me/Shykiller)....ππΌπΏπ ππππ β€οΈ.

ππππ πΌππ ππππ πΎππΏπ ππ πππ ππππ π½ππ """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "π Sα΄α΄α΄α΄Ι΄ Mα΄β π", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "Hα΄α΄‘ Tα΄ Usα΄ Mα΄β β", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "π Cα΄α΄α΄α΄Ι΄α΄s", callback_data="cbcmds")
                ],[
                    InlineKeyboardButton(
                        "ββUα΄α΄α΄α΄α΄s CΚα΄Ι΄Ι΄α΄Κ π£", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "Sα΄α΄α΄α΄Κα΄ CΚα΄α΄ π₯", url=f"https://t.me/{GROUP_SUPPORT}")
                ],[
                ],[
                    InlineKeyboardButton(
                        "π₯ Oα΄‘Ι΄α΄Κ 1", url=f"https://t.me/I_follow_no_one"
                    ),
                    InlineKeyboardButton(
                        "β¨ Oα΄‘Ι΄α΄Κ 2", url=f"https://t.me/Shykiller")
                ],[
                    InlineKeyboardButton(
                        "π€ π΄πππ ππππ πΆππ π©ππ π€", url="https://github.com/devellyf/ShyboyXD"
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
                InlineKeyboardButton("π₯ GΚα΄α΄α΄", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "π£ CΚα΄Ι΄Ι΄α΄Κ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"π πππππ {message.from_user.mention}, π'π’ {BOT_NAME}\n\nπ πππΌ ππ, π½ππ ππ πππππππ ππππ\nπ₯ πππππ: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\nβ³ πππππππ: `v{__version__}`\nπ€ ππππ πππππππ: `{pyrover}`\nβ‘ ππππππ πππππππ: `{__python_version__}`\nπ₯± ππππππ: `{uptime}`\n\n**Thanks For Using Me β€οΈ**"

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
        f"""π **Hello** {message.from_user.mention()} !

Β» **Press The Button Below To Read The Explanation And See The List Of Available Commands!**

π¦ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="β Basic Guide", callback_data="cbguide")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("π `PONG!!`\n" f"π₯ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "π€ Bot Status:\n"
        f"β’ **uptime:** `{uptime}`\n"
        f"β’ **start time:** `{START_TIME_ISO}`"
    )
