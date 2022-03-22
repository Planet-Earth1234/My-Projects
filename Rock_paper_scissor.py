import random
import pyttsx3
List = ["Rock","Paper","Scissor"]


engine = pyttsx3.init()

while True :
    Input = input ("Any List:")
    Output = random.choice(List)
    point_player = 0
    point_computer = 0
    if Input == "Rock" and Output == "Paper":
        print (f"{Output, Input} computer won the game")
        point_computer += 1
        engine.say("Computer won the game")
        
    elif Input == "Paper" and Output == "Scissor":
        print (f"{Output, Input} computer won the game")
        point_computer += 1
        engine.say("Computer won the game")
        
    elif Input == "Scissor" and Output == "Rock":
        print (f"{Output, Input} computer won the game")
        point_computer += 1
        engine.say("Computer won the game")

    elif Input == Output :
        print (f"{Output,Input} None won the game")
        engine.say("None won the game")
    else:
        print (f"{Output, Input}Player won the game")
        point_player += 1
        engine.say("Player won the game")
    print (point_player)
    print(point_computer)

    engine.runAndWait()



    


