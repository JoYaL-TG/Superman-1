import os
import logging
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import START_MSG, CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION
from utils import Media, get_file_details
from pyrogram.errors import UserNotParticipant
logger = logging.getLogger(__name__)

ADMINS = int(os.environ.get("ADMINS", 1745047302))

PHOTO = [
    "https://telegra.ph/file/9c47001f468a7d8ec3b85.jpg",
    "https://telegra.ph/file/f3fb811e5b75175dbe6a2.jpg",
    "https://telegra.ph/file/011b4087cdb8a0d07644f.jpg",
    "https://telegra.ph/file/2c980314c0cdc1b9e2058.jpg",
    "https://telegra.ph/file/e5f6428c770586043f90d.jpg",
    "https://telegra.ph/file/b305e461514ff4919dcf9.jpg",
    "https://telegra.ph/file/6b07d1e8b92b438de4e12.jpg",
    "https://telegra.ph/file/b3e3417cdc4ec08241434.jpg",
    "https://telegra.ph/file/6af9875a9a3a6c665ac6d.jpg",
    "https://telegra.ph/file/91c596e85fde3e0aae79f.jpg",
    "https://telegra.ph/file/56398140fae3873a56898.jpg",
    "https://telegra.ph/file/dec15fb3bc3f0bc22880a.jpg",
    "https://telegra.ph/file/09ffd32fd9c4984078219.jpg",
    "https://telegra.ph/file/05e04a3b08b30c815a322.jpg",
    "https://telegra.ph/file/f6f599389f7563c8385a6.jpg",
    "https://telegra.ph/file/561fe647eee3a0b1bc3c8.jpg",
    "https://telegra.ph/file/e1efa9565ace2324614ff.jpg",
    "https://telegra.ph/file/b9585457e6ae7cc834ac6.jpg",
    "https://telegra.ph/file/444af460ab9785d52e229.jpg",
    "https://telegra.ph/file/05931986e2599d0ee6815.jpg",
    "https://telegra.ph/file/968cbb7c6b04b776ff26e.jpg",
    "https://telegra.ph/file/40815aab00039f9e5db8b.jpg",
    "https://telegra.ph/file/34bafb8438ad3ef47ae78.jpg",
    "https://telegra.ph/file/cf32ae611eb37862e61d5.jpg",
    "https://telegra.ph/file/f9303edef6f4a16c525ae.jpg",
    "https://telegra.ph/file/03430ea064121f11decb8.jpg",
    "https://telegra.ph/file/e9ddab724643c871d01ad.jpg",
    "https://telegra.ph/file/feb7b9cfa5ec5cfdd5892.jpg",
    "https://telegra.ph/file/15f3895c6b4dee389853d.jpg",
    "https://telegra.ph/file/c62f47b1a990b8c8b184f.jpg",
    "https://telegra.ph/file/f20ae180f58812d1b9c58.jpg",
    "https://telegra.ph/file/4f0b51842b0849c4bd069.jpg",
    "https://telegra.ph/file/f1ec16bc10c73b65764d7.jpg",
    "https://telegra.ph/file/e61e351e3913966cca46c.jpg",
    "https://telegra.ph/file/e5c2931d3f93808c7ab43.jpg",
    "https://telegra.ph/file/0315a61c48943ac0fd2ce.jpg",
    "https://telegra.ph/file/0ebd004f4332bd69bb86d.jpg",
    "https://telegra.ph/file/974e9eb7d1cd032aa75c5.jpg",
    "https://telegra.ph/file/e0ed2d5dfdb8ee0680021.jpg",
    "https://telegra.ph/file/50f89bfd69dc6ceff0cb9.jpg"
]

@Client.on_message(filters.command(['start']))
async def start(client, message):
    usr_cmdall1 = cmd.text
    if usr_cmdall1.startswith("/start subinps"):
        if AUTH_CHANNEL:
            invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
            try:
                user = await bot.get_chat_member(int(AUTH_CHANNEL), cmd.from_user.id)
                if user.status == "kicked":
                    await bot.send_message(
                        chat_id=cmd.from_user.id,
                        text="Sorry Sir, You are Banned to use me.",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                ident, file_id = cmd.text.split("_-_-_-_")
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="**🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭\n\nനിങ്ങൾക് സിനിമകൾ വെന്നോ? അതിനായി അത്യം ങ്ങളുടെ മെയിൻ ചാനലിൽ ജോയിൻ ചെയ്യണം... 😁 \nJoin ചെയ്ത ശേഷം വീണ്ടും ബോട്ട് /start ആക്കൂ.😁 \nഎന്നിട്ട് ഒന്നുടെ TrY Again ബട്ടൺ ക്ലിക്ക് ചെയ്താൽ മൂവി കിട്ടുന്നതാണ്..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔰 ᴊᴏɪɴ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ🔰", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton(" 🔄 Try Again", callback_data=f"checksub#{file_id}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await bot.send_photo(
                    chat_id=cmd.from_user.id,
                    photo=f"{random.choice(PHOTO)}",
                    caption="Something went Wrong.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        try:
            ident, file_id = cmd.text.split("_-_-_-_")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=files.file_size
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = f"{files.file_name}"
                buttons = [
                    [
                        InlineKeyboardButton('Search again 🔎', switch_inline_query_current_chat=''),
                        InlineKeyboardButton('Share Us ♻️', url='https://t.me/share/url?url=https://t.me/joinchat/o0habe6377I5MDhl')
                    ]
                    ]
                await bot.send_cached_media(
                    chat_id=cmd.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")
    elif len(cmd.command) > 1 and cmd.command[1] == 'subscribe':
        invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
        await bot.send_photo(
            chat_id=cmd.from_user.id,
            photo=f"{random.choice(PHOTO)}",
            caption="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link)
                    ]
                ]
            )
        )
    else:
        await cmd.reply_photo(
            photo=f"{random.choice(PHOTO)}",
            caption=START_MSG,
            reply_markup=InlineKeyboardMarkup(
                    [
                    [
                        InlineKeyboardButton("➕ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ➕", url= "https://t.me/Cv_links_project7_bot?startgroup=true")
                    ],
                    [
                        InlineKeyboardButton("🔍 𝖲𝖾𝖺𝗋𝖼𝗁 𝖧𝖾𝗋𝖾", switch_inline_query_current_chat=''),
                        InlineKeyboardButton("𝖦𝗋𝗈𝗎𝗉", url="https://t.me/cinema_beacon_group")
                    ],
                    [
                        InlineKeyboardButton("🕵️‍♂️ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋", url="https://t.me/Joel_TG"),
                        InlineKeyboardButton("😊 𝖠𝖻𝗈𝗎𝗍", callback_data="about")
                    ]    
                ]
            )
         )


@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')
@Client.on_message(filters.command('about'))
async def bot_info(bot, message):
    buttons = [
        [
            InlineKeyboardButton('𝐔𝐏𝐃𝐀𝐓𝐄𝐒 ⚒️', url='https://t.me/cv_updatez'),
            InlineKeyboardButton('𝐉𝐎𝐈𝐍 ♂️', url='https://t.me/cv_group1')
        ]
        ]
    await message.reply(text="<b>𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 👷 : <a href='https://t.me/Cv_groupAdmin2'>𝓳ꪮꫀꪶ ᵇˣ</a>\nLanguage : <code>Python3</code>\nLibrary : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio</a>\nSource Code : <a href='https://github.com/subinps/Media-Search-bot'>🔐</a>\nUpdate Channel : <a href='https://t.me/cv_updatez'>Updatez</a> </b>", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
