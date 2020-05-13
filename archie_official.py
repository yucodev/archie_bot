######################################
#  Cibernetic Athletics Developers   #
#  Code by PyJavaPulver and Viktaur  #
#  Based on: 'discord.py' library    #
#  Copyright  ©2018-2019  V. 2.1.1   #
######################################

### please run this script only with Python3

if __name__ == '__main__':
    import botversion

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import requests
from fortnite_python import Fortnite
import os
from os import getenv
import asyncio
import ctx
from weather import Weather, Unit
import time
from datetime import datetime
import pytz
import random
import site
from apex_PC import ApexLegends
from apex_XBOX import ApexLegendsXBOX
from apex_PSN import ApexLegendsPSN
from gametokens import *
import sys
import config
# hide config.py
sys.path.insert(0, '/home/dietpi/discord')

client = discord.Client()

# do not remove, this is for other servers without welcome-bot.

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.author.bot: return

    if message.content.startswith('!apexplayerpc'):
       string = message.content.split(" ")
       player_name = str(" ".join(string[1:]))
       player = apex.player(player_name)
       for legend in player.legends:
           await client.send_message(message.channel, player_name + '\'s' + ' status with ' + legend.legend_name + ':')
           await client.send_message(message.channel, player)
           await client.send_message(message.channel, legend.icon)
           break

    if message.content.startswith('!apexplayerpsn'):
       string = message.content.split(" ")
       player_name = str(" ".join(string[1:]))
       playerPSN = apexPSN.playerPSN(player_name)
       for legend in player.legends:
           await client.send_message(message.channel, player_name + '\'s' + ' status with ' + legend.legend_name + ':')
           await client.send_message(message.channel, player)
           await client.send_message(message.channel, legend.icon)
           break

    if message.content.startswith('!apexplayerxbox'):
       string = message.content.split(" ")
       player_name = str(" ".join(string[1:]))
       playerXBOX = apexXBOX.playerXBOX(player_name)
       for legend in player.legends:
           await client.send_message(message.channel, player_name + '\'s' + ' status with ' + legend.legend_name + ':')
           await client.send_message(message.channel, player)
           await client.send_message(message.channel, legend.icon)
           break

    if message.content.startswith('!fortniteplayer'):
        apiKey = {"TRN-Api-Key": "34a3d375-b089-4409-a2ce-e34472ff4ebe"}
        string = message.content.split(" ")
        platform = str(" ".join(string[1:]))
        q1 = 'PC'
        if q1 == "PC":
          platform = "pc"
        elif q1 == "Playstation" or "PS4" or "psn":
          platform = "psn"
        elif q1 == "XBox":
          platform = "xbl"
        s2 = str(" ".join(string[2:]))
        name = s2
        url = "https://api.fortnitetracker.com/v1/profile/" + platform + "/" + name
        req = requests.get(url, headers=apiKey)
        data = req.json()
        solo_wins = data["stats"]["p2"]["top1"]["valueInt"]
        await client.send_message(message.channel, 'Solo Wins: ' + str(solo_wins))
        print("Solo Wins:", solo_wins)

    if message.content.startswith('!fortnitenews'):
        msg = 'Last Fortnite news: https://www.epicgames.com/fortnite/en/news'
        await client.send_message(message.channel, msg)

    #### Weather yahoo API is no longer available ####

    #if message.content.startswith('!weathercel'):
    #    weather = Weather(unit=Unit.CELSIUS)
    #    city = message.content.split(" ")
    #    CITYUP = str(" ".join(city[1:])).upper()
    #    location = weather.lookup_by_location(" ".join(city[1:]))
    #    forecasts = location.forecast
    #    await client.send_message(message.author, '_**WEATHER FORECAST CELSIUS %s **_' % (CITYUP))
    #    msg = 'Forecast sent via DM'
    #    await client.send_message(message.channel, msg)
    #    time.sleep(1)
    #    for forecast in forecasts:
    #        await client.send_message(message.author, '**On ' + forecast.date + '**')
    #        await client.send_message(message.author, ' :low_brightness: ' + forecast.text)
    #        await client.send_message(message.author, ' :small_orange_diamond: Max temp. ' + forecast.high)
    #        await client.send_message(message.author, ' :small_blue_diamond: Min temp. ' + forecast.low)
    #        await client.send_message(message.author, ' --------------------- ')

    #if message.content.startswith('!todayweathercel'):
    #    weather = Weather(unit=Unit.CELSIUS)
    #    city = message.content.split(" ")
    #    location = weather.lookup_by_location(" ".join(city[1:]))
    #    forecasts = location.forecast
    #    #msg1 = 'Forecast in Celsius for {0.author.mention} in ' + city
    #    #msg = msg1.format(message)
    #    #await client.send_message(message.channel, msg)
    #    time.sleep(1)
    #    for forecast in forecasts:
    #        await client.send_message(message.channel, '**On ' + forecast.date + ' (ºC)**')
    #        await client.send_message(message.channel, ' :low_brightness: ' + forecast.text)
    #        await client.send_message(message.channel, ' :small_orange_diamond: Max temp. ' + forecast.high)
    #        await client.send_message(message.channel, ' :small_blue_diamond: Min temp. ' + forecast.low)
    #        if ('today') in message.content:
    #            break
    #        await client.send_message(message.channel, ' --------------------- ')

    #if message.content.startswith('!weatherfar'):
    #    weather = Weather(unit=Unit.FAHRENHEIT)
    #    city = message.content.split(" ")
    #    CITYUP = str(" ".join(city[1:])).upper()
    #    location = weather.lookup_by_location(" ".join(city[1:]))
    #    forecasts = location.forecast
    #    await client.send_message(message.author, '_**WEATHER FORECAST FAHRENHEIT %s **_' % (CITYUP))
    #    msg = 'Forecast sent per DM'
    #    await client.send_message(message.channel, msg)
    #    time.sleep(1)
    #    for forecast in forecasts:
    #        await client.send_message(message.author, '**On ' + forecast.date + '**')
    #        await client.send_message(message.author, ' :low_brightness: ' + forecast.text)
    #        await client.send_message(message.author, ' :small_orange_diamond: Max temp. ' + forecast.high)
    #        await client.send_message(message.author, ' :small_blue_diamond: Min temp. ' + forecast.low)
    #        await client.send_message(message.author, ' --------------------- ')

    #if message.content.startswith('!todayweatherfar'):
    #     weather = Weather(unit=Unit.FAHRENHEIT)
    #     city = message.content.split(" ")
    #     location = weather.lookup_by_location(" ".join(city[1:]))
    #     forecasts = location.forecast
    #     # msg1 = 'Forecast in Fahrenheit for {0.author.mention} in ' + city
    #     # msg = msg1.format(message)
    #     # await client.send_message(message.channel, msg)
    #     time.sleep(1)
    #     for forecast in forecasts:
    #         await client.send_message(message.channel, '**On ' + forecast.date + ' (ºF)**')
    #         await client.send_message(message.channel, ' :low_brightness: ' + forecast.text)
    #         await client.send_message(message.channel, ' :small_orange_diamond: Max temp. ' + forecast.high)
    #         await client.send_message(message.channel, ' :small_blue_diamond: Min temp. ' + forecast.low)
    #         if ('today') in message.content:
    #             break
    #         await client.send_message(message.channel, ' --------------------- ')

    #### END WEATHER SCRIPT ####

    if message.content.startswith('!echo'):
        echo = message.content.split(" ")
        await client.send_message(message.channel, '%s' % (" ".join(echo[1:])))

    if message.content.startswith('!sendme'):
        sendme = message.content.split(" ")
        await client.send_message(message.author, '%s' % (" ".join(sendme[1:])))

    if message.content.startswith('!myid'):
        msg = 'Your user ID is: {0.author.id}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('archie'):
        msg = 'What do you want?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!joke'):
        jokes = [
            ('Can a kangaroo jump higher than a house?', 'Of course, a house doesn’t jump at all.'),
            ('Anton, do you think I’m a bad mother?', 'My name is Paul.'),
            ('Why can\'t cats work with a computer?', 'Because they get too distracted chasing the mouse around!'),
            ('My dog used to chase people on a bike a lot.', 'It got so bad, finally I had to take his bike away.'),
            ('What do Italian ghosts have for dinner?', 'Spook-hetti!')]
        setup, punchline = random.choice(jokes)
        await client.send_message(message.channel, setup)
        await asyncio.sleep(3)
        await client.send_message(message.channel, punchline)

    if message.content.startswith('!quiz'):
        #split = message.content.split(" ")
        #response = (" ".join(split[1:]))
        msg = 'Can cats fly? (yes/no)'
        await client.send_message(message.channel, msg)
        if message.content.startswith('no'):
        #if response == "no":
            await client.send_message(message.channel, 'Noooooo')
            time.sleep(2)
            await client.send_message(message.channel, 'But I wish they did... :heart_eyes_cat:')
        if message.content.startswith('yes'):
        #if response == "yes":
             print("lol")
             await client.send_message(message.channel, 'Of course they can!')
             time.sleep(2)
             await client.send_message(message.channel, 'Well, no.')

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
        a = 'Red'
        b = 'Blue'
        c = 'Green'
        d = 'Lime'
        e = 'White'
        f = 'Black'
        g = 'Yellow'
        h = 'Gray'
        i = 'Orange'
        msg = random.choice([a, b, c, d, e, f, g, h, i]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomsport'):
        a = 'Tennis'
        b = 'Basketball'
        c = 'Golf'
        d = 'Athletics'
        e = 'Rugby'
        f = 'Baseball'
        g = 'Canoeing'
        h = 'Badminton'
        i = 'Ski'
        msg = random.choice([a, b, c, d, e, f, g, h, i]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randommobilegame'):
        a = 'Clash of Clans'
        b = 'Clash Royale'
        c = 'Pokemon Go'
        d = 'Helix Jump'
        e = 'Arena of Valor'
        f = 'Modern Combat 5'
        g = 'Angry Birds'
        h = 'Candy Crush'
        i = 'SimCity BuildIt'
        j = 'Subway Surfers'
        k = 'Tigerball'
        l = 'Plants vs Zombies'
        m = 'Hungry Shark World'
        n = 'Smash Hit'
        msg = random.choice([a, b, c, d, e, f, g, h, i, j, k, l, m, n]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomcarbrand'):
        a = 'Alfa Romeo'
        b = 'Audi'
        c = 'BMW'
        d = 'Aston Martin'
        e = 'Bentley'
        f = 'Bugatti'
        g = 'Chevrolet'
        h = 'Seat'
        i = 'Ferrari'
        j = 'Lamboghini'
        k = 'Maserati'
        l = 'Jaguar'
        m = 'Mercedes'
        n = 'McLaren'
        o = 'Porsche'
        p = 'Tesla'
        q = 'Volkswagen'
        r = 'Opel'
        s = 'Mazda'
        msg = random.choice([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomclothe'):
        a = 'Nike'
        b = 'Adidas'
        c = 'Levis'
        d = 'Holister'
        e = 'Abercrombie'
        f = 'Hunder Armour'
        g = 'Gucci'
        h = 'Lacoste'
        i = 'Vans'
        j = 'Supreme'
        k = 'asics'
        l = 'Pepe Jeans'
        m = 'Kappa'
        n = 'Kelme'
        o = 'Calvin Klein'
        p = 'Quicksilver'
        q = 'Diesel'
        r = 'puma'
        s = 'Rip Curl'
        t = 'Joma'
        u = 'Fila'
        msg = random.choice([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomseries'):
        a = 'Money Heist'
        b = 'Narcos'
        c = 'The End of the F***ing World'
        d = '13 Reasons Why'
        e = 'Game of Thrones'
        f = 'The Simpsons'
        g = 'Dragonball'
        h = 'Fawlty Towers'
        i = 'Pokemon'
        j = 'Bright'
        k = 'The Big Bang Theory'
        l = 'Breaking Bad'
        m = 'Stranger Things'
        n = 'sense8'
        o = 'House of Cards'
        p = 'Lost in Space'
        q = 'GLOW'
        r = 'Queer Eye'
        s = 'The Crown'
        t = 'Lucifer'
        u = 'American Horror History'
        v = 'The Walking Dead'
        w = 'Riverdale'
        x = 'Disenchantment'
        y = 'Teen Wolf'
        z = 'Orange is the new Black'
        aa = 'Sex Education'
        ab = 'Prison Break'
        msg = random.choice([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!botinfo'):
        msg = 'Archie Bot (version ' + botversion.version + ') ©2019\nA funny Discord Bot with a lot of features! For more info visit our GitHub repository https://github.com/cibathleticsdev/archie-bot or type !help to see the commands you can use with me so far.'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!credits'):
        msg = '- PyJavaPulver (https://github.com/PyJavaPulver)\n- viktaur (https://github.com/viktaur)\n***With the collaboration of:***\n- TheAlx1Boy (https://github.com/TheAlx1Boy)\n- varitogolf (https://github.com/varitogolf)\nCybernetic Athletics Developers ©2018-2019 (http://cadevelopers.ml/, https://github.com/cibathleticsdev)\nAll rights reserved.'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!flipcoin'):
        a = 'Heads :fire:'
        b = 'Tails :snowflake:'
        msg = random.choice([a, b]).format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!randomnum'):
        args = message.content.split(" ")
        num1 = int(" ".join(args[1]))
        num2 = int(" ".join(args[2]))
        # msg1 = num1, num2
        # await client.send_message(message.channel, msg1)
        msg = random.randint(num1, num2)
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
        now = datetime.utcnow()
        # now = datetime.now()
        msg = 'Current date and time: %04d-%02d-%02d %02d:%02d:%02d (UTC)' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!music'):
        a = 'https://youtu.be/hLTgQ5SC-PU' # Do you know the way
        b = 'https://youtu.be/kJQP7kiw5Fk' # Luis Fonsi - Despacito
        c = 'https://youtu.be/FTQbiNvZqaY' # Toto - Africa
        d = 'https://youtu.be/tK601BjwRbk' # Million Dollar Weekends - Addicted To Your Love
        e = 'https://youtu.be/v2AC41dglnM' # AC/DC - Thunderstruck (Official Video)
        msg = 'My recommendation for {0.author.mention}: '.format(message) + random.choice([a, b, c, d, e,])
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

    if message.content.startswith('!math'):
        split = message.content.split(" ")
        operation = (" ".join(split[1:]))
        operationeval = eval(operation)
        # await client.send_message(message.channel, operation)
        await client.send_message(message.channel, operationeval)
#'%s' % (" ".join(operationeval[1:])))

    # if message.content.startswith('!multiply'):
    #     split = message.content.split(" ")
    #     num1 = (" ".join(split[1]))
    #     num2 = (" ".join(split[2]))
    #     num1int = int(num1)
    #     num2int = int(num2)
    #     msg = (num1int*num2int)
    #     await client.send_message(message.channel, msg)
    #
    # if message.content.startswith('!add'):
    #     split = message.content.split(" ")
    #     num1 = (" ".join(split[1]))
    #     num2 = (" ".join(split[2]))
    #     num1int = int(num1)
    #     num2int = int(num2)
    #     msg = (num1int+num2int)
    #     await client.send_message(message.channel, msg)
    #
    # if message.content.startswith('!subtract'):
    #     split = message.content.split(" ")
    #     num1 = (" ".join(split[1]))
    #     num2 = (" ".join(split[2]))
    #     num1int = int(num1)
    #     num2int = int(num2)
    #     msg = (num1int-num2int)
    #     await client.send_message(message.channel, msg)
    #
    # if message.content.startswith('!divide'):
    #     split = message.content.split(" ")
    #     num1 = (" ".join(split[1]))
    #     num2 = (" ".join(split[2]))
    #     num1int = int(num1)
    #     num2int = int(num2)
    #     msg = (num1int/num2int)
    #     await client.send_message(message.channel, msg)

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
        a = 'What are you going to do today?'
        b = 'Where are you came from?'
        c = 'Do you like animals?'
        msg = random.choice([a, b]).format(message)
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
    await client.change_presence(game=discord.Game(name="CADevelopers | !help"))
    await client.send_message(discord.Object(id='481951758722138113'), 'Archie is now online! Type !help for more info. Enjoy!')


if __name__ == '__main__':
    import config
    client.run(config.token)
