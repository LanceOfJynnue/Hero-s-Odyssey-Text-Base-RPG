from pathlib import Path
import json
import random
import sys
import func
import char_create
import subprocess
import dir

func.textBox("Greetings, O wandering soul. Thou hast entered the world of Jynnue; A place of magic, adventure, and mystery. In this world, thou will encounter many challenges and obstacles, but thou shall not fear, for thou are destined for greatness. First, thou must answer a few questions that let's me know what kind of adventurer thou are. Are thou ready to begin?",100)

input("\nPress ENTER to continue.")

int_ext = [0 for _ in range(6)]
log_emo = [0 for _ in range(6)]
intu_sens = [0 for _ in range(6)]

q_num = 1
x = 0
inex = func.arrayRand(1, 12, 6)
loem = func.arrayRand(1, 12, 6)
inse = func.arrayRand(1, 12, 6)

for h in range(3):
    for i in range(6):
        func.clear_terminal()
        if h == 0:
            x = inex[i]-1
        elif h == 1:
            x = loem[i]-1
        elif h == 2:
            x = inse[i]-1
        print(q_num,".",char_create.question[h][x],sep="")
        q_num += 1
        choice = func.questionChoices()
        check = False
        
        while check==False:
            if func.isDigit(choice):
                choice = int(choice)
                if choice >= 1 and choice <= 6:
                    check=True
                else:
                    choice = input("\nPlease select a valid choice: ")
            else:
                choice = input("\nPlease select a valid choice: ")
        
        if x >= 6 and x <= 11:
            if choice == 1:
                choice = 3
            elif choice == 2:
                choice = 2
            elif choice == 3:
                choice = 1
            elif choice == 4:
                choice = -1
            elif choice == 5:
                choice = -2
            elif choice == 6:
                choice = -3
        else:
            if choice == 1:
                choice = -3
            elif choice == 2:
                choice = -2
            elif choice == 3:
                choice = -1
            elif choice == 4:
                choice = 1
            elif choice == 5:
                choice = 2
            elif choice == 6:
                choice = 3

        if h == 0:
            int_ext[i] = choice
        elif h == 1:
            log_emo[i] = choice
        elif h == 2:
            intu_sens[i] = choice
    
int_ext_sum = func.arraySum(int_ext)
log_emo_sum = func.arraySum(log_emo)
intu_sens_sum = func.arraySum(intu_sens)

while int_ext_sum==0:
    int_ext_sum = random.randint(-1,1)
while log_emo_sum==0:
    log_emo_sum = random.randint(-1,1)
while intu_sens_sum==0:
    intu_sens_sum = random.randint(-1,1)

if int_ext_sum < 0:
    x=0
elif int_ext_sum > 0:
    x=1
    
if log_emo_sum < 0:
    y=0
elif log_emo_sum > 0:
    y=1

if intu_sens_sum < 0:
    z=0
elif intu_sens_sum > 0:
    z=1

func.clear_terminal()

race = char_create.race[x][y][z]

func.textBox("Thy hast done well in answering these questions. In this moment, I implore what name shall thou be addressed.",100)
char_name = input("\nThy name is: ")
file_name = char_name+".json"
file_path = Path(dir.parent_dir+"/character/"+file_name)

while True:
    if file_path.is_file():
        char_name = input("\nThis name has already been taken. Please provide me a different one: ")
        file_name = char_name+".json"
        file_path = Path(dir.parent_dir+"/character/"+file_name)
    elif char_name == "":
        char_name = input("\nThy had not given any name. Please let me know thy name: ")
        file_name = char_name+".json"
        file_path = Path(dir.parent_dir+"/character/"+file_name)
    elif func.isDigit(char_name[0]):
        char_name = input("\nThe first character of thy name cannot be a digit. Please provide me a different one: ")
        file_name = char_name+".json"
        file_path = Path(dir.parent_dir+"/character/"+file_name)
    else: break

# WILL ADD NAME EASTER EGGS HERE #
func.textBox(char_name+"... Well then, this world shall know the name of "+char_name+".")

####

input("\nPress ENTER to continue.")
func.clear_terminal()

func.textBox("Now, let me tell thee about the vessel you'll have within this realm. In this world, there are 8 intellectual races created as caretakers of it and govern over it. Among these races, thou vessel is from the race of "+race+".")

input("\nPress ENTER to continue.")
func.clear_terminal()

if race == "Dwarf":
    func.textBox("Thy race is of the small stature, comparable to half of the average size of the other races, excluding the Giants. This race specializes in technological knowledge, and is known for their thirst for advancement, specially as a whole race. Almost all dwarves currently resides within their underground nation called 'Blackreach', living in seclusion; away from the rest of the world. They are mostly arrogant, short-tempered, but quick-witted, and skillful in their crafts.")
    elem_bias = "earth"
    cont_bias = "dark"
    vit = 2
    str = 3
    wis = 3
    agi = 1
    cha = 1
elif race == "Elf":
    func.textBox("Thy race is known for their pointy ears, fair and pale skin, and regarded by the race of humans for having peerless beauty as a whole. This race specializes in botany and archery, and has high affinity with the nature. Most elves prefer to live and build their community within forests, where there is an abundance of vegetation. They are mostly quiet, reserved, and observant, and strict when it comes to the laws they have.")
    elem_bias = "wind"
    cont_bias = "light"
    vit = 0
    str = 1
    wis = 2
    agi = 4
    cha = 3
elif race == "Sigries":
    func.textBox("Thy race is known for their cerulean skin, gills by their neck, limbs with fins and flaps, and their ability to live and breathe both underwater and in land. Many sigries live underwater, mostly within the kingdom of Akurim, with a few living as adventurers on land. This race specializes in alchemy and sorceric item creation. They are mostly selfish, territorial, but also intelligent and resourceful.")
    elem_bias = "water"
    cont_bias = "dark"
    vit = 1
    str = 1
    wis = 3
    agi = 3
    cha = 2
elif race == "Giant":
    func.textBox("Thy race is of the larger stature, almost twice the size of the average height of the other races, except the dwarves. They are known of having two horns on the sides of their heads, as well as for having a tougher physical body. They can alter their size to that of the common height, however, it does consume mana, reason why only a few does it on a regular basis. They prefer to live on higher lands, such as hills and mountains. They are mostly kind, helpful, and hospitable.")
    elem_bias = "earth"
    cont_bias = "dark"
    vit = 4
    str = 3
    wis = 1
    agi = 0
    cha = 2
elif race == "Herth":
    func.textBox("Thy race is known for their pale scarlet skin, having 1 or 2 horns in their forehead. They specialize in sorcery, and most is fond of researching a variety of topics and theories. They inhabit the underworld, however, many also travels and live on the overworld. They are mostly mischievous, crafty, lustful, and known for their unpredictability.")
    elem_bias = "fire"
    cont_bias = "light"
    vit = 0
    str = 1
    wis = 4
    agi = 2
    cha = 3
elif race == "Velda":
    func.textBox("Thy race is recognized by their angel-like wings, and having white hair, regardless of having light affinity or not. Due to some historical events and their capability to fly, they are tasked by their ancestors to inhabit and cultivate the islands that hovers in the sky all over the world. They specialize in socializing and known for being the most friendly race. They are mostly kind, patient, and caring.")
    elem_bias = "wind"
    cont_bias = "light"
    vit = 2
    str = 0
    wis = 1
    agi = 3
    cha = 4
elif race == "Human":
    func.textBox("Thy race is the most commonly known and highest in population. Knowing thy place of origins; and yes, I am indeed talking about thy world in which you hailed from, I do not think I need to expound more regarding what a human is. All I can say about this race in comparison to the other race is that plentiful of them are brave, determined, and highly curious about anything and everything.")
    elem_bias = "water"
    cont_bias = "dark"
    vit = 2
    str = 2
    wis = 2
    agi = 2
    cha = 2
elif race == "Drazen":
    func.textBox("Thy race is known for having the characteristics of both beasts and bi-pedal creatures, mainly comparable to humans. There are some that are full breeds, which are mostly covered in fur, and there are half-breeds that have more human-like features. The common hybrids of Drazens are feline, canine, and bear-like. They specialize in close-up battles with their raw strength. They are mostly rowdy, barbaric, and agile.")
    elem_bias = "fire"
    cont_bias = "light"
    vit = 2
    str = 4
    wis = 0
    agi = 3
    cha = 1

input("\nPress ENTER to continue.")
func.clear_terminal()

elem_attr = char_create.elemAttr(elem_bias,cont_bias)
fire = elem_attr[0]
water = elem_attr[1]
earth = elem_attr[2]
wind = elem_attr[3]
light = elem_attr[4]
dark = elem_attr[5]
space = elem_attr[6]
timex = elem_attr[7]

lightning = char_create.sec_mix_elem(fire, water)
smoke = char_create.sec_mix_elem(fire, wind)
metal = char_create.sec_mix_elem(fire, earth)
plant = char_create.sec_mix_elem(water, earth)
ice = char_create.sec_mix_elem(water, wind)
sand = char_create.sec_mix_elem(wind, earth)

storm = char_create.ter_mix_elem(fire, water, wind)
meteor  = char_create.ter_mix_elem(fire, wind, earth)
crystal = char_create.ter_mix_elem(fire, water, earth)
beasts = char_create.ter_mix_elem(water, wind, earth)

elementals = char_create.elementalist(fire, water, wind, earth)

sun = char_create.sec_mix_elem(light, fire)
rainbow = char_create.sec_mix_elem(light, water)
music = char_create.sec_mix_elem(light, wind)
stardust = char_create.sec_mix_elem(light, earth)

blackFlame = char_create.sec_mix_elem(dark, fire)
toxic = char_create.sec_mix_elem(dark, water)
void = char_create.sec_mix_elem(dark, wind)
moon = char_create.sec_mix_elem(dark, earth)

print("Your elemental attribute is:")
func.printPerc("Fire",fire)
func.printPerc("Water",water)
func.printPerc("Earth",earth)
func.printPerc("Wind",wind)

func.printPerc("Lightning",lightning)
func.printPerc("Smoke",smoke)
func.printPerc("Metal",metal)
func.printPerc("Plant",plant)
func.printPerc("Ice",ice)
func.printPerc("Sand",sand)

func.printPerc("Storm",storm)
func.printPerc("Meteor",meteor)
func.printPerc("Crystal",crystal)
func.printPerc("Beasts",beasts)

func.printPerc("Elementals",elementals)

func.printPerc("Light",light)
func.printPerc("Dark",dark)

func.printPerc("Sun",sun)
func.printPerc("Rainbow",rainbow)
func.printPerc("Music",music)
func.printPerc("Stardust",stardust)

func.printPerc("Black Flame",blackFlame)
func.printPerc("Toxic",toxic)
func.printPerc("Void",void)
func.printPerc("Moon",moon)

func.printPerc("Space",space)
func.printPerc("Time",timex)

skills = {}
    
def elem_skill(elem, elem_perc):
    global skills
    if elem_perc >= 0.1:
        skills[elem+"_affinity"] = 1

elem_skill("fire", fire)
elem_skill("water", water)
elem_skill("earth", earth)
elem_skill("wind", wind)
elem_skill("lightning", lightning)
elem_skill("smoke", smoke)
elem_skill("metal", metal)
elem_skill("plant", plant)
elem_skill("ice", ice)
elem_skill("sand", sand)
elem_skill("storm", storm)
elem_skill("meteor", meteor)
elem_skill("crystal", crystal)
elem_skill("beasts", beasts)
elem_skill("light", light)
elem_skill("dark", dark)
elem_skill("sun", sun)
elem_skill("rainbow", rainbow)
elem_skill("music", music)
elem_skill("stardust", stardust)
elem_skill("blackFlame", blackFlame)
elem_skill("toxic", toxic)
elem_skill("void", void)
elem_skill("moon", moon)
elem_skill("space", space)
elem_skill("timex", timex)

input("\nPress ENTER to continue.")
func.clear_terminal()

char_alloc = func.allocation(vit,str,wis,agi,cha)
func.checkStats(char_alloc)

input("\nPress ENTER to continue.")
func.clear_terminal()

character = {
    "name": char_name,
    "race": race,
    "cur_hp": char_alloc[5],
    "cur_mp": char_alloc[6],
    "lvl": 1,
    "xp": 0,
    "gold": 0,
    "talent_points": 5,
    "coordinate": [0, 0],
    "attributes": {
        "fire": fire,
        "water": water,
        "earth": earth,
        "wind": wind,
        "lightning": lightning,
        "smoke": smoke,
        "metal": metal,
        "plant": plant,
        "ice": ice,
        "sand": sand,
        "storm": storm,
        "meteor": meteor,
        "crystal": crystal,
        "beasts": beasts,
        "elementals": elementals,
        "light": light,
        "dark": dark,
        "sun": sun,
        "rainbow": rainbow,
        "music": music,
        "stardust": stardust,
        "blackFlame": blackFlame,
        "toxic": toxic,
        "void": void,
        "moon": moon,
        "space": space,
        "timex": timex
    },
    "base_talents": {
        "vit": char_alloc[0],
        "str": char_alloc[1],
        "wis": char_alloc[2],
        "agi": char_alloc[3],
        "cha": char_alloc[4]
    },
    "base_stats": {
        "max_hp": char_alloc[5],
        "cur_mp": char_alloc[6],
        "max_mp": char_alloc[6],
        "mp_regen": char_alloc[7],
        "phy_att": char_alloc[8],
        "mag_att": char_alloc[9],
        "phy_def": char_alloc[10],
        "mag_def": char_alloc[11],
        "spd": char_alloc[12],
        "eva": char_alloc[13],
        "perc": char_alloc[14],
        "acc": char_alloc[15],
        "purs": char_alloc[16],
        "luck": char_alloc[17]
    },
    "skills": skills,
    "tags": []
}

# 2. Open a new file in write mode ("w") and dump the data
with open(dir.parent_dir+"/character/"+file_name, "w", encoding="utf-8") as json_file:
    json.dump(character, json_file, indent=4)

subprocess.run(["python", dir.parent_dir+"/misc/gameplay.py",file_name])
sys.exit()
