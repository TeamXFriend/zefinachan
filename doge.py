from telethon import TelegramClient, events
from os import environ as e

bot = TelegramClient(None, e.get("API_KEY"), e.get("API_HASH"))
bot.start(bot_token=e.get("TOKEN"))

a, b, c, d = "[0-9]{16}[|][0-9]{1,2}[|][0-9]{2,4}[|][0-9]{3}", "[0-9]{15}[|][0-9]{1,2}[|][0-9]{2,4}[|][0-9]{4}", "[0-9]{16}", "[0-9]{15}"
   

@bot.on(events.NewMessage(pattern="^/start$"))
async def _s(e):
 await e.reply("This CC Scraper has been started successfully | Developed by Doge.")

@bot.on(events.NewMessage(func=lamda e: e.text, chats=[e.get("CHAT_ID_FORWARD")]))
async def _xtract(e):
 try:
  try:
   x = re.findall(c, e.text)
   x = str(x[0][0:1])
  except:
   x = re.findall(d, e.text)
   x = str(x[0][0:1])
  
   
   
 
