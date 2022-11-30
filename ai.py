import random
import os
import time

import main

def ai(): # needs to determine risk and have risk tolerance factor to intelligently make a decision
    os.system("CLS")
    global difficulty
    print(difficulty)

    risk = 0
    risk_tolerance = 0 # percent chance to take a risk

    if difficulty.lower() == "e":       risk_tolerance = 65 # easy difficulty
    elif difficulty.lower() == "m":     risk_tolerance = 40 # medium difficulty
    elif difficulty.lower() == "h":     risk_tolerance = 15 # hard difficulty
    else:                               risk_tolerance = 50 # default difficulty

    print("HELLO MY NAME IS AI AND MY RISK TOLERANCE IS " + str(risk_tolerance))
    os.system("TIMEOUT 5")
    determine_risk()

def determine_risk():
    pass