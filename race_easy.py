import turtle
import random

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100) #Initial Position of player one

player_two = turtle.Turtle()
player_two.color("blue")
player_two.shape("turtle")
player_two.penup()
player_two.goto(-200,-100)  #Initial Position of player two

player_one.goto(300,60) #Final position of player one
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100) #Returning back to initial position

player_two.goto(300,-140) #Final position of player two
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100) #Returning back to initial position

die = [1,2,3,4,5,6] #Virtual dice

for i in range(30): #30 Chances per Player
    if player_one.pos() >= (300,100): #If player one reaches the destination first 
            print("Player One Wins!!")
            break
    elif player_two.pos() >= (300,-100): #If player two reaches the destination first
            print("Player Two Wins!!")
            break
    else: #Else be in the for loop 
        
        player_one_turn = input("Hit Enter to roll the die.")

        die_outcome = random.choice(die)
        print("Result: %s" %die_outcome)
        player_one.fd(10*die_outcome) #Player one moving forward

        player_two_turn = input("Hit Enter to roll the die.")
        die_outcome = random.choice(die)
        print("Result of the die: %s " %die_outcome)
        player_two.fd(10*die_outcome) #Player two moving forward
