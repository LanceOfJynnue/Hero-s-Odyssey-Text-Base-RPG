import math
import random
import os
from pathlib import Path
import json

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def arrayAvg(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum/len(array)

def arrayMode(array):
    mode = 0
    maxCount = 0
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[j] == array[i]:
                count += 1
        if count > maxCount:
            maxCount = count
            mode = array[i]
    return mode

def arrayMedian(array):
    array.sort()
    if len(array) % 2 == 0:
        median1 = array[len(array)//2]
        median2 = array[len(array)//2 - 1]
        median = (median1 + median2)/2
    else:
        median = array[len(array)//2]
    return median

def arrayMax(array):
    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    return max

def arrayMin(array):
    min = array[0]
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
    return min

def arraySum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum

def arrayRand(min,max,sel):
    array = []
    for i in range(min,max):
        array.insert(len(array),i)
    
    for i in range(len(array)):
        j = random.randint(0,len(array)-1)
        array[i], array[j] = array[j], array[i]
        
    array = array[0:sel]
    return array

def arrayShuffle(array):
    for i in range(len(array)):
        j = random.randint(0,len(array)-1)
        array[i], array[j] = array[j], array[i]
    return array

def isDigit(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def isBool(string):
    if string.lower() == "true" or string.lower() == "false":
        return True
    else:
        return False
    
def isList(string):
    if string.startswith("[") and string.endswith("]"):
        return True
    else:
        return False

def isString(string):
    if isinstance(string, str):
        return True
    else:
        return False

def questionChoices():
    print("\nPlease select and type the number corresponding to your choice:" )
    print("1. Strongly Disagree")
    print("2. Disagree")
    print("3. Somewhat Disagree")
    print("4. Somewhat Agree")
    print("5. Agree")
    print("6. Strongly Agree")
    return input("\nYour choice: ")

def textBox(text, width=118):
    lines = []
    while len(text) > width:
        space_index = text.rfind(" ", 0, width)
        if space_index == -1:
            lines.append("|" + text[:width] + "|")
            text = text[width:]
        else:
            lines.append("|" + text[:space_index] + " " * (width - space_index) + "|")
            text = text[space_index+1:]
    lines.append("|" + text + " " * (width - len(text)) + "|")
    print("\n+" + "-" * width + "+")
    print("\n".join(lines))
    print("+" + "-" * width + "+")
    return ""
    
def checkSelect(string):
    checkSel = True
    while checkSel == True:
        try:
            num = int(string)
            checkSel = False
            return num
        except ValueError:
            string = input("Invalid selection. Please try again: ")

def printPerc(per_name,perc,checkNull=True):
    if perc > 0 and checkNull==True:
        print(per_name,": ",round(perc*100,2),"%",sep="")
    elif checkNull==False:
        print(per_name,": ",round(perc*100,2),"%",sep="")
        
def printStat(stat_name,stat,over_stat=False):
    if over_stat == False: print(stat_name,": ",stat,sep="")
    else: print(stat_name,": ",over_stat,"/",stat,sep="")

def allocation(vit,str,wis,agi,cha):
    char_alloc = [vit,str,wis,agi,cha]
    
    max_hp = math.trunc(50+((vit * 2) + (str * 1.5) + wis) * 5)
    max_mp = math.trunc(30+((wis * 2) + str + vit) * 6)
    mp_regen = math.trunc(1+wis + (vit/2))

    phy_att = math.trunc(1+(str * 1.5) + vit + agi)
    mag_att = math.trunc(1+(wis * 2) + str + (cha/2))

    phy_def = math.trunc(1+(str * 2) + (vit * 1.2))
    mag_def = math.trunc(1+(wis * 2.5) + vit)

    spd = math.trunc(1+(agi * 2) + (str/2))
    eva = math.trunc(1+(agi  * 1.5) + wis)

    perc = math.trunc(1+(wis * 1.2) + (cha * 1.1))
    acc = math.trunc(1+(wis * 1.1) + agi + (vit/2))

    purs = math.trunc(1+(cha * 2) + (wis * 1.5) + str)
    luck = math.trunc(1+(cha/2) + (wis/3))

    char_alloc.append(max_hp)
    char_alloc.append(max_mp)
    char_alloc.append(mp_regen)
    char_alloc.append(phy_att)
    char_alloc.append(mag_att)
    char_alloc.append(phy_def)
    char_alloc.append(mag_def)
    char_alloc.append(spd)
    char_alloc.append(eva)
    char_alloc.append(perc)
    char_alloc.append(acc)
    char_alloc.append(purs)
    char_alloc.append(luck)
    
    return char_alloc

def checkStats(array,entity="Your",hp=0,mp=0):
    last_ent_char = entity[-1]
    vit = array[0]
    str = array[1]
    wis = array[2]
    agi = array[3]
    cha = array[4]
    
    max_hp = array[5]
    max_mp = array[6]
    mp_regen = array[7]
    phy_att = array[8]
    mag_att = array[9]
    phy_def = array[10]
    mag_def = array[11]
    spd = array[12]
    eva = array[13]
    perc = array[14]
    acc = array[15]
    purs = array[16]
    luck = array[17]
    
    if hp == 0:
        hp = max_hp
    if mp == 0:
        mp = max_mp

    if entity == "Your": print("Your Talent Allocations:")
    elif last_ent_char == "s": print(entity,"' Talent Allocations:")
    else: print(entity,"'s Talent Allocations:")
    
    printStat("Vitality",vit)
    printStat("Strength",str)
    printStat("Wisdom",wis)
    printStat("Agility",agi)
    printStat("Charisma",cha)
    
    print("")
    if entity == "Your": print("Your Stat Values:")
    elif last_ent_char == "s": print(entity,"' Stat Values:")
    else: print(entity,"'s Stat Values:")
    
    printStat("HP",max_hp,over_stat=hp)
    printStat("MP",max_mp,over_stat=mp)
    printStat("MP Regenaration Rate",mp_regen)
    printStat("Physical Attack",phy_att)
    printStat("Magical Attack",mag_att)
    printStat("Physical Defence",phy_def)
    printStat("Magical Defence",mag_def)
    printStat("Speed",spd)
    printStat("Evasion",eva)
    printStat("Perception",perc)
    printStat("Accuracy",acc)
    printStat("Pursuasion",purs)
    printStat("Luck",luck)
    
    
    