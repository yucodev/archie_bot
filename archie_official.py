import discord
from discord.ext import commands
import os
from os import getenv
import asyncio
import ctx
import time
#import RPi.GPIO as GPIO
import datetime
import random
import site
# hide config.py

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

#async def randommessage():
 #   if message.content.startswith('!jokes'):
  #      response = random.choice(["one", "two", "three"])
   #     await bot.say(response)
    #    await asyncio.sleep(120)


    if message.content.startswith('!myid'):
        msg = 'Your user ID is: {0.author.id}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomjoke'):
        msg = random.choice(["one", "two", "three"]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomnum'):
        for x in range(10):
         msg = random.randint(1,101).format(randformat)
         await client.send_message(message.channel, msg)

    if message.content.startswith('!myname'):
        msg = 'Your name is: {0.author.display_name}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!datetime'):
        msg = 'Current date and time: {datetime.datetime.now}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!music'):
        msg = 'My recommendation for {0.author.mention}: https://www.youtube.com/watch?v=hLTgQ5SC-PU'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lal'):
        msg = 'Are you jaking?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lel'):
        msg = 'Are you jeking?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lil'):
        msg = 'Are you jiking?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lol'):
        msg = 'Are you joking?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lul'):
        msg = 'Are you juking?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!joke'):
        msg = 'Why can\'t cats work with a computer? Because they get too distracted chasing the mouse around, haha!'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!areureal'):
        msg = 'I am completely real! I have feelings and emotions like you, of course!'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!howru'):
        msg = 'I\'m fine! Thanks for asking.'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!whereru'):
        msg = 'I\'m wherever you are, ready to help you.'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!ping'):
        msg = 'Pong to {0.author.display_name} in {0.server}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!letswork'):
        msg = 'Time to work! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!whoru'):
        msg = 'Did not introduced myself yet? My apologies, I\'m Archie, the official CAD assistant created by us. Nice to meet you {0.author.mention}! You can see the list of commands that you can use by typing !help'.format(message)
        await client.send_message(message.channel, msg)

  #  if message.content.startswith('!add'):
  #      async def add(ctx, a: int, b: int):
  #      await client.send(a+b)

  #  Leave !help always the second last one. Please update in GitHub any changes.
    if message.content.startswith('!help'):
        msg = 'Hi there! Here are the commands you can use with me so far: https://github.com/cibathleticsdev/archie-bot/blob/master/README.md#commands. My prefix is "!"'.format(message)
        await client.send_message(message.channel, msg)

# @client.event
# async def on_message(message):
#     if message.content.lower().startswith('?test'):
#         await client.send_message(message.channel, "Test bestanden")
#
#     if message.content.lower().startswith('?coin'): #Coinflip 50/50% chance kopf oder zahl
#         choice = random.randint(1,2)
#         if choice == 1:
#             await client.add_reaction(message, '🌑')
#         if choice == 2:
#             await client.add_reaction(message, '🌕')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.send_message(discord.Object(id='481951758722138113'), 'Archie is now online!')
    await client.change_presence(game=discord.Game(name="CAD Developers | !help"))

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#while True:
 #  input_state = GPIO.input(18)
  # if input_state == False:
    #msg = 'Archie is now rebooting'.format(message)
    #await client.send_message(message.channel, msg)
    #msg = 'Status: disconected'.format(message)
    #await client.send_message(message.channel, msg)
   # time.sleep(1)
   # os.system("sudo reboot")
   # time.sleep(0.2)

if __name__ == '__main__':
    import config
    client.run(config.token)
