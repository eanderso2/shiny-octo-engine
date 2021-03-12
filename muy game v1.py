import time
def game_over():
    print("game over")
    time.sleep(2)
def hello_there():
        print("Type your name:")
        name = input()
        print("Hi", name, )
def level():
    print("type your level:")
    name = input()
def game_p1():
        level()
def game():
        game_p1()
        game_over()
mycount = 0
hello_there()
while (mycount < 4):
        game()
print(game_dict)
