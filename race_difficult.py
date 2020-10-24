import turtle
import random

player_one = turtle.Turtle() 
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100) #Initial Position of player one

player_two = turtle.Turtle()
player_two.color("blue")
player_two.shape("turtle")
player_two.penup()
player_two.goto(-200, -100) #Initial position of player two

player_one.goto(300, 60) #Go to destination
player_one.pendown()
player_one.circle(40) #Make a circle
player_one.penup()
player_one.goto(-200, 100) #Comeback to initial position

player_two.goto(300, -140) #Go to destination
player_two.pendown()
player_two.circle(40) #Make a circle
player_two.penup()
player_two.goto(-200, -100) #Comeback to initial position

die = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6] #Virtual Dice

for i in range(50): #Total 50 chances per player
    if player_one.pos() >= (300, 100): #If player one crosses the destination then he wins
        print("Player One wins!!")
        break
    elif player_two.pos() >= (300, -100): #Else if player two crosses the destination then he wins
        print("Player Two wins!!")
        break

    else: #Else be in the for loop
        player_one_turn = input("Hit enter to roll the die.")
        die_outcome = random.choice(die)
        print("Result: %s" % die_outcome) #printing the output of the virtual dice
        if die_outcome >= 0: #For moving forward
            player_one.fd(10*die_outcome)
        else: #For moving backward 
            player_one.bk(10*(-die_outcome))

        #Similar to the above case
        player_two_turn = input("Hit enter to roll the die.")
        die_outcome = random.choice(die)
        print("Result: %s" % die_outcome)
        if die_outcome >= 0:
            player_two.fd(10*die_outcome)
        else:
            player_two.bk(10*(-die_outcome))
