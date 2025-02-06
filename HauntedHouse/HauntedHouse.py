﻿import time

key1 = False
fusebox = False


def hallway():
    print("---HALLWAY---")
    print("You are in the hallway, a grand room. As you look around you see paintings and delicate ornaments. There are three exits​,")

    valid = False

    while valid == False:
        direction = input("Theres door North and South. Input either N or S to choose your direction")
        if direction.upper() == "N":
            valid = True
            bottomBedroom()
        elif direction.upper() == "S":
               valid = True
               livingRoom()
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

def utilityCloset():
    print("---UTILITY CLOSET---")
    choice = input("Mess witht he fusebox? Y/N?")

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
    print("---UTILITY CLOSET---")
    choice = input("Take the elevator Y/N?")

    valid = False

    while valid == False:
        if choice.upper() == "Y" or choice.upper() == "YES" and fusebox == True :
           print("You enter the elevator and pull the lone lever within it, taking you up to the second floor")
           # hallway2()
        if choice.upper() == "Y" or choice.upper() == "YES" and fusebox == False :
           print("The Elevator is unresponsive. It appears to have no power being sent to it")
        elif choice.upper() == "N" or choice.upper() == "NO":
            print("You leave the room")
            diningRoom()
            
        else:
            print("What")



start = time.time()

hallway()