import discord

client = discord.Client()

@client.event
async def on_message():
    print('Archie here!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


if __name__ == '__main__':
    import config
    client.run(config.token)
