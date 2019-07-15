from data import *
import math
import discord
import asyncio
import random
import time


def input_loop():
    ProgramNumber = input()

    if ProgramNumber == str(1):
        import inclinedplane

    elif ProgramNumber == str(2):
        import gravitation

    else:
        print('Unexpected input! Please try again')
        time.sleep(1.5)
        input_loop()


time.sleep(1)
print(Yellow + 'Welcome to Cibathleticsdev Physics Calculator!')
time.sleep(1)
print(Yellow + 'Which program would you like to start?')
time.sleep(2)
print(' ')
print('[1] Inclined plane')
print('[2] Gravitation' + Color_Off)
input_loop()
