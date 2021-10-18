import os
from pyrogram import Client ,filters
from helper.database import getid
ADMINS = int(os.environ.get("ADMINS", 1890385137))

@Client.on_message(filters.command(['broadcast']) & filters.user(ADMINS))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"**🔖 Broadcast Started** \n\n**Sending Message To {tot} Users 😃**")
   for id in ids:
     try:
      await message.reply_to_message.copy(id)
     except:
      pass
