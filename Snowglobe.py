"""Snowglobe gamble"""
import random

def snowglobe() -> str:
    """Returns one tank as in World of Tanks Blitz Christmas event according to tanks drop chances."""
    with open("resources/snowglobe.txt", "r", encoding="utf8") as file: #imports tanks and percentages from file
        text = [a.split(" ") for a in file.readlines()] #splits each line
    chances = []
    for tank in text:
        if tank[-1] == " " or tank[-1] == "\n" or tank[-1] == "": #something like .strip()
            tank.pop()
        if "\n" in tank[-1]: #checks if the ends contains enter
            num = tank[-1][:-2:] #saves the percentage
        else:
            num = tank[-1][:-1:] #saves the percentage
        tank.pop() #deletes the percentage at the end
        for _ in range(int(num)): #appends to list of tanks (percent)times
            chances.append(" ".join(tank))
    return random.choice(chances) #random choice
