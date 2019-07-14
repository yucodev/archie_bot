import math
import discord
import asyncio
import random

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

# Underline
UBlack="\033[4;30m"       # Black
URed="\033[4;31m"         # Red
UGreen="\033[4;32m"       # Green
UYellow="\033[4;33m"      # Yellow
UBlue="\033[4;34m"        # Blue
UPurple="\033[4;35m"      # Purple
UCyan="\033[4;36m"        # Cyan
UWhite="\033[4;37m"       # White



# DATA #
average_person_mass = 70
earth_gravity = 9.80665
earth_mass = 5.97e+24
earth_moon_distance = 3.844e+8
earth_radius = 6371000
earth_sun_distance = 1.496e+11
G = 6.67e-11
jupiter_mass = 1.898e+27
mars_mass = 6.39e+23
mars_sun_distance = 227.9e+6
mercury_mass = 3.285e+23
mercury_sun_distance = 57.91e+6
moon_mass = 7.34e+22
neptune_mass = 1.024e+26
saturn_mass = 5.683e+26
uranus_mass = 8.681e+25
venus_mass = 4.867e+24
venus_sun_distance = 108.2e+6
