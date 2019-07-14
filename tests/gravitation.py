from data import *
import math
import discord
import asyncio
import random
import time



# INPUT SCRIPT #
print('* * * * * * * * * * * * * * * * * * * * * * * *')
print('* G R A V I T A T I O N   C A L C U L A T O R *')
print('* * * * * * * * * * * * * * * * * * * * * * * *')
time.sleep(1)
print(' ')
time.sleep(0.1)
print(' ')
time.sleep(0.1)
print('                 *            *       *        ')
time.sleep(0.1)
print('           *         *    *       *            ')
time.sleep(0.1)
print('       *          * *                   *      ')
time.sleep(0.1)
print('             *         *     *       *      *  ')
time.sleep(0.1)
print('           *         *   *              *      ')
time.sleep(0.1)
print('                                               ')
time.sleep(0.1)
print('                                               ')
time.sleep(0.1)
print('                     ****                      ')
time.sleep(0.1)
print('                   ********                    ')
time.sleep(0.1)
print('                  **********                   ')
time.sleep(0.1)
print('      (________  ************  _________)      ')
time.sleep(0.1)
print('      (________  ************  _________)      ')
time.sleep(0.1)
print('                  **********                   ')
time.sleep(0.1)
print('                   ********                    ')
time.sleep(0.1)
print('                     ****                      ')
time.sleep(0.1)



print('Press "S" to start calculator or "H" for help or information. Then press enter.')
varinput = input()

if varinput in ['S', 's']:
    print('Insert the bigger mass (kg): ')
    M = eval(input())
    print('Insert the smaller mass (kg): ')
    m = eval(input())
    print('Insert the distance of the objects or the radius of the orbit (m): ')
    R = eval(input())

    # CALCULATIONS AND FORMULES #
    g = G * M / (R**2)
    a = G * m / (R**2)
    P = m * g
    P2 = M * a * (-1)
    v = math.sqrt(G * M / R)
    T = (2 * math.pi * R) / v
    uu = v / R     # or (2 * math.pi) / T

    # DISPLAY SCRIPT #
    print(' ')
    print('INPUT')
    print('M = ' + str(M) + ' kg')
    print('m = ' + str(m) + ' kg')
    print('R = ' + str(R) + ' m')
    print(' ')
    print('OUTPUT')
    print('P (M on m) = ' + str(P) + ' N')
    print('P (m on M) = ' + str(P2) + ' N')
    print('g = ' + str(g) + ' m/s2')
    print('a = ' + str(a) + ' m/s2')
    print('T = ' + str(T) + ' s')
    print('v = ' + str(v) + ' m/s')
    print('uu = ' + str(uu) + ' rad/s')
elif varinput in ['H', 'h']:
    print('HERE WILL BE HELP DOCS AND SOME INFO')
else:
    print('ERROR, ABORTING')
