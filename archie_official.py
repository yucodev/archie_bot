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
import sys
# hide config.py
sys.path.insert(0, '/home/dietpi/discord')

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #if ('archie') in message.content:
     #   msg = 'What do you want?'.format(message)
     #   await client.send_message(message.channel, msg)

    if message.content.startswith('!myid'):
        msg = 'Your user ID is: {0.author.id}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!joke'):
        a = 'Can a kangaroo jump higher than a house?\nOf course, a house doesn’t jump at all.'
        b = 'Anton, do you think I’m a bad mother?\nMy name is Paul.'
        c = 'Why can\'t cats work with a computer?\nBecause they get too distracted chasing the mouse around, haha!'
        d = 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.'
        msg = random.choice([a, b, c, d]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!flipcoin'):
        a = 'Heads :fire:'
        b = 'Tails :snowflake:'
        msg = random.choice([a, b]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!5random'):
        msg = random.randint(1, int(5))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomnum'):
        msg = random.randint(1, int(10))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!100random'):
        msg = random.randint(1, int(100))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!1000random'):
        msg = random.randint(1, int(1000))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lottery'):
        msg = random.randint(0, int(99999))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!myname'):
        msg = 'Your name is: {0.author.display_name}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!datetime'):
        msg = 'Current date and time: ' + str(datetime.datetime.now())
        await client.send_message(message.channel, msg)

    if ('hello archie') in message.content:
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'How are you today?'.format(message)
        await client.send_message(message.channel, msg)

    if ('good night archie') in message.content:
        msg = 'Good night {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'see you tomorrow'.format(message)
        await client.send_message(message.channel, msg)

    if ('fine thanks archie') in message.content:
        msg = 'Cool, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(2)
        msg = 'I\'m fine too :laughing:'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(3)
        msg = 'Can you change my profile picture? I don\'t like it very much'.format(message)
        await client.send_message(message.channel, msg)

    if ('not fine archie') in message.content:
        msg = 'well, ok {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!music'):
        a = 'https://youtu.be/hLTgQ5SC-PU' # Do you know the way
        b = 'https://youtu.be/kJQP7kiw5Fk' # Luis Fonsi - Despacito
        c = 'https://youtu.be/FTQbiNvZqaY' # Toto - Africa
        d = 'https://youtu.be/tK601BjwRbk' # Million Dollar Weekends - Addicted To Your Love
        # ISSUE with {0.author.mention}.
        msg = 'My recommendation for {0.author.mention}: '.format(message) + random.choice([a, b, c, d])
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

  # do not remove '!update' !!
    if message.content.startswith('!update'):
        msg = 'Wait a few seconds...'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'Updating Archie'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'Archie is now offline!'.format(message)
        await client.send_message(message.channel, msg)
        os.system("python3 ~/discord/update.py")
        time.sleep(5)
        exit()

  #  if message.content.startswith('!add'):
  #      async def add(ctx, a: int, b: int):
  #      await client.send(a+b)

  #  Leave !help always the last one. Please update in GitHub any changes.
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
