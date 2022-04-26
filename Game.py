import time
import sys
import random
import ascii_art

player_stat = {
    "Name": " ",
    "HP" : 50,
    "Defends": 6,
    "Hit_Chance" : 0.7,
    "Attack": 15,
}

bear_stat = {
    "Name" : "Bear",
    "HP" : 20,
    "Defends": 5,
    "Hit_Chance" : 0.6,
    "Attack": 10,
}

dragon_stat = {
    "Name": "Dragon",
    "HP" : 40,
    "Defends": 10,
    "Hit_Chance" : 0.5,
    "Attack": 20,
}
auto_gen = random.randint(0,6)
riddles = ["I shave every day, but my beard stays the same. What am I?",
"I have branches, but no fruit, trunk or leaves. What am I?", "What gets wet while drying?",
"The more of this there is, the less you see. What is it?", 
"What cannot talk but will reply when spoken to?", 
"What can you break, even if you never pick it up or touch it?", 
"What goes up but never comes down?"]
riddles_ans = ["barber", "bank", "towel", "darkness", "echo", "promise", "age"]
bear_boss=True
chest_key=False

def start():
    get_player_name()
    wish_to_enter()

def delay_print(message,delay):
    for c in message:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")   

def get_player_name():
    global player_stat
    delay_print("\nAdventurer,What is your name?",0.02)
    player_name=input()
    player_stat["Name"] = player_name

def wish_to_enter():
    # delay_print(player_stat["Name"])
    delay_print("""
, you see a cave in the distance you start to approach it. 
Upon arrival you are greeted with a sign that reads, Adventurers enter if you dare. 
Do you choose to enter? please enter 'Yes' or 'No' """ ,0.02)
    enter = input().lower()
    if enter == "yes":
        delay_print("\nYou are a brave soul! Goodluck adventurer",0.03)
        delay_print("""You enter the cave, you are faced with three tunnels,
Tunnel of Courage, Tunnel of Death, Tunnel of Greed.
Which option would you like to choose? """,0.03)
        cave_entrance()
    elif enter == "no":
        delay_print("I this you?",0.05)
        time.sleep(1)
        ascii_art.print_ascii_art(ascii_art.chicken) 
    else:
        start()
           
def cave_entrance():
    delay_print("Please enter '1' for Tunnel of Courage', '2' for Tunnel of Death' or '3' for Tunnel of Greed. ",0.02)
    try:
        where_to_go = int(input())
    except:
        print("Invalid input.")
    
    if where_to_go == 1:
        left_room()
    elif where_to_go == 2:
        delay_print("Welcome to the Tunnel of Death!!\n",0.02)
        delay_print("As you enter the tunnel you hear a howl, you proceed with caution...\n",0.07)
        delay_print("Oh noooo!!! You are ambushed by a pack of wolves!\n",0.02)
        time.sleep(0.2)
        delay_print("Do you wish to stay and fight the wolves? Yes or No? " ,0.02)
        death_tunnel()
    elif where_to_go == 3:
        right_room()
    else:
        print("Invalid input.")
        cave_entrance()

def random_riddles(): 
    print(riddles[auto_gen])
    answer = input().lower()
    if answer.count(riddles_ans[auto_gen]) >= 1:
        return True
    else:
        return False
    
def left_room():
    global bear_boss
    global chest_key
   
    if bear_boss: 
        delay_print("""
As you make your way down the tunnel of courage you see the glisten of what looks like a key, 
as you edge closer to the key you hear an almighty RAW! and a bear appears.\n""",0.03)
        ascii_art.print_ascii_art(ascii_art.cute_bear)
        delay_print("Do you wish to fight the bear?" "\n \nEnter 'Yes' to engage combat or 'No' to return to previous room. ",0.02)
        fight_or_not = input().lower()
        if fight_or_not =="yes":
            time.sleep(1)
            ascii_art.print_ascii_art(ascii_art.angry_bear)
            time.sleep(1)
            ascii_art.print_ascii_art(ascii_art.bear_bear)
            print("Bear is ready to fight.\n")
            counter=1
            global player_stat
            global bear_stat
            while player_stat["HP"]>0 and bear_stat["HP"]>0:
                combat_turn(bear_stat,counter)
                print(player_stat["HP"], bear_stat["HP"])
                if player_stat["HP"]<=0:
                    delay_print("you have been deafeated by Bear",0.03)
                    #game_over()
                elif bear_stat["HP"]<=0:
                    delay_print("you have defeated the bear", 0.03)
                    print("\n")
                    delay_print("You have obtained a key",0.03)
                    chest_key=True
                    bear_boss=False
                counter+=1
            delay_print("you have returned to the entrance",0.03)
            cave_entrance()
        elif fight_or_not == "no":
            
            if random_riddles()==True:
                delay_print("Corret!!! You escape back to the entrance.")
                cave_entrance()
            else:
                delay_print("Failed to escape, you loose 5HP.\n",0.03)
                player_stat["HP"]-=5
            fight_or_not="yes"   
        else:
            print("Invalid input.\nEnter 'Yes' to engage combat or 'No' to return to previous room.\n")
            left_room()
    else:
        delay_print("The bear has been defeated, there is nothing is the room.\n",0.02)
        print("\n")
        delay_print("Return to the entrance",0.02)
        cave_entrance()

def death_tunnel ():
    
    fight_wolves = (input()).capitalize()
    if fight_wolves == "Yes":
        delay_print("Game over!" + " " + "RIP my friend!" + " " "You have lost the battle! ",0.02)     
    elif fight_wolves == "No":
        answer =random_riddles()
        if answer == True:
            delay_print("You've barely escaped the wolves ",0.02)
            print("\n")
            delay_print("you are back to the entrance.",0.02)
            cave_entrance()
        else:
            delay_print("Game over!"+" " + "RIP my friend!" + " " "You have lost the battle!",0.02)
    else:
        print("Invalid command, please try again.")
        death_tunnel()

def right_room():
    global chest_key
   
    if chest_key: 
        delay_print("""
The third and final tunnel as you approach you hear the snoring of something mighty! 
The closer you get you start to see a shape resembling a DRAGON!!! 
you tremble with fear, as you try to hide you see a shiny gold chest hidden behind the sleeping dragon.
The greed consumes you, you can't help but think that the key you obtained earlier could unlock this chest! 
You approach cautiously and insert the key into the locked chest, as you turn the key you hear a clank IT WORKS! 
You open the chest and see enough treasure to last a life time!!!
But wait! OH NO!""",0.04) 

        ascii_art.print_ascii_art(ascii_art.dragon_stare)
        delay_print("the dragon has awoke from its slumber!", 0.05)
        
        delay_print("Do you wish to fight the dragon?" "\n \nEnter 'Yes' to engage combat or 'No' to return to previous room. ",0.04)
        fight_or_not = input().lower()
        if fight_or_not =="yes":
            counter=1
            global player_stat
            global dragon_stat
            while player_stat["HP"]>0 and dragon_stat["HP"]>0:
                combat_turn(dragon_stat,counter)
                print(player_stat["HP"], dragon_stat["HP"])
                if player_stat["HP"]<=0:
                    delay_print("you have been deafeated by dragon",0.02)
                    #game_over()
                elif dragon_stat["HP"]<=0:
                    delay_print("you have slain the dragon, Claim your treasure well done!",0.02)
                    chest_key=False
                counter+=1
        elif fight_or_not == "no":
            delay_print("you are back to the entrance.",0.02)
            cave_entrance()
        else:
            print("Invalid input.\nEnter 'Yes' to engage combat or 'No' to return to previous room.\n")
            left_room()
    else:
        delay_print("""
You do not have the key, please obtain it and then return to this room.
Return to the entrance
""",0.02)
        cave_entrance()

def combat_turn(enemy,counter):
    Counter=counter
    name=enemy["Name"]
    player_name=player_stat["Name"]
    if Counter%2 == 0:
        delay_print(f"turn {Counter},it the {name}'s turn.\n",0.02)
        attack(enemy,player_stat)
    else:
        delay_print(f"turn {Counter},it {player_name}'s turn.\n",0.02)
        combat(enemy)

def combat(tt):
    try:    
        action =int(input("1:Attack, 2:Escape, 3:Stat"))
    except:
        print("Invalid input please try again.\n")
        combat(tt)
    if action == 1:
        attack(player_stat,tt)
    elif action == 2:
        escape()
    elif action == 3:
        check_stat(player_stat)
        check_stat(tt)
        combat(tt)
    else:
        print("Invalid input please try again.\n")
        combat(tt)

def attack(attacker,defender):
    
    global player_stat
    global bear_stat
    global dragon_stat
    delay_print(attacker["Name"]+" decided to attack.",0.03)
    hit_roll = random.randint(1,10)
    
    if attacker["Name"]==player_stat["Name"]:
        if defender["Name"]==bear_stat["Name"]:
            bear_stat=defender
            player_stat=attacker
        else:
            dragon_stat=defender
            player_stat=attacker
        
    elif attacker["Name"]==bear_stat["Name"]:
        bear_stat=attacker
        player_stat=defender
    else:
        dragon_stat=attacker
        player_stat=defender
        
    if hit_roll <=(attacker["Hit_Chance"])*10: 
        damage=attacker["Attack"]-defender["Defends"]
        defender["HP"]-=damage
        print("Successfull hit, {} have {} Attack and {} have {} Defends, {} -{}HP".format(attacker["Name"],attacker["Attack"],defender["Name"],defender["Defends"],defender["Name"],damage))
    else:
        print("Attack missed")
        
def escape():
    delay_print("\nAnswer the following riddle for you to escape.",0.02)
    delay_print("\n What is full of holes but still holds water? \n",0.02)
    riddle = input().lower()

    if riddle.count("sponge")>=1:
        delay_print("Corret!!! You've barely escaped.",0.02)
        delay_print("you are back to the entrance.",0.02)
        cave_entrance()
    else:
        delay_print("Wrong answer! You failed to escape.",0.02)

def check_stat(t):
    print("Name: {}, HP:{}, Defends : {}, Hit Chance: {}%, Attack: {}".format(t["Name"],t["HP"],t["Defends"],t["Hit_Chance"]*100,t["Attack"]))

start()








    
    



