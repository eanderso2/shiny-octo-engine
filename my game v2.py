import time
import turtle
def map():
    turtle.penup()
    turtle.forward(440)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(380)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(770)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(390)
    turtle.penup()
    turtle.goto(x=0,y=0)
print("this was made by CONTUNUM PROGRAMING")
def game_over():
    print("game over")
    time.sleep(1)
    game_over()
time.sleep(1)
print("pleas have in full screen")
time.sleep(1)
name = input("what is your name: ")
print("hi",name)
time.sleep(1)
friend_name = input("what is your best friend's name: ")
time.sleep(1)
print("You are in the carrabean on a unknown island.")
time.sleep(1)
print("you were in a plane crash with",friend_name,"everyone else died.")
time.sleep(1)
print("  ______  __    __       ___      .______   .___________. _______ .______          __  ")
print(" /      ||  |  |  |     /   \     |   _  \  |           ||   ____||   _  \        /_ | ")
print("   ,----'|  |__|  |    /  ^  \    |  |_)  | `---|  |----`|  |__   |  |_)  |        | | ")
print("|  |     |   __   |   /  /_\  \   |   ___/      |  |     |   __|  |      /         | | ")
print("|  `----.|  |  |  |  /  _____  \  |  |          |  |     |  |____ |  |\  \----.    | | ")
print(" \______||__|  |__| /__/     \__\ | _|          |__|     |_______|| _| `._____|    |_| ")                                                                                    
time.sleep(5)
print('you : hay',friend_name)
time.sleep(1)
print(friend_name,': yes')
time.sleep(1)
print('you : are you okay?')
time.sleep(1)
print(friend_name,': yes')
time.sleep(1)
print(friend_name,": what are we going to eat other than the Doritos from the plane?")
time.sleep(1)
print(friend_name,": coconut. (not)")
time.sleep(1)
print("if you see a , then add a answer")
time.sleep(1)
food=input("there is a coconut tree nearby and a watermelon patch by a river. choose one ")
print("okay") 
time.sleep(1)
print(friend_name,": i will go get some",food)
time.sleep(1)
print(friend_name,": go set up the tent. okay?")
tent=input()
if tent=="no":
    game_over()
if tent=="yes":
    print("later that day")
time.sleep(1)
print("it is time to go to bed")
time.sleep(1)
print(" ______  __    __       ___      .______   .___________. _______ .______          ___   ") 
print(" /      ||  |  |  |     /   \     |   _  \  |           ||   ____||   _  \        |__ \  ") 
print("|  ,----'|  |__|  |    /  ^  \    |  |_)  | `---|  |----`|  |__   |  |_)  |          ) | ") 
print("|  |     |   __   |   /  /_\  \   |   ___/      |  |     |   __|  |      /          / /  ") 
print("|  `----.|  |  |  |  /  _____  \  |  |          |  |     |  |____ |  |\  \----.    / /_  ") 
print(" \______||__|  |__| /__/     \__\ | _|          |__|     |_______|| _| `._____|   |____| ") 
time.sleep(5)
print("you : yawn.")
time.sleep(1)
print("you : hay",friend_name)
time.sleep(1)
print("you : hmm, no answer")
time.sleep(1)
print("outside of the banana leaf tent")
time.sleep(1)
print("you : there are footprints. mabye",friend_name,"is getting wood")
time.sleep(1)
print("you : why are there other footprints that",friend_name,"did not make")
time.sleep(1)
map1=input("do you want to open the map ")
if map1=="yes":
    map()
    