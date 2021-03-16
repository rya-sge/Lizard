# -*- coding: utf-8 -*-

import random


tuple = ["Lizard", "Spock", "Paper", "Scissors", "Rock"]
score = 0
stopBreak = 0

def checkLiz(srvString):
    if srvString  == "Spock" or srvString  == "Paper":
        return "Win"
    elif srvString == "Lizard":
        return "Draw"
    else:
        return "Lose"

def checkSpock(srvString):
    if srvString  == "Scissors" or srvString  == "Rock":
        return "Win"
    elif srvString  == "Spock":
        return "Draw"
    else:
        return "Lose"



def checkPaper(srvString):
    if srvString == "Spock" or srvString == "Rock":
        return "Win"
    elif srvString == "Paper":
        return "Draw"
    else:
        return "Lose"


def checkSciss(srvString):
    if srvString  == "Lizard" or srvString  == "Paper":
        return "Win"
    elif srvString  == "Scissors":
        return "Draw"
    else:
        return "Lose"

def checkRock(srvString):
    if srvString  == "Lizard" or srvString  == "Scissors":
        return "Win"
    elif srvString  == "Rock":
        return "Draw"
    else:
        return "Lose"

def Win():
    global score
    score = score + 1


#Source switch : https://jaxenter.com/implement-switch-case-statement-python-138315.html
def switch(arg):
    if(arg > 4):
        return "Lost"
    srvValue = random.randint(0, 4)
    srvString = tuple[srvValue]
    switcher = {
        1: checkLiz(srvString),
        2: checkSpock(srvString),
        3: checkPaper(srvString),
        4: checkSciss(srvString),
        5: checkRock(srvString),
    }
    # Get the function from switcher dictionary
    fun = switcher.get(arg, lambda: "NON")
    if(fun == "Win"):
        Win()
    return fun
def main():
    global score
    MAX = 10
    count = 0
    while(True):
        try:
            arg = input("Entrez votre valeur : ")
        except:
            print("Ce n'est pas permis")
        if(isinstance(arg, (int, float))):
            res = switch(int(arg))
            print res
        if score >= MAX:
            print("Yes, you are too incredible")
        count = count + 1
        if count == MAX:
            score = 0
            count = 0

if __name__ == "__main__":
    # execute only if run as a script
    main()

