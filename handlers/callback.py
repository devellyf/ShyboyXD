# (C) 2021 All Rights Reserved PratheekProjects

from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>👋 𝙃𝙀𝙇𝙇𝙊 𝙏𝙃𝙀𝙍𝙀 {message.from_user.mention}</b> ❗ 𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙈𝙔 𝘽𝙊𝙏💞

𝙏𝙃𝙄𝙎 𝙄𝙎 𝘼 𝘽𝙊𝙏 𝘿𝙀𝙎𝙄𝙂𝙉𝙀𝘿 𝙏𝙊 𝙋𝙇𝘼𝙔 𝙈𝙐𝙎𝙄𝘾 𝙄𝙉 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋𝙎!

𝙏𝙃𝙄𝙎 𝙄𝙎 𝘼 𝙋𝙐𝘽𝙇𝙄𝘾 𝙋𝙍𝙊𝙅𝙀𝘾𝙏 𝙊𝙁 [𝙋𝙍𝘼𝙏𝙃𝙀𝙀𝙆](https://t.me/pratheek06) & [𝘼𝘼𝙆𝘼𝙎𝙃](https://t.me/akshhhxx)....𝙈𝘼𝘿𝙀 𝙒𝙄𝙏𝙃 ❤️.

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
                        "🥀 Oᴡɴᴇʀ 1", url=f"https://t.me/pratheek06"
                    ),
                    InlineKeyboardButton(
                        "✨ Oᴡɴᴇʀ 2", url=f"https://t.me/akshhhxx")
                ],[
                    InlineKeyboardButton(
                        "🤖 𝑴𝒂𝒌𝒆 𝒀𝒐𝒖𝒓 𝑶𝒘𝒏 𝑩𝒐𝒕 🤖", url="https://github.com/PratheekXD/PratheekxAakash"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **Press The Button Below To Read The Explanation And See The List Of Available Commands!**

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Basic Cmd", callback_data="cbbasic"),
                    InlineKeyboardButton("Advanced Cmd", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("Sudo Cmd", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("Owner Cmd", callback_data="cbowner")],
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Here Is The Basic Commands**

🎧 [ GROUP VC CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

🎧 [ CHANNEL VC CMD ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🔴 **Here Is The Advanced Commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Here Is The Admin Commands**

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🔴 **Here Is The Sudo Commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Here Is The Owner Commands**

/stats - show the bot statistic
/broadcast (reply to message) - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 Note: All Commands Owned By This Bot Can Be Executed By The Owner Of The Bot Without Any Exceptions.

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **HOW TO USE THIS BOT:** ❔

1.) **First, Add Me To Your Group.**
2.) **Then Promote Me As Admin And Give All Permissions Except Anonymous Admin.**
3.) **Add @{ASSISTANT_NAME} To Your Group Or Type /join to invite.**
4.) **Turn On The Voice Chat First Before Start To Play Music.**

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📘 Command List", callback_data="cbhelp")],
                [InlineKeyboardButton("❌ Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "** Here Is The Control Menu Of Bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ Pause", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ Resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ Skip", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ Stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("⛔ Anti Cmds", callback_data="cbdelcmds")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📗 **This Is The Feature Information:**
        
**❗ Feature:** !Delete Every Commands Sent By Users To Avoid Spam In Groups!

❔ Usage:**

 1️⃣ To Turn On Feature:
     » type `/delcmd on`
    
 2️⃣ To Turn Off Feature:
     » type `/delcmd off`
      
🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋 **Hello** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **Press The Button Below To Read The Explanation And See The List Of Available Commands !**

🦄 __Powered By {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Basic Cmd", callback_data="cblocal"),
                    InlineKeyboardButton("Advanced Cmd", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="cblamp"),
                    InlineKeyboardButton("Sudo Cmd", callback_data="cblab"),
                ],
                [InlineKeyboardButton("Owner Cmd", callback_data="cbmoon")],
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **HOW TO USE THIS BOT:** ❔

1.) **First, Add Me To Your Group.**
2.) **Then Promote Me As Admin And Give All Permissions Except Anonymous Admin.**
3.) **Add @{ASSISTANT_NAME} To Your Group Or Type /join To Invite Her.**
4.) **Turn On The Voice Chat First Before Start To Play Music.**

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🔴 **Here Is The Basic Commands**

🎧 [ GROUP VC CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

🎧 [ CHANNEL VC CMD ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Here Is The Advanced Commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🔴 **Here Is The Admin Commands**

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Here Is The Sudo Commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🔴 **Here Is The Owner Commands**

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 Note: All Commands Owned By This Bot Can Be Executed By The Owner Of The Bot Without Any Exceptions.

🦄 __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )
