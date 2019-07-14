from data import *
import math
import discord
import asyncio
import random
import time

def start():
    time.sleep(1)
    print(Yellow + 'Which program would you like to start?')
    time.sleep(2)
    print(' ')
    print('[1] Inclined plane')
    print('[2] Gravitation' + Color_Off)
    ProgramNumber = input()

    if ProgramNumber == 1:
        import inclinedplane

    elif ProgramNumber == 2:
        import gravitation

    else:
        print('Unexpected input, let\'s try again!')
        time.sleep(1.5)
        start()

start()
