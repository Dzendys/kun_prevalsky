"""Klaudie simulator/deforming"""
import random
#KLAUDIE SIMULATOR
def klaudie_simulator(word: str) -> str:
    """Returns deformed word"""
    #CHANCES
    u_all: int = 4 #probability of missclick of ALL
    u_radky: int = 10 #probability of missclick to different keyboard line
    klaves: list = [["q","w","e","r","t","z","u","i","o","p"],["a","s","d","f","g","h","j","k","l"],["y","letter","c","v","b","n","m"]]
    returning_word: str = "" #returning value
    for letter in word:
        if random.randint(1,u_all) == 1: #probability of missclick of ALL (1/4)
            seznam: list = [] #saves all possible letters

            #very usual letters of missclick
            if letter == "a":
                seznam.append("q")
            elif letter=="e":
                seznam.append("w")
            elif letter == "p":
                seznam.append("o")

            #1st line on keyboard
            elif letter in klaves[0]:
                #left
                if klaves[0].index(letter) != 0:
                    for _ in range(u_radky):
                        seznam.append(klaves[0][klaves[0].index(letter)-1])
                #right
                if letter != klaves[0][-1]:
                    for _ in range(u_radky):
                        seznam.append(klaves[0][klaves[0].index(letter)+1])
                #down
                try:
                    seznam.append(klaves[1][klaves[0].index(letter)])
                except IndexError:
                    pass

            #2nd line on keyboard
            elif letter in klaves[1]:
                #left
                if klaves[1].index(letter) != 0:
                    for _ in range(u_radky):
                        seznam.append(klaves[1][klaves[1].index(letter)-1])
                #right
                if letter != klaves[1][-1]:
                    for _ in range(u_radky):
                        seznam.append(klaves[1][klaves[1].index(letter)+1])
                #down
                try:
                    seznam.append(klaves[2][klaves[1].index(letter)])
                except IndexError:
                    pass
                #up
                try:
                    seznam.append(klaves[0][klaves[1].index(letter)])
                except IndexError:
                    pass

            #3rd line on keyboard
            elif letter in klaves[2]:
                #left
                if klaves[2].index(letter) != 0:
                    for _ in range(u_radky):
                        seznam.append(klaves[2][klaves[2].index(letter)-1])
                #right
                if letter != klaves[2][-1]:
                    for _ in range(u_radky):
                        seznam.append(klaves[2][klaves[2].index(letter)+1])
                #up
                try:
                    seznam.append(klaves[1][klaves[2].index(letter)])
                except IndexError:
                    pass

            #if the letter is not on keyboard => stays same
            else:
                seznam.append(letter)

            #chooses one letter of all possibilities
            returning_word+=str(random.choice(seznam))

        #letter stays same
        else:
            returning_word+=str(letter)
    return returning_word
