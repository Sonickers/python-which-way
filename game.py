from random import randint
import time

def greeting():
    print("Welcome! Write your name:")
    name = input()
    print(name + ", your travel ends and starts here. That's a crossroad before you. You can choose one way. Are you ready?")
    print()
    time.sleep(2)
greeting()

def choose_way():    
    chose_way = ''
    while chose_way != '1' and chose_way != '2':
        print("Sign on the LEFT(1) says \"Don't go there!\" but on the RIGHT(2) \"Easy way to your goal!\" Which road do you go?")
        chose_way = input()    

    return chose_way    
chosen_way = choose_way()

def has_choosen(): 
    print("You made choice. Was that a good one?")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(2)
has_choosen()

def result(chosen_way):
    good_road = randint(1, 2)
    print('debug: {}'.format(good_road))
    if chosen_way == str(good_road):
        print("You chose good way. Good luck!")
    else:
        print("You chose wrong way. You need to back and choose again...")
result(chosen_way)

