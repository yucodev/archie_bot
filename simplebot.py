import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.send_message(discord.Object(id='453629533569024017'), 'Archie here!')

if __name__ == '__main__':
    import config
    client.run(config.token)
