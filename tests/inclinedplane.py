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


# INITIAL SCRIPT #
def initial():
    clear()
    time.sleep(0.01)
    print(Cyan + ' ')
    print('* * * * * * * * * * * * * * * * * * * * * * * * * * *')
    print('* I N C L I N E D   P L A N E   C A L C U L A T O R *')
    print('* * * * * * * * * * * * * * * * * * * * * * * * * * *')
    time.sleep(1)
    print(' ')
    time.sleep(0.1)
    print(' ')
    time.sleep(0.1)
    print('                                                    *')
    time.sleep(0.1)
    print('                                                 ****')
    time.sleep(0.1)
    print('                                              *******')
    time.sleep(0.1)
    print('                                           **********')
    time.sleep(0.1)
    print('                                         ************')
    time.sleep(0.1)
    print('                                      ***************')
    time.sleep(0.1)
    print('                                   ******************')
    time.sleep(0.1)
    print('                                *********************')
    time.sleep(0.1)
    print('                             ************************')
    time.sleep(0.1)
    print('                          ***************************')
    time.sleep(0.1)
    print('                       ******************************')
    time.sleep(0.1)
    print('                    *********************************')
    time.sleep(0.1)
    print('                 ************************************')
    time.sleep(0.1)
    print('              ***************************************')
    time.sleep(0.1)
    print('           ******************************************')
    time.sleep(0.1)
    print('        *********************************************')
    time.sleep(0.1)
    print('     ************************************************')
    time.sleep(0.1)
    print('  ***************************************************')
    time.sleep(0.1)
    print(' ')
    time.sleep(0.1)
    print(' ')
    time.sleep(0.1)
    print(' ')
    time.sleep(0.1)
    print(' ' + Color_Off)
    time.sleep(1)
    print(Cyan + 'Press "S" to start calculator, "H" for help or information, "M" to return to the main menu or "E" to exit the program. Then press enter.' + Color_Off)

    return

def home():
    # print(Cyan + 'Press "S" to start calculator, "H" for help or information, "M" to return to the main menu or "E" to exit the program. Then press enter.' + Color_Off)
    home.varinput = input()

    if home.varinput in ['S', 's', 'START', 'start']:
        # INPUT SCRIPT #

        def ObjectMass():
            mNoEval = input().lower()
            try:
                m = eval(mNoEval)
            except NameError:
                print(Red + 'ERROR: Unexpected input! Please try again:' + Color_Off)
                time.sleep(0.01)
                ObjectMass()
            return m

        print(Cyan + 'Insert object mass (kg): ' + Color_Off)
        ObjectMass()



        def ObjectGravity():
            gNoEval = input().lower()
            try:
                g = eval(gNoEval)
            except NameError:
                print(Red + 'ERROR: Unexpected input! Please try again:' + Color_Off)
                time.sleep(0.01)
                ObjectGravity()
            return g

        print(Cyan + 'Insert gravity (m/s²): ' + Color_Off)
        ObjectGravity()



        def ObjectInclination():
            ÂNoEval = input().lower()
            try:
                Â = eval(ÂNoEval)
            except NameError:
                print(Red + 'ERROR: Unexpected input! Please try again:' + Color_Off)
                time.sleep(0.01)
                ObjectInclination()
            return Â


        print(Cyan + 'Insert plane\'s inclination angel (DEG): ' + Color_Off)
        ObjectInclination()



        def ObjectFrictionCoef():
            µNoEval = input().lower()
            try:
                µ = eval(µNoEval)
            except NameError:
                print(Red + 'ERROR: Unexpected input! Please try again:' + Color_Off)
                time.sleep(0.01)
                ObjectFrictionCoef()
            return µ

        print(Cyan + 'Insert coefficient of friction: ' + Color_Off)
        ObjectFrictionCoef()



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
        time.sleep(3)
        print(' ')
        print(' ')
        print(Cyan + 'Press "S" to start calculator, "H" for help or information, "M" to return to the main menu or "E" to exit the program. Then press enter.' + Color_Off)
        home()
        return


    elif home.varinput in ['H', 'h', 'HELP', 'help', 'INFO', 'info', 'I', 'i']:
        from physics import info

    elif home.varinput in ['E', 'e', 'EXIT', 'exit']:
        print('Leaving program')

    elif home.varinput in ['M', 'm', 'MENU', 'menu']:
        import physics

    else:
        print(Red + 'ERROR: Unexpected input! Please try again:' + Color_Off)
        home()

    return

# while True:
#     initial()
#     home()

initial()
home()
