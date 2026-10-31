import random
import func

question = [[0 for _ in range(12)] for _ in range(3)]
question[0][0] = "You would love a job that requires you to work alone most of the time."
question[0][1] = "You find the idea of networking or promoting yourself to strangers very daunting."
question[0][2] = "You avoid making phone calls."
question[0][3] = "You enjoy solitary hobbies or activities more than group ones."
question[0][4] = "You usually wait for others to introduce themselves first at social gatherings."
question[0][5] = "You worry about whether you make a good impression on people you meet."
question[0][6] = "You feel more drawn to busy, bustling atmospheres than to quiet, intimate places."
question[0][7] = "You can easily connect with people you have just met."
question[0][8] = "You usually prefer to be around others rather than on your own."
question[0][9] = "You regularly make new friends."
question[0][10] = "You enjoy participating in team-based activities."
question[0][11] = "You feel comfortable just walking up to someone you find interesting and striking up a conversation."
question[1][0] = "You usually base your choices on objective facts rather than emotional impressions."
question[1][1] = "You are not easily swayed by emotional arguments."
question[1][2] = "You prioritize facts over people’s feelings when determining a course of action."
question[1][3] = "You favor efficiency in decisions, even if it means disregarding some emotional aspects."
question[1][4] = "In disagreements, you prioritize proving your point over preserving the feelings of others."
question[1][5] = "You can control your emotions well."
question[1][6] = "You are more likely to rely on emotional intuition than logical reasoning when making a choice."
question[1][7] = "When making decisions, you focus more on how the affected people might feel than on what is most logical or efficient."
question[1][8] = "When facts and feelings conflict, you usually find yourself following your heart."
question[1][9] = "You prioritize being sensitive over being completely honest."
question[1][10] = "People’s stories and emotions speak louder to you than numbers or data."
question[1][11] = "You usually feel more persuaded by what resonates emotionally with you than by factual arguments."
question[2][0] = "You prefer tasks that require you to come up with creative solutions rather than follow concrete steps."
question[2][1] = "Complex and novel ideas excite you more than simple and straightforward ones."
question[2][2] = "You enjoy debating ethical dilemmas."
question[2][3] = "You are drawn to various forms of creative expression, such as writing."
question[2][4] = "You enjoy experimenting with new and untested approaches."
question[2][5] = "You enjoy exploring unfamiliar ideas and viewpoints."
question[2][6] = "You believe that pondering abstract philosophical questions is a waste of time."
question[2][7] = "You are not too interested in discussing theories on what the world could look like in the future."
question[2][8] = "You become bored or lose interest when the discussion gets highly theoretical."
question[2][9] = "You are not too interested in discussions about various interpretations of creative works."
question[2][10] = "You cannot imagine yourself writing fictional stories for a living."
question[2][11] = "You actively seek out new experiences and knowledge areas to explore."

race = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)]
race [0][0][0] = "Dwarf"
race [0][0][1] = "Elf"
race [0][1][0] = "Sigries"
race [0][1][1] = "Giant"
race [1][0][0] = "Herth"
race [1][0][1] = "Velda"
race [1][1][0] = "Human"
race [1][1][1] = "Drazen"

def elemAttr(elem_bias,cont_bias):
    fire = random.random()
    water = random.random()
    earth = random.random()
    wind = random.random()
    
    if elem_bias == "earth":
        earth *= 1.2
        if earth > 1:
            earth = 1
    elif elem_bias == "wind":
        wind *= 1.2
        if wind > 1:
            wind = 1
    elif elem_bias == "water":
        water *= 1.2
        if water > 1:
            water = 1
    elif elem_bias == "fire":
        fire *= 1.2
        if fire > 1:
            fire = 1
    
    sum = fire + water + earth + wind
    
    while sum > 1:
        decrease = (sum-1)/4
        
        fire -= decrease
        water -= decrease
        earth -= decrease
        wind -= decrease
        
        if fire < 0:
            fire = 0
        if water < 0:
            water = 0
        if earth < 0:
            earth = 0
        if wind < 0:
            wind = 0
        
        sum = fire + water + earth + wind
        
    cont_roll = random.random()
    
    if cont_roll < 0.125:
        if cont_bias == "light":
            light = random.random()*random.random()*2
            dark = random.random()*random.random()
            if light > dark:
                light /= 2
                dark = 0
            else: light = 0
        elif cont_bias == "dark":
            dark = random.random()*2
            light = random.random()
            if dark > light:
                dark /= 2
                light = 0
            else: dark = 0
    else:
        light = 0
        dark = 0
    
    quan_roll = random.random()
    
    if quan_roll < 0.00001:
        space = random.random()*random.random()*random.random()*random.random()
        timex = random.random()*random.random()*random.random()*random.random()
    else:
        space = 0
        timex = 0

    return [fire, water, earth, wind, light, dark, space, timex]

def sec_mix_elem(elem_a,elem_b):
    if elem_a <= 0.05 or elem_b <= 0.05:
        x = 0
    elif elem_b - 0.05 <= elem_a <= elem_b + 0.05:
        diff = abs(elem_a - elem_b)
        x = (1 - (20 * diff)) * random.random()
    else: x = 0
    return x
   
def ter_mix_elem(elem_a,elem_b,elem_c):
    if elem_a <= 0.05 or elem_b <= 0.05 or elem_c <= 0.05:
        x = 0
    elif elem_b - 0.05 <= elem_a <= elem_b + 0.05 and elem_c - 0.05 <= elem_b <= elem_c + 0.05 and elem_a - 0.05 <= elem_c <= elem_a + 0.05:
        diff_a = abs(elem_a - elem_b)
        diff_b = abs(elem_b - elem_c)
        diff_c = abs(elem_c - elem_a)
        array = [diff_a,diff_b,diff_c]
        ter_avg = func.arrayAvg(array)
        x = (1 - (20 * ter_avg)) * random.random()
    else: x = 0
    return x
   
def elementalist(elem_a,elem_b,elem_c,elem_d):
    array = [0 for _ in range(6)]
    if elem_a <= 0.05 or elem_b <= 0.05 or elem_c <= 0.05 or elem_d <= 0.05:
        x = 0
    elif elem_b - 0.05 <= elem_a <= elem_b + 0.05 and elem_c - 0.05 <= elem_a <= elem_c + 0.05 and elem_d - 0.05 <= elem_a <= elem_d + 0.05 and elem_c - 0.05 <= elem_b <= elem_c + 0.05 and elem_d - 0.05 <= elem_b <= elem_d + 0.05 and elem_d - 0.05 <= elem_c <= elem_d + 0.05:
        diff_a = abs(elem_a - elem_b)
        diff_b = abs(elem_a - elem_c)
        diff_c = abs(elem_a - elem_d)
        diff_d = abs(elem_b - elem_c)
        diff_e = abs(elem_b - elem_d)
        diff_f = abs(elem_c - elem_d)
        array = [diff_a,diff_b,diff_c,diff_d,diff_e,diff_f]
        lmntlst_avg = func.arrayAvg(array)
        x = (1 - (20 * lmntlst_avg)) * random.random()
    else: x = 0
    return x