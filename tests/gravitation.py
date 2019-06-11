import math
import discord
import asyncio
import random
import data
# import sys



# DATA #
G = data.G #6.67e-11
earth_mass = data.earth_mass #5.97e+24
moon_mass = data.moon_mass #7.34e+22
earth_radius = data.earth_radius #6371000
earth_moon_distance = data.earth_moon_distance #3.844e+8
earth_sun_distance = data.earth_sun_distance #1.496e+11
average_person_mass = data.average_person_mass #70
earth_gravity = data.earth_gravity #9.80665



# INPUT SCRIPT #
print('* * * * * * * * * * * * * * * * * * * * * * * *')
print('* G R A V I T A T I O N   C A L C U L A T O R *')
print('* * * * * * * * * * * * * * * * * * * * * * * *')
print(' ')
print('Type --help after the execution command (in a new line) to read the instructions and how to use the variables.')
input('Press any key to continue...')
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
