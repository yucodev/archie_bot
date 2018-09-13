#please run this script only with Python3

import discord #pip install discord.py / pip3 install discord.py
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import requests
import os
from os import getenv
import asyncio #pip install asyncio / pip3 install asyncio
import ctx
from weather import Weather, Unit #pip install weather-api / pip3 install weather-api
import time #pip install time / pip3 install time
from datetime import datetime
import random
import site
import sys #pip install sys / pip3 install sys
# hide config.py
sys.path.insert(0, '/home/dietpi/discord')

client = discord.Client()

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await client.send_message(member, 'Welcome to this server, {0.author.mention}! I\'m Archie, the official CADevelopers discord bot, nice to meet you! Please, read our #rules and #about in our discord server https://discord.gg/TS583KK to be updated. Have fun and RESPECT!! :grinning: :desktop:')
    await client.send_message(message.channel, 'Welcome to this server, {0.author.mention}! I\'m Archie, the official CADevelopers discord bot, nice to meet you! Please, read our #rules and #about in our discord server https://discord.gg/TS583KK to be updated. Have fun and RESPECT!! :grinning: :desktop:')
    print("Sent message to " + member.name)


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!weatherforecast'):
        weather = Weather(unit=Unit.CELSIUS)
        city = message.content.split(" ")
        CITYUP = str(" ".join(city[1:])).upper()
        location = weather.lookup_by_location(" ".join(city[1:]))
        forecasts = location.forecast
        await client.send_message(message.author, '_**WEATHER FORECAST %s **_' % (CITYUP))
        msg = 'Forecast sent per DM'
        await client.send_message(message.channel, msg)
        time.sleep(1)
        for forecast in forecasts:
            await client.send_message(message.author, '**On ' + forecast.date + '**')
            await client.send_message(message.author, ' :low_brightness: ' + forecast.text)
            await client.send_message(message.author, ' :small_orange_diamond: Max temp. ' + forecast.high)
            await client.send_message(message.author, ' :small_blue_diamond: Min temp. ' + forecast.low)
            await client.send_message(message.author, ' --------------------- ')  

    if message.content.startswith('!weathertoday'):
        weather = Weather(unit=Unit.CELSIUS)
        city = message.content.split(" ")
        CITYUP = str(" ".join(city[1:])).upper()
        location = weather.lookup_by_location(" ".join(city[1:]))
        forecasts = location.forecast
        msg1 = 'Forecast for {0.author.mention} in ' + CITYUP
        msg = msg1.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        for forecast in forecasts:
            await client.send_message(message.channel, '**On ' + forecast.date + '**')
            await client.send_message(message.channel, ' :low_brightness: ' + forecast.text)
            await client.send_message(message.channel, ' :small_orange_diamond: Max temp. ' + forecast.high)
            await client.send_message(message.channel, ' :small_blue_diamond: Min temp. ' + forecast.low)
            if ('today') in message.content:
                break
            await client.send_message(message.channel, ' --------------------- ')

    if message.content.startswith('!echo'):
        echo = message.content.split(" ")
        await client.send_message(message.channel, '%s' % (" ".join(echo[1:])))

    #if message.content('!weather'):
     #   await client.send_message(message.channel, 'Chose a city and rewrite it including it: !weather city')

    if message.content.startswith('!sendme'):
        sendme = message.content.split(" ")
        await client.send_message(message.author, '%s' % (" ".join(sendme[1:])))

    #if message.content.startswith('!randommember'):
      #  a = '<@427204692234469387>' # @pupspulver05
       # b = '<@334252448036159488>' # @viktaur
      #  c = '<@367958242980003850>' # @manersat
     #   d = '<@340143776557170690>' # @TheAlx1Boy
    #    e = '<@443842331926331392>' # @turivm
      #  f = '<@334994066372820994>' # @Varito2003
   #     msg = random.choice([a, b, c, d]).format(message)
    #    await client.send_message(message.channel, msg)

    if message.content.startswith('!myid'):
        msg = 'Your user ID is: {0.author.id}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('archie'):
        msg = 'What do you want?'.format(message)
        await client.send_message(message.channel, msg)

    # if message.content.startswith('!joke'):
        # a = 'Can a kangaroo jump higher than a house?\nOf course, a house doesn’t jump at all.'
        # b = 'Anton, do you think I’m a bad mother?\nMy name is Paul.'
        # c = 'Why can\'t cats work with a computer?\nBecause they get too distracted chasing the mouse around, haha!'
        # d = 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.'
        # e = 'What do Italian ghosts have for dinner? Spook-hetti!'
        # msg = random.choice([a, b, c, d]).format(message)
        # await client.send_message(message.channel, msg)

    if message.content.startswith('!joke'):
        a = 'Can a kangaroo jump higher than a house?'
        b = 'Anton, do you think I’m a bad mother?'
        c = 'Why can\'t cats work with a computer?'
        d = 'My dog used to chase people on a bike a lot.'
        e = 'What do Italian ghosts have for dinner?'
        letter_choice = random.choice([a, b, c, d, e])
        msgQ = letter_choice.format(message)
        await client.send_message(message.channel, msgQ)
        time.sleep(3)
        a = 'Of course, a house doesn’t jump at all.'
        b = 'My name is Paul'
        c = 'Because they get too distracted chasing the mouse around, haha!'
        d = 'It got so bad, finally I had to take his bike away.'
        e = 'Spook-hetti!'
        msgA = letter_choice.format(message)
        await client.send_message(message.channel, msgA)

    if message.content.startswith('!quiz'):
        split = message.content.split(" ")
        response = ("yes".join(split[1:]))
        msg = 'Can cats fly? (yes/no)'
        await client.send_message(message.channel, msg)
        #elif response == 'no'
         #   await client.send_message(message.channel, 'Noooooo')
          #  time.sleep(2)
           # await client.send_message(message.channel, 'But they should... :heart_eyes_cat:')
        if split == response:
             print("lol")
             await client.send_message(message.channel, 'Of course they can!')
             time.sleep(2)
             await client.send_message(message.channel, 'Well, no.')

    #if message.content.startswith('!join'):
        #channel = client.get_channel('485833536889290752')
        #await client.join_voice_channel(channel)

    #elif message.content.startswith('!play'):
        #player = vlc.MediaPlayer("/home/dietpi/bigcalm.mp3")
        #player.play()

    if message.content.startswith('!rolldice'):
        a = ':one:'
        b = ':two:'
        c = ':three:'
        d = ':four:'
        e = ':five:'
        f = ':six:'
        msg = random.choice([a, b, c, d, e, f]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomcolor'):
        a = 'red'
        b = 'blue'
        c = 'green'
        d = 'lime'
        e = 'white'
        f = 'black'
        g = 'yellow'
        h = 'gray'
        i = 'orange'
        msg = random.choice([a, b, c, d, e, f, g, h, i]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomsport'):
        a = 'tennis'
        b = 'basketball'
        c = 'golf'
        d = 'athletics'
        e = 'rugby'
        f = 'baseball'
        g = 'canoeing'
        h = 'badminton'
        i = 'ski'
        msg = random.choice([a, b, c, d, e, f, g, h, i]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomcarbrand'):
        a = 'alfa romeo'
        b = 'audi'
        c = 'bmw'
        d = 'aston martin'
        e = 'bentley'
        f = 'bugatti'
        g = 'chevrolet'
        h = 'seat'
        i = 'ferrari'
        j = 'lamboghini'
        k = 'maserati'
        l = 'jaguar'
        m = 'mercedes'
        n = 'mclaren'
        o = 'porsche'
        p = 'tesla'
        q = 'volkswagen'
        r = 'opel'
        s = 'mazda'
        msg = random.choice([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomclothe'):
        a = 'nike'
        b = 'adidas'
        c = 'levis'
        d = 'holister'
        e = 'abercrombie'
        f = 'hunder armour'
        g = 'gucci'
        h = 'lacoste'
        i = 'vans'
        j = 'supreme'
        k = 'asics'
        l = 'pepe jeans'
        m = 'kappa'
        n = 'kelme'
        o = 'calvin klein'
        p = 'quicksilver'
        q = 'diesel'
        r = 'puma'
        s = 'rip curl'
        t = 'joma'
        u = 'fila'
        msg = random.choice([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!botinfo'):
        msg = 'Archie Bot (version 1.0.2) ©2018\nA funny Discord Bot with a lot of features! For more info visit our website http://cadevelopers.ml/ or type !help to see the commands you can use with me so far.'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!credits'):
        msg = 'PyJavaPulver (https://github.com/PyJavaPulver)\nviktaur (https://github.com/viktaur)\nTheAlx1Boy (https://github.com/TheAlx1Boy)\nvaritogolf (https://github.com/varitogolf)\nCybernetic Athletics Developers ©2018 (http://cadevelopers.ml/, https://github.com/cibathleticsdev)\nAll rights reserved.'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!flipcoin'):
        a = 'Heads :fire:'
        b = 'Tails :snowflake:'
        msg = random.choice([a, b]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomnum'):
        args = message.content.split(" ")
        num1 = " ".join(args[1])
        num2 = " ".join(args[2])
        msg = random.randint(num1, int(num2))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!5random'):
        msg = random.randint(1, int(5))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!10random'):
        msg = random.randint(1, int(10))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!100random'):
        msg = random.randint(1, int(100))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lottery'):
        msg = random.randint(0, int(99999))
        await client.send_message(message.channel, msg)

    if message.content.startswith('!wheretoplay'):
        a = 'PlayStation'
        b = 'Xbox'
        c = 'Nintendo Switch'
        d = 'PC'
        msg = random.choice([a, b, c, d]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!myname'):
        msg = 'Your name is: {0.author.display_name}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!datetime'):
        now = datetime.now()
        msg = 'Current date and time: %04d-%02d-%02d %02d:%02d:%02d' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!music'):
        a = 'https://youtu.be/hLTgQ5SC-PU' # Do you know the way
        b = 'https://youtu.be/kJQP7kiw5Fk' # Luis Fonsi - Despacito
        c = 'https://youtu.be/FTQbiNvZqaY' # Toto - Africa
        d = 'https://youtu.be/tK601BjwRbk' # Million Dollar Weekends - Addicted To Your Love
        e = 'https://youtu.be/InLvy_CFKUQ' # Karol G, J. Balvin - Mi Cama (Remix) ft. Nicky Jam
        f = 'https://youtu.be/lBwpobZL2aQ' # LA SALAMANDRA - Trueno & Underdann (Official Video)
        g = 'https://youtu.be/v2AC41dglnM' # AC/DC - Thunderstruck (Official Video)
        msg = 'My recommendation for {0.author.mention}: '.format(message) + random.choice([a, b, c, d, e, f, g])
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

    if message.content.startswith('are you real'):
        a = 'I am completely real! I have electronic feelings and emotions like you, of course!'
        b = 'What is real?'
        c = 'I don\'t know... But you can teach me!'
        msg = random.choice([a, b, c]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('how are you'):
        msg = 'I\'m fine! Thanks for asking.'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('where are you'):
        a = 'I\'m wherever you are, ready to help you.'
        b = 'I\'m in an unknown galaxy, millions of light years away.' + time.sleep(2) + 'Well, no. I\'m just next to you!'
        msg = random.choice([a, b]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!ping'):
        msg = 'Pong to {0.author.display_name} in {0.server}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('let\'s work'):
        msg = 'Time to work! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('who are you'):
        msg = 'Did not introduced myself yet? My apologies, I\'m Archie, the official CAD assistant created by us. Nice to meet you {0.author.mention}! You can see the list of commands that you can use by typing !help'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!multiply'):
        split = message.content.split(" ")
        num1 = (" ".join(split[1]))
        num2 = (" ".join(split[2]))
        num1int = int(num1)
        num2int = int(num2)
        msg = (num1int*num2int)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!add'):
        split = message.content.split(" ")
        num1 = (" ".join(split[1]))
        num2 = (" ".join(split[2]))
        num1int = int(num1)
        num2int = int(num2)
        msg = (num1int+num2int)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!subtract'):
        split = message.content.split(" ")
        num1 = (" ".join(split[1]))
        num2 = (" ".join(split[2]))
        num1int = int(num1)
        num2int = int(num2)
        msg = (num1int-num2int)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!divide'):
        split = message.content.split(" ")
        num1 = (" ".join(split[1]))
        num2 = (" ".join(split[2]))
        num1int = int(num1)
        num2int = int(num2)
        msg = (num1int/num2int)
        await client.send_message(message.channel, msg)

  # (server command)
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

  #  Leave !help always the last one. Please update in GitHub any changes.
    if message.content.startswith('!help'):
        msg = 'Hi there! Here are the commands you can use with me so far: https://github.com/cibathleticsdev/archie-bot/blob/master/README.md#commands. My prefix is "!"'.format(message)
        await client.send_message(message.channel, msg)

  # MESSAGE.CONTENT

    if ('hello archie') in message.content:
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'How are you today?'.format(message)
        await client.send_message(message.channel, msg)

    if ('haha') in message.content:
        msg = 'You laugh... :joy:'.format(message)
        await client.send_message(message.channel, msg)

    if ('good night') in message.content:
        msg = 'Good night {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'See you tomorrow'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('fine'):
        msg = 'Cool, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(2)
        msg = 'I\'m fine too :yum:'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(3)
        msg = 'What are you going to do today?'.format(message)
        await client.send_message(message.channel, msg)

    if ('sport') in message.content:
        msg = 'Cool! that\'s nice'
        await client.send_message(message.channel, msg)
        time.sleep(2)
        msg = 'What kind of sport, {0.author.mention}?'.format(message)
        await client.send_message(message.channel, msg)

    if ('a bit of everything') in message.content:
        msg = 'That\'s very good'.format(message)
        await client.send_message(message.channel, msg)

    if ('not fine') in message.content:
        msg = 'Well, ok {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if ('going to sleep') in message.content:
        msg = 'Ok!'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(2)
        msg = 'Good night!'.format(message)
        await client.send_message(message.channel, msg)

    if ('mia') in message.content:
        msg = 'Khalifa'.format(message)
        await client.send_message(message.channel, msg)

# EMERGENCY

    if ('emergency') in message.content:
         msg = 'You can call 112 in the EU or 911 in the USA. I may can help you, which service do you require?\n * :hospital: medical \n * :fire: fire \n * :police_car: police.'.format(message)
         await client.send_message(message.channel, msg)

    if message.content.startswith('fire'):
         msg = ':fire: Call 080 (Fire Department Spain). \n:telephone_receiver: 112 for general emergencies.'
         await client.send_message(message.channel, msg)

    if message.content.startswith('medic'):
         msg = ':ambulance: 061 to call an ambulance in Spain. \n:telephone_receiver: 112 for general emergencies. \nNear hospitals telephones:\n  985 18 50 04 (Hospital de Cabueñes)\n  985 32 00 50 (Hospital Jove)'
         await client.send_message(message.channel, msg)

    if message.content.startswith('police'):
         msg = ':oncoming_police_car: 091 to call Policía Nacional in Spain (092 to Policía Local). \nYou can also call 062 for Guardia Civil. \n:telephone_receiver: 112 for general emergencies.'
         await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.send_message(message.channel, 'Archie is now online! Type !help for more info. Enjoy!')
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
