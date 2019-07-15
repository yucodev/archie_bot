from data import *
import math
import discord
import asyncio
import random
import time

def info():
    print(UCyan + 'What is Cibathleticsdev Physics Calculator?' + Color_Off)
    print('This project contains some physics calculators like inclined-plane or gravitation. In them, some input (like a mass) is introduced and some output (weight, friction force, orbital velocity...) is expected.' + Color_Off)
    print(UCyan + 'Data variables' + Color_Off)
    print('Some data like Earth\'s mass or the radius of Mass\' orbit is stored in this program. Here are the available variables so far:')
    print('- average_person_mass')
    print('- earth_gravity')
    print('- earth_mass')
    print('- earth_moon_distance')
    print('- earth_radius')

    input("Press any key to continue...")
    program_start()


def input_loop():
    ProgramNumber = input()

    if ProgramNumber in ['E', 'e', 'EXIT', 'exit']:
        print('Leaving program')

    elif ProgramNumber == str(0):
        info()

    elif ProgramNumber == str(1):
        import inclinedplane

    elif ProgramNumber == str(2):
        import gravitation

    else:
        print(Red + 'ERROR: Unexpected input! Please try again:' + Color_Off)
        input_loop()


def program_start():
    print(Yellow + 'Which program would you like to start? You should read the INFO before starting the program for the first time.')
    print(' ' + Color_Off)
    print(Red + '[E] EXIT' + Color_Off)
    print(' ')
    print(Yellow + '[0] INFO')
    print('[1] Inclined plane')
    print('[2] Gravitation' + Color_Off)
    print(' ')
    input_loop()

time.sleep(1)
print(Yellow + 'WELCOME TO CIBATHLETICSDEV PHYSICS CALCULATOR!')
time.sleep(1)
program_start()
