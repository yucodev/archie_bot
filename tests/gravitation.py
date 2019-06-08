import math
import discord
import asyncio
import random




# DATA #
G = 6.67 * 10**-11
earth_mass = 5.97 * 10**24
moon_mass = 7.34 * 10**22
earth_radius = 6371000
earth_moon_distance = 384400000



# DISPLAY SCRIPT #
print('* * * * * * * * * * * * * * * * * * * * * * * *')
print('* G R A V I T A T I O N   C A L C U L A T O R *')
print('* * * * * * * * * * * * * * * * * * * * * * * *')
print(' ')
print('Type --help after the execution command (in a new line) to read the instructions and how to use the variables.')
input('Press any key to continue...')
print('Enter the bigger mass (kg): ')
M = eval(input())
print('Enter the smaller mass (kg): ')
m = eval(input())
print('Enter the distance of the objects or the radius of the orbit (m): ')
R = eval(input())
# DISPLAY SCRIPT #



# CALCULATIONS AND FORMULES #
g = G * M / (R**2)
P = m * g
a = G * m / (R**2)
v = math.sqrt(G * M / R)
T = (2 * math.pi * R) / v
uu = v / R     # or (2 * math.pi) / T



print(' ')
print('INPUT')
print('M = ' + str(M) + ' kg')
print('m = ' + str(m) + ' kg')
print('R = ' + str(R) + ' m')
print(' ')
print('OUTPUT')
print('P = ' + str(P) + ' N')
print('g = ' + str(g) + ' m/s2')
print('a = ' + str(a) + ' m/s2')
print('T = ' + str(T) + ' s')
print('v = ' + str(v) + ' m/s')
print('uu = ' + str(uu) + ' rad/s')
