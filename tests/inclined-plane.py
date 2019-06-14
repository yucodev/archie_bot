import math
import discord
import asyncio
import random
import data
import time

# CONSOLE COLORS #

# Regular colors
Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"        # White
Color_Off="\033[0m"       # Text Reset

# Bold
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White


# DATA #
earth_gravity = data.earth_gravity #9.80665



# INPUT SCRIPT #
print(Cyan + '* * * * * * * * * * * * * * * * * * * * * * * * * * *')
print('* I N C L I N E D   P L A N E   C A L C U L A T O R *')
print('* * * * * * * * * * * * * * * * * * * * * * * * * * *')
time.sleep(1)
print(' ')
time.sleep(0.1)
print(' ')
time.sleep(0.1)
print('                                                    ***')
time.sleep(0.1)
print('                                                 ******')
time.sleep(0.1)
print('                                              *********')
time.sleep(0.1)
print('                                           ************')
time.sleep(0.1)
print('                                         **************')
time.sleep(0.1)
print('                                      *****************')
time.sleep(0.1)
print('                                   ********************')
time.sleep(0.1)
print('                                ***********************')
time.sleep(0.1)
print('                             **************************')
time.sleep(0.1)
print('                          *****************************')
time.sleep(0.1)
print('                       ********************************')
time.sleep(0.1)
print('                    ***********************************')
time.sleep(0.1)
print('                 **************************************')
time.sleep(0.1)
print('              *****************************************')
time.sleep(0.1)
print('           ********************************************')
time.sleep(0.1)
print('        ***********************************************')
time.sleep(0.1)
print('     **************************************************')
time.sleep(0.1)
print('  *****************************************************')
time.sleep(0.1)
print(' ')
time.sleep(0.1)
print(' ')
time.sleep(0.1)
print(' ')
time.sleep(0.1)
print(' ')
time.sleep(1)

print('Type "S" to start calculator or "H" for help or information. Then press enter.' + Color_Off)
varinput = input()

if varinput in ['S', 's']:
    print(Cyan + 'Insert object mass (kg): ' + Color_Off)
    m = eval(input())
    print(Cyan + 'Insert gravity (m/s²): ' + Color_Off)
    g = eval(input())
    print(Cyan + 'Insert plane\'s inclination angel (DEG): ' + Color_Off)
    Â = eval(input())
    print(Cyan + 'Insert coefficient of friction: ' + Color_Off)
    µ = eval(input())

    # CALCULATIONS AND FORMULES #
    P = m * g
    Px = m * g * math.sin(math.radians(Â))
    Py = m * g * math.cos(math.radians(Â))
    N = -Py
    Fƒ = µ * N
    Fres = Px + Fƒ
    a = Fres / m

    # DISPLAY SCRIPT #
    print(' ')
    print(Cyan + 'INPUT' + Color_Off)
    print('m = ' + str(m) + ' kg')
    print('g = ' + str(g) + ' m/s²')
    print('Â = ' + str(Â) + 'º')
    print('µ = ' + str(µ))
    print(' ')
    print(Cyan + 'OUTPUT' + Color_Off)
    print('P = ' + str(P) + ' N')
    print('Px = ' + str(Px) + ' N')
    print('Py = ' + str(Py) + ' N')
    print('N = ' + str(N) + ' N')
    print('Fƒ = ' + str(Fƒ) + ' N')
    print('Fres = ' + str(Fres) + ' N')
    print('a (Fres) = ' + str(a) + ' m/s²')
elif varinput in ['H', 'h']:
    print('HERE WILL BE HELP DOCS AND SOME INFO')
else:
    print('ERROR')
# # CALCULATIONS AND FORMULES #
# P = m * g
# Px = m * g * math.sin(math.radians(Â))
# Py = m * g * math.cos(math.radians(Â))
# N = -Py
# Fƒ = µ * N
# Fres = Px + Fƒ
# a = Fres / m
#
#
#
# # DISPLAY SCRIPT #
# print(' ')
# print('INPUT')
# print('m = ' + str(m) + ' kg')
# print('g = ' + str(g) + ' m/s²')
# print('Â = ' + str(Â) + 'º')
# print('µ = ' + str(µ))
# print(' ')
# print('OUTPUT')
# print('P = ' + str(P) + ' N')
# print('Px = ' + str(Px) + ' N')
# print('Py = ' + str(Py) + ' N')
# print('N = ' + str(N) + ' N')
# print('Fƒ = ' + str(Fƒ) + ' N')
# print('Fres = ' + str(Fres) + ' N')
# print('a (Fres) = ' + str(a) + ' m/s²')
