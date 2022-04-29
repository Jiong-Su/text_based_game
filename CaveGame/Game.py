import time
import sys
import random
import ascii_art

player_stat = {
    "Name": " ",
    "HP" : 43,
    "Max_Health":43,
    "Defends": 6,
    "Hit_Chance" : 0.7,
    "Attack": 15,
}
bear_stat = {
    "Name" : "Bear",
    "HP" : 20,
    "Max_Health":20,
    "Defends": 5,
    "Hit_Chance" : 0.6,
    "Attack": 15,
}
dragon_stat = {
    "Name": "Dragon",
    "HP" : 60,
    "Max_Health":60,
    "Defends": 10,
    "Hit_Chance" : 0.5,
    "Attack": 20,
}

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
    time.sleep(1)
    ascii_art.print_ascii_art(ascii_art.the_cave)
    time.sleep(1)
    get_player_name()
    delay_print("""
Adventurer, you see a cave in the distance you start to approach it. 
Upon arrival you are greeted with a sign that reads, 'Adventurers enter if you dare'.""",0.05) 
    time.sleep(1)
    ascii_art.print_ascii_art(ascii_art.cave)
    wish_to_enter()

def delay_print(message,delay):
    for c in message:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")   

def get_player_name():
    global player_stat
    delay_print("\nAdventurer, What is your name?",0.05)
    player_name=input()
    player_stat["Name"] = player_name

def wish_to_enter():
    delay_print("""Do you choose to enter?
1).Yes
2).No""" ,0.05)
    try:
        enter = int(input())
    except:
        print("Invalid input, please enter a number.\n")
        wish_to_enter()
        
    if enter == 1:
        delay_print("\nYou are a brave soul! Goodluck adventurer",0.03)
        delay_print("""You enter the cave, you are faced with three tunnels,
Tunnel of Courage, Tunnel of Death, Tunnel of Greed.
Which option would you like to choose? """,0.05)
        cave_entrance()
    elif enter == 2:
        delay_print("Is this you?",0.05)
        time.sleep(1)
        ascii_art.print_ascii_art(ascii_art.chicken)
        game_over()
       
    else:
        wish_to_enter()

def cave_entrance():
    print("""Please choose from the following:
1).Tunnel of Courage
2).Tunnel of Death
3).Tunnel of Greed
""")
    try:
        where_to_go = int(input())
    except:
        print("Invalid input, please enter a number.\n")
    if where_to_go == 1:
        if bear_boss: 
            delay_print("""
As you make your way down the tunnel of courage you see the glisten of what looks like a key, 
as you edge closer to the key you hear an almighty ROAR! and a bear appears.\n""",0.04)
            time.sleep(1)
            ascii_art.print_ascii_art(ascii_art.cute_bear)
        Tunnel_of_Courage()
    elif where_to_go == 2:
        delay_print("Welcome to the Tunnel of Death!!",0.05)
        delay_print("As you enter the tunnel you hear a howl, you proceed with caution...",0.06)
        delay_print("Oh noooo!!! You are ambushed by a pack of wolves!",0.05)
        time.sleep(2)
        ascii_art.print_ascii_art(ascii_art.wolf)
        
        tunnel_of_death()
    elif where_to_go == 3:
        Tunnel_of_Greed()
    else:
        print("Invalid input.")
        cave_entrance()

def random_riddles(): 
    
    auto_gen = random.randint(0,6)
    print(riddles[auto_gen]+"\n")
  
    answer = input().lower()
    if answer.count(riddles_ans[auto_gen]) >= 1:
        return True
    else:
        return False

def Tunnel_of_Courage():
    global bear_boss
    global chest_key
    global player_stat
    global bear_stat
    if bear_boss: 
        delay_print("Do you wish to fight the bear or attempt to escape?",0.05)
        print("1).Fight \n2).Escape")
        try:
            fight_or_not = int(input())
        except:
            print("Invalid input, please enter a number.\n")
            fight_or_not = int(input())
        
        if fight_or_not ==1:
            time.sleep(1)
            ascii_art.print_ascii_art(ascii_art.angry_bear)
            time.sleep(1)
            ascii_art.print_ascii_art(ascii_art.bear_bear)
            print("The Bear is very angry and is ready to fight. Press enter to begin the fight.\n")
            input()
            counter=1
            
            while player_stat["HP"]>0 and bear_stat["HP"]>0:
                combat_turn(bear_stat,counter)
                
                if player_stat["HP"]<=0:
                    delay_print("you have been deafeated by Bear",0.1)
                    game_over()
                elif bear_stat["HP"]<=0:
                    delay_print("you have defeated the bear", 0.1)
                    time.sleep(0.5)
                    ascii_art.print_ascii_art(ascii_art.bear_ko)
                    delay_print("You have obtained a key and recoved to full health.",0.1)
                    time.sleep(2)
                    ascii_art.print_ascii_art(ascii_art.key)
                    delay_print("You have obtained a sword. Your attack incresed by 20" ,0.1)
                    time.sleep(2)
                    player_stat["HP"]=player_stat["Max_Health"]
                    ascii_art.print_ascii_art(ascii_art.sword)
                    player_stat["Attack"]+=20
                    chest_key=True
                    bear_boss=False
                    time.sleep(2)
                    delay_print("You have returned to the entrance",0.05)
                    cave_entrance()
                counter+=1
                            
        elif fight_or_not == 2:
            
            escape=random_riddles()
            if escape==True:
                delay_print("You've recovered back to full health",0.05)
                player_stat["HP"]=player_stat["Max_Health"]
                cave_entrance()
            else:
                delay_print("Failed to escape, you loose 5HP.\n",0.05)
                player_stat["HP"]-=5
                fight_or_not=1   
        else:
            print("Invalid input.\n")
            Tunnel_of_Courage()
    else:
        delay_print("The bear has been defeated, there is nothing is the room.",0.05)
        delay_print("Return to the entrance.",0.05)
        cave_entrance()

def tunnel_of_death():
    delay_print("Do you wish to stay and fight the wolves? " ,0.05)
    print("1).Fight the wolves\n2).Attempt to escape.")
    try:
        fight_wolves = int(input())
    except:
        print("Invalid input, please enter a number.\n")
        tunnel_of_death ()
   
    if fight_wolves == 1:
        delay_print("Game over!" + " " + "RIP my friend!" + " " "You have lost the battle! ",0.05)
        game_over()     
    elif fight_wolves == 2:
        delay_print("\nAnswer the following riddle for you to escape from the pack of wolves",0.05)
        answer =random_riddles()
        if answer == True:
            delay_print("\nYou've barely escaped the wolves ",0.05)
            delay_print("You are back to the entrance.",0.05)
            cave_entrance()
        else:
            delay_print("\nGame over!"+" " + "RIP my friend!" + " " "You have lost the battle!",0.05)
            time.sleep(1.5)
            game_over()
    else:
        print("Invalid command, please try again.\n")
        tunnel_of_death()

def Tunnel_of_Greed():
    global chest_key
   
    if chest_key: 
        delay_print("""
The third and final tunnel as you approach you hear the snoring of something mighty! 
The closer you get you start to see a shape resembling a DRAGON!!! 
you tremble with fear, as you try to hide you see a shiny gold chest hidden behind the sleeping dragon.
The greed consumes you, you can't help but think that the key you obtained earlier could unlock this chest! 
You approach cautiously and insert the key into the locked chest, as you turn the key you hear a clank IT WORKS! 
You open the chest and see enough treasure to last a life time!!!
But wait! OH NO!""",0.05) 

        ascii_art.print_ascii_art(ascii_art.dragon_stare)
        delay_print("Please press enter to continue.",0.05)
        input()
        ascii_art.print_ascii_art(ascii_art.dragon)
        delay_print("The dragon has awoke from its slumber!", 0.05)
        delay_print("You see his eyes glow with the colour of fire, as his mouth opens wide you can feel the heat of the flames and with an almight roar the flames attempt to consume you! ",0.05)
        delay_print("Dodge you roll out the way of the flames and attempt to counter with a strike of your own lowering the dragons HP",0.05)
        delay_print("Press enter to begin the fight. ",0.05)
        input()
        counter=1
        global player_stat
        global dragon_stat
        while player_stat["HP"]>0 and dragon_stat["HP"]>0:
            combat_turn(dragon_stat,counter)
        
            if player_stat["HP"]<=0:
                delay_print("The dragon attacks again although wounded it still manages to spit fire!", 0.05)
                delay_print("Faildodge you are engulfed in the flames resulting in death! GAME OVER!",0.05)
                game_over()
            elif dragon_stat["HP"]<=0:
                delay_print("The dragon attacks again although wounded it still manages to spit fire!", 0.05)
                delay_print("You dodge again and are able to deliver the killing blow!", 0.05)
                delay_print("VICTORY You have slain the dragon and can now bask in the chest of treasures awaiting you!",0.05)
                ascii_art.print_ascii_art(ascii_art.thank_you)
            counter+=1
            time.sleep(1)
    else:
        delay_print("You do not have the key, please obtain it and then return to this room.",0.05)
        delay_print("Returned to the entrance", 0.05)
        cave_entrance()

def combat_turn(enemy,counter):
    Counter=counter
    name=enemy["Name"]
    player_name=player_stat["Name"]
    if Counter%2 == 0:
        delay_print(f"Turn {Counter}, it the {name}'s turn.",0.07)
        time.sleep(1)
        attack(enemy,player_stat)
    else:
        delay_print(f"Turn {Counter},it {player_name}'s turn.",0.07)
        time.sleep(1)
        combat(enemy)

def combat(target):
    try:
        action =int(input("Please choose from the following action:\n\n1:Attack, 2:Escape, 3:Stat\n"))
    except:
        print("Invalid input, please enter a number.\n")
        combat(target)

    if action == 1:
        attack(player_stat,target)
    elif action == 2:
        delay_print("Answer the following riddle for you to escape.",0.05)
        if random_riddles()==True:
            delay_print("Corret!!! You escape back to the entrance.",0.05)
            delay_print("You recoved back to full health",0.05)
            player_stat["HP"]=player_stat["Max_Health"]
            target["HP"]=target["Max_Health"]
            cave_entrance()
        else:
            delay_print("Failed to escape, you loose 5HP.\n",0.05)
            player_stat["HP"]-=5

    elif action == 3:
        check_stat(player_stat)
        check_stat(target)
        print("\n")
        combat(target)
    else:
        print("Invalid input please try again.\n")
        combat(target)

def attack(attacker,defender):
    global player_stat
    global bear_stat
    global dragon_stat
    delay_print(attacker["Name"]+" decided to attack.",0.06)
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
        time.sleep(1)
        print("Successfull hit, {} have {} Attack and {} have {} Defends, {} -{}HP".format(attacker["Name"],attacker["Attack"],defender["Name"],defender["Defends"],defender["Name"],damage))
        print(defender["Name"]+" current health is " + str(defender["HP"]) + "/"+str(defender["Max_Health"]) + "\n")
    else:
        delay_print("Attack missed",0.06)

def check_stat(t):
    print("Name: {}, HP:{}/{}, Defends : {}, Hit Chance: {}%, Attack: {}".format(t["Name"],t["HP"],t["Max_Health"],t["Defends"],t["Hit_Chance"]*100,t["Attack"]))

def game_over():
    global chest_key
    global bear_stat
    global bear_boss
    global dragon_stat 
    global player_stat
    ascii_art.print_ascii_art(ascii_art.game_over)
    delay_print("\nDo you want to play again? Y/N",0.1)
    if input().lower()=="y":
        bear_stat["HP"]=bear_stat["Max_Health"]
        dragon_stat["HP"]=dragon_stat["Max_Health"]
        player_stat["HP"]=player_stat["Max_Health"]
        player_stat["Attack"]-=20
        chest_key=False
        bear_boss=True
        start()
            
    else:
        quit()
            

start()

# wish_to_enter()
# # print line, 2 speed 
# random_riddles()
# Tunnel_of_Courage()
# tunnel_of_death()
# chest_key=True
# Tunnel_of_Greed()
     