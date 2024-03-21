#### image
import requests
from PIL import Image
from io import BytesIO
import sys
import pygame

# create a dictionary of all rooms and there contents and respectiv doors
rooms = {
    "cell room": {
        "objects": ["a - toilet", "b - closet"],
        "doors": ["A", "cell door"]},
    "corridor": {
        "objects": ["a - psychopath"],
        "doors": ["A","cell door", "B","old wooden door", "C","security door"]},
    "cafeteria": {
        "objects": ["a - locker", "b - frezeer"],
        "doors": ["B", "old wooden door"]},
    "prison entrance": {
        "objects": ["a - security desk"],
        "doors": ["C", "security door", "D", "exit door"]}}

# status of the keys found
keys_found = set()

# status of the doors that are unlocked
doors_unlocked = set()

# indication of the Current room and where to start 
current_room = "cell room"

    
def space1():
    print(                                                          )

def space2():
    print( 
          
          )

def display_intro_image_from_url():
    intro_image_url = "https://i.ibb.co/qN83nTw/Aban-2.jpg"  # Replace with the actual URL of your image
    try:
        response = requests.get(intro_image_url)
        response.raise_for_status()  # Check if the request was successful
        intro_image = Image.open(BytesIO(response.content))
        intro_image.show()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the image: {e}")
        
def display_end_image_from_url():
    intro_image_url = "https://i.ibb.co/ky5tP76/prision.jpg"  # Replace with the actual URL of your image
    try:
        response = requests.get(intro_image_url)
        response.raise_for_status()  # Check if the request was successful
        intro_image = Image.open(BytesIO(response.content))
        intro_image.show()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the image: {e}")

def welcome_ironhack_game():
    space1()
    print("Welcome to the world of Ironhack games.")
    space1()
    start_game()

def start_game():
    space1()
    question = input("Do you want to play escape room?   v1.1 (y/n)")
    if question == "y":
        space1()
        print("ok, let's go")
        pygame.init()
        pygame.mixer.music.load("halloween.mp3")
        pygame.mixer.music.play()
        display_intro_image_from_url()
        space2()
        introdction()
    elif question == "n":
        print("ok, see you another day")
        exit
    else:
        print("sorry, I didn't understand that")
    
def start_room():
    space2()
    print(f"You are in the {current_room}.")
    prompt_user()

def introdction():
    print("""Welcome to the 'Abandoned Prison' escape game, where you will embark on a thrilling adventure to break free from the deepest confined spaces. \nAs you step into the dimly lit corridors, you'll encounter a series of challenges. With each step, you'll unravel the mysteries of the forsaken prison and strive to find your way to freedom. \nAre you ready to face the unknown and escape the 'Abandoned Prison' before time runs out? \nThe clock is ticking, and the fate of your escape lies in your hands. Good luck!""")
    space2()
    print("You just woke up and discovered that you are inside a prison cell. Explore the area to find a way out.")
    start_room()
    
# define the function Explore in the current room
def explore_room():
    space2()
    print(f"You are in {current_room}. In this area you can find the following objects: {', '.join(rooms[current_room]['objects'])}")
    space1()
    print(f"Also in this area you can find this doors: {', '.join(rooms[current_room]['doors'])}.")
    prompt_user()

# Examine an object
def examine_object():
    print(f"The objects in {current_room} are: {', '.join(rooms[current_room]['objects'])}.")
    print(f"The doors in this room are: {', '.join(rooms[current_room]['doors'])}.")
    object_name = input(f"Enter the name of the object you want to examine {rooms[current_room]['objects']}: ")
    if object_name == "a" or "b":
        space1()
        print(f"You examine the object.")
        if (object_name == "b" and current_room == "cell room"):
            key = "key A"
            print(f"You found a crowbar!")
            space1()
            keys_found.add(key)
            doors_unlocked.add("A")
            print("With that, you've destroyed the cell door!")
            space1()
        elif (object_name == "a" and current_room == "corridor"):
            key = "key B"
            space1()
            print(f"You found and saved the big stone to brake the wooden door!")
            space1()
            keys_found.add(key)
            doors_unlocked.add("B")
            space1()
            print("You brake the old wooden door!")
            space1()
        elif (object_name == "a" and current_room == "cafeteria"):
            key = "key C"
            space1()
            print(f"You found and saved the security door key!")
            space1()
            keys_found.add(key)
            doors_unlocked.add("C")
            space1()
            print("You unlocked security door!")
            space1()
        elif (object_name == "b" and current_room == "cafeteria"):
            key = "key D"
            space1()
            print(f"You found and saved the exit door key! Let's try to escape!!!")
            space1()
            keys_found.add(key)
            doors_unlocked.add("D")
            space1()
            print("You unlocked exit door!")
            space1()
        elif (object_name != "a" ):
            space1()
            print(f"This {object_name} letter is incorrect.")
            space1()  
        else:
            print("You didn't find anything that could help to escape.")
            space1()
    else:
        space1()
        print(f"There is no {object_name} in this room.")
        space1()
    prompt_user()

# Open a door
def open_door():
    door = input(f"Which door would you like to go to? ({', '.join(rooms[current_room]['doors'])}): ")
    if door in rooms[current_room]["doors"]:
        key = "key " + door
        if key in keys_found:
            if door in doors_unlocked:
                if door == "D":
                    display_end_image_from_url()
                    print("End of game - You win!")
                    sys.exit()                   
                else:
                    update_current_room(door)
                    space1()
            else:
                print(f"You haven't unlocked {door} yet.")
                space1()
        else:
            print(f"You don't have a way to open {door}.")
            space1()
    else:
        print(f"There is no door {door} in this room.")
        space2()
    prompt_user()

# Update current room
def update_current_room(door):
    global current_room
    if door == "A":
        if current_room == "cell room":
            current_room = "corridor"
        else:
            current_room = "cell room"            
    elif door == "B":
        if current_room == "corridor":
            current_room = "cafeteria"
        else:
            current_room = "corridor"            
    elif door == "C":
        if current_room == "corridor":
            current_room = "prison entrance"
        else:
            current_room = "corridor"
    explore_room()

# Prompt user for action
def prompt_user():
    space1()
    action = input("What would you like to do? (a) Explore (b) Examine (c) Go to a door: ")
    space1()
    if action == "a":
        explore_room()
        space1()        
    elif action == "b":
        examine_object()
        space1()        
    elif action == "c":
        open_door()
        space1()
    else:
        print("Invalid choice. Please try again.")
        space1()
        prompt_user()

# Start the game
welcome_ironhack_game()
