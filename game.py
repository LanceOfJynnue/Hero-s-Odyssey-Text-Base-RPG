import sys
import misc.func
import misc.dir
import json
from pathlib import Path
import subprocess


playing = True

while playing == True:
    misc.func.textBox("HERO'S ODYSSEY",100)
    print("Enter the number of your choice:")
    print("1. New Game")
    print("2. Continue")
    print("3. Settings")
    print("4. Exit Game")

    menu_inp = input("\nSelect: ")
    check = False

    while check==False:
        if misc.func.isDigit(menu_inp):
            menu_inp = int(menu_inp)
            if menu_inp >= 1 and menu_inp <= 4:
                check=True
            else:
                menu_inp = int(input("\nPlease select a valid choice: "))
        else:
            menu_inp = int(input("\nPlease select a valid choice: "))

    if menu_inp == 1:
        misc.func.clear_terminal()
        subprocess.run(["python", misc.dir.parent_dir+"/misc/intro.py"])
    elif menu_inp == 2:
        misc.func.clear_terminal()
        directory = Path(misc.dir.parent_dir+"/character")
        json_files = list(directory.glob("*.json"))
        i = 0

        if json_files:
            save_array = False
            print(f"Found {len(json_files)} save file(s):")
            for file in json_files:
                i += 1
                # Open and load the JSON file
                with open(misc.dir.parent_dir+f"/character/{file.name}", 'r') as filex:
                    data = json.load(filex)
                    namex = data['name']
                    namex.strip("\'")
                    race = data['race']
                    race.strip("\'")
                    lvl = data['lvl']
                    
                print(i,". ",namex," || Race: ",race," || Level: ",lvl,sep="")
                if save_array == False:
                    save_array = [namex]
                else: save_array.append(namex)
            i += 1
            print("\n",i,". RETURN TO MENU",sep="")
            selectCont = misc.func.checkSelect(input("\nSelect and enter the number of your choice: "))
            
            while True:
                if selectCont == i:
                    misc.func.clear_terminal()
                    break
                elif 0 < selectCont < i: 
                    misc.func.clear_terminal()
                    subprocess.run(["python", misc.dir.parent_dir+"/misc/gameplay.py",save_array[selectCont-1]])
                else: selectCont = input("\nInvalid choice, please try again: ")
        else:
            print("No save files found.")
            input("Press ENTER to go back to the menu")
            misc.func.clear_terminal()
    elif menu_inp == 3:
        misc.func.clear_terminal()
        print("Meow")
        input("Press ENTER to contine")
        misc.func.clear_terminal()
    elif menu_inp == 4:
        misc.func.clear_terminal()
        playing = False
        sys.exit()

