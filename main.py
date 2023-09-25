import discord
from sifre import gen_pass

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Vay be bağlandın! {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("OOO! Paşam gelmiş, hoş gelmiş.")

    elif message.content.startswith('$gülegüle'):
        await message.channel.send("\\U0001f642")

    elif message.content.startswith('$sifre'):
        await message.channel.send(gen_pass(85))

    else:
        await message.channel.send(message.content)

client.run("MTE1MzM3MTIxNTYzMzg0MjMxOQ.GgsAld.NW77DcE4o4MdMKGWrbCVMMeQV-LscFPMeeIRJI")