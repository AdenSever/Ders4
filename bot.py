import discord

from bot_mantik import emoji_olusturucu, gen_pass
# İstekler değişkeni botun yetkilerini saklar
intents = discord.Intents.default()
# Mesaj okuma yetkisini etkinleştirme
intents.message_content = True
# Bir bot oluşturma ve yetkileri aktarma
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} olarak giris yapildi')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$emoji'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('$sifre'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send("Sifreniz: " + gen_pass(8))
client.run("MTQ3NDExMTg3MjI5MzY2NjkxOQ.GwbyIl.ufEktCt4atUXIuy48vGzHe3Hj4gQy4J9juM3_Y")

ayarlar = {
    "on_taki": ">", #ön takı, prefix (maybe it won't work if we call it different here)
    "TOKEN": "MTQ3NDExMTg3MjI5MzY2NjkxOQ.GwbyIl.ufEktCt4atUXIuy48vGzHe3Hj4gQy4J9juM3_Y"
