import discord
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as: {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Testing Phase."))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    print('Author ID: {0.author.id} Channel Name/ID: {0.channel} / {0.channel.id} : Message from {0.author}: {0.content}'.format(msg))
token = input('Token: ')
client.run(token)