import math
import discord
import asyncio
import random
import data
import time


# DATA #
earth_gravity = data.earth_gravity #9.80665



# INPUT SCRIPT #
print('* * * * * * * * * * * * * * * * * * * * * * * * * * *')
print('* I N C L I N E D   P L A N E   C A L C U L A T O R *')
print('* * * * * * * * * * * * * * * * * * * * * * * * * * *')
print(' ')
print(' ')
time.sleep(2)
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
print(' ')
print(' ')
print(' ')
print(' ')
time.sleep(1)
print('Type --help after the execution command (in a new line) to read the instructions and how to use the variables.')
time.sleep(1)
input('Press any key to continue...')
print('Insert object mass (kg): ')
m = eval(input())
print('Insert gravity (m/s²): ')
g = eval(input())
print('Insert plane\'s inclination angel (DEG): ')
Â = eval(input())
print('Insert coefficient of friction: ')
µ = eval(input())




# CALCULATIONS AND FORMULES #
P = m * g
Px = m * g * math.sin(math.radians(Â))
Py = m * g * math.cos(math.radians(Â))
N = -Py
Fƒ = µ * N
Fres = Px - Fƒ
a = Fres / m



# DISPLAY SCRIPT #
print(' ')
print('INPUT')
print('m = ' + str(m) + ' kg')
print('g = ' + str(g) + ' m/s²')
print('Â = ' + str(Â) + 'º')
print('µ = ' + str(µ))
print(' ')
print('OUTPUT')
print('P = ' + str(P) + ' N')
print('Px = ' + str(Px) + ' N')
print('Py = ' + str(Py) + ' N')
print('N = ' + str(N) + ' N')
print('Fƒ = ' + str(Fƒ) + ' N')
print('Fres = ' + str(Fres) + ' N')
print('a (Fres) = ' + str(a) + ' m/s²')
