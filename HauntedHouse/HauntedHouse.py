import random
import time

key1 = False
key2 = False
fusebox = False
sword = False

playerHP = 10
playerDamageMultiplier = 3


def hallway():
    print("---HALLWAY---")
    print("You are in the hallway, a grand room. As you look around you see paintings and delicate ornaments. There are three exits​,")

    valid = False
    
    global key1
    global fusebox

    while valid == False:
        direction = input("Theres door North and South. Input either N or S to choose your direction")
        if direction.upper() == "N":
            valid = True
            bottomBedroom()
        elif direction.upper() == "S":
               valid = True
               livingRoom()
        elif direction.upper() == ("TEST"):
            print("Loading second floor...")
            fusebox = True
            key1 = True
            hallway2()
        elif direction.upper() == ("BATTLE TEST"):
            grandBedroom()
        else:
            print("You cant do that")

def bottomBedroom():
    print("---BOTTOM BEDROOM---")
    print("You enter a musty bedroom with peeling wallpaper and mouldy corners")

    valid = False

    while valid == False:
        direction = input("Theres door West and South. Input either W or S to choose your direction")
        if direction.upper() == "W":
            valid = True
            kitchen()
        elif direction.upper() == "S":
              valid = True
              hallway()
        else:
            print("You cant do that")


def kitchen():
    print("---KITCHEN---")
    print("Plates are smashed across the floor imitate a domestic minefield. Theres a door to what appears to be a closet. It appears to be locked (REQUIRES KEY FOUND ON FIRST FLOOR)")


    valid = False

    while valid == False:
        direction = input("Theres door West, East and South. Input either W,S or E to choose your direction")
        if direction.upper() == "W" and key1 == True:
            valid = True
            utilityCloset()
        elif direction.upper() == "W" and key1 == False:
            print("The door to the west is locked youll need a key from this floor")
        elif direction.upper() == "W" and fusebox == True:
            print("There was nothing other then the fusebox in there. Theres no point going back in")
        elif direction.upper() == "S":
              grandHall()
              valid = True
        elif direction.upper() == "E":
            valid = True
            bottomBedroom()
        else:
            print("You cant do that")


def grandHall():
    print("---GRAND HALL---")
    print("A large room looms over you. Building supplies are scattered all across it and all but two doors are covered by planks")


    valid = False

    while valid == False:
        direction = input("Theres doors West and North. Input either W or N to choose your direction")
        if direction.upper() == "W":
            valid = True
            wineCellar()
            
        elif direction.upper() == "N":
              valid = True
              kitchen()

        else:
            print("You cant do that")

def wineCellar():
    print("---WINE CELLAR---")
    global key1

    if key1 == False:

        key1 = True

        print("You find a key in the wine cellar and leave theres nothing else important here.")

        grandHall()

    else:

        print("Theres nothing important in here.")
        
        grandHall()

def utilityCloset():
    print("---UTILITY CLOSET---")
    choice = input("Mess with the fusebox? Y/N?")

    global fusebox

    valid = False

    while valid == False:
        if choice.upper() == "Y" or choice.upper() == "YES":
            print("You flick the fuses around and hear a faint motor noise come from the opposite end of the house")
            kitchen()
            fusebox = True
            valid = True
            print(fusebox)
        elif choice.upper() == "N" or choice.upper() == "NO":
            print("You leave the fusebox and leave the room")
            print(fusebox)
            kitchen()
            valid = True
        else:
            print("What")

 
def livingRoom():
    print("---LIVING ROOM---")
    print("An empty living room devoid of life. Ironic")
    
    valid = False

    while valid == False:
        direction = input("Theres doors West and North. Input either W or N to choose your direction")
        if direction.upper() == "W":
            valid = True
            diningRoom()
            
        elif direction.upper() == "N":
              valid = True
              hallway()

        else:
            print("You cant do that")

def diningRoom():
    print("---Dining Room---")
    print("The smell of rotten food pierces your nose")
    
    valid = False

    while valid == False:
        direction = input("Theres doors West and North. Input either W or E to choose your direction")
        if direction.upper() == "W":
            valid = True
            elevator1()
            
        elif direction.upper() == "E":
              valid = True
              livingRoom()

        else:
            print("You cant do that")

def elevator1():
    print("---ELEVATOR---")
    choice = input("Take the elevator Y/N?")

    valid = False

    while valid == False:
        if choice.upper() == "Y" or choice.upper() == "YES" and fusebox == True :
           print("You enter the elevator and pull the lone lever within it, taking you up to the second floor")
           valid = True
           hallway2()
        if choice.upper() == "Y" or choice.upper() == "YES" and fusebox == False :
           print("The Elevator is unresponsive. It appears to have no power being sent to it")
           valid = True
        elif choice.upper() == "N" or choice.upper() == "NO":
            print("You leave the room")
            valid = True
            diningRoom()
            
        else:
            print("What")

def hallway2():
   print("---Second Floor Hallway---")
   print("Two doors meet you at either side. Theres a strange whailing coming from the west")
   
   valid = False

   while valid == False:
    
    direction = input("Theres doors West,East and North (Elevator). Input either W,E or N to choose your direction")
    if direction.upper() == "W":
            valid = True
            grandBedroom()
    elif direction.upper() == "E":
            valid = True
            secondaryBedroom()
    elif direction.upper() == "N":
            print("You take the elevator back to the first floor")
            diningRoom()

    else:
        print("You cant do that")

def secondaryBedroom():
    print("---SECONDARY BEDROOM---")
    print("You enter what appears to be a son's room, half the roof is rotting and you can catch the stray raindrops from outside")

    global sword
    global playerDamageMultiplier

    if sword == False:
        print("Theres a sword on a stand, you take it")
        playerDamageMultiplier = 2
        sword = True
        hallway2()
       
    else:
        print("Theres nothing interesting here")
        print("You leave the way you came in")
        hallway2()
  
def grandBedroom():

    global key2

    ghostBattle = battleEncounter("001")

    if ghostBattle >= 0:
        print("You survive the fight against the ghoul and get find a key")
        print("You are at",ghostBattle,"HP")

        key2 = True
        
        hallway2()


def battleEncounter(monsterID):

    stay = True

    global playerDamageMultiplier
    global playerHP

    if monsterID == "001":
        monster = "Ghost"
        ATK = 6
        HP = 10

    elif monsterID == "002":
        monster = "Rat"
        ATK = 2
        HP = 4

    while stay == True:
        print(monster,":",HP)
        print("You have:",playerHP,"HP")

        action = input("F - FIGHT OR R - RUN")

        if action.upper() == "F":
            enemyroll = random.randint(1,ATK)
            playerroll = random.randint(1,6)

            if playerroll >= enemyroll:
                print("You attack the enemy and deal",playerroll*playerDamageMultiplier,"damage points")
                HP = HP - (playerroll * playerDamageMultiplier)
            else:
                print("The enemy attacks you and deals",enemyroll,"points of damage")
                playerHP = playerHP - enemyroll

        elif action.upper() == "R":
            print("You run away, but still get hit on your way out")
            enemyroll = random.randint(1,ATK)
            playerHP = playerHP - enemyroll
            stay = False
            if monsterID == "001":
                hallway2()
            elif monsterID == "002":
                kitchen()

        if HP <= 0:
            print("Monster Lost")
            stay = False
        elif playerHP <= 0:
           gameOver("GHOST")
           stay = False








def gameOver(death):
    print("---GAME OVER---")

    if death == "GHOST":
        print("You died to a spectral foe")
        

    

        

start = time.time()

hallway()