from data import *
import math
import discord
import asyncio
import random
import time
import subprocess
import platform

def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)

def info():
    clear()
    time.sleep(0.01)
    print(UCyan + 'What is YuCode Dev Physics Calculator?' + Color_Off)
    print('This project contains some physics calculators like inclined-plane or gravitation. In them, some input (like a mass) is introduced and some output (weight, friction force, orbital velocity...) is expected.' + Color_Off)
    print(UCyan + 'Data variables' + Color_Off)
    print('Some data like Earth\'s mass or the radius of Mass\' orbit is stored in this program. Here are the available variables so far:')
    print('- average_person_mass')
    print('- earth_gravity')
    print('- earth_mass')
    print('- earth_moon_distance')
    print('- earth_radius')
    print('- earth_sun_distance')
    print('- G (gravitational_constant)')
    print('- jupiter_mass')
    print('- mars_mass')
    print('- mars_sun_distance')
    print('- mercury_mass')
    print('- mercury_sun_distance')
    print('- moon_mass')
    print('- neptune_mass')
    print('- saturn_mass')
    print('- uranus_mass')
    print('- venus_mass')
    print('- venus_sun_distance')


    input(Green + "Press any key to continue..." + Color_Off)
    clear()
    time.sleep(0.01)
    program_start()
    return


def input_loop():
    ProgramNumber = input()

    if ProgramNumber in ['E', 'e', 'EXIT', 'exit']:
        print(Red + 'Leaving program' + Color_Off)

    elif ProgramNumber == str(0):
        info()

    elif ProgramNumber == str(1):
        import inclinedplane

    elif ProgramNumber == str(2):
        import gravitation

    else:
        print(Red + 'ERROR: Unexpected input! Please try again:' + Color_Off)
        input_loop()

    return


def program_start():
    print(' ')
    print(Yellow + 'Which program would you like to start? You should read the INFO before starting the program for the first time.')
    print(' ' + Color_Off)
    print(Red + '[E] EXIT' + Color_Off)
    print(Green + '[0] INFO' + Color_Off)
    print(Yellow + '[1] Inclined plane' + Color_Off)
    print(Yellow + '[2] Gravitation' + Color_Off)
    print(' ')
    input_loop()
    return

# time.sleep(1)
clear()
time.sleep(0.01)
print(Yellow + 'WELCOME TO YUCODE DEV PHYSICS CALCULATOR!')
time.sleep(1)

program_start()
