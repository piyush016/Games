import random
from termcolor import colored, cprint

outcome = random.randint(1, 2) #Making random selection from 1-2

print(colored("*** This is a toss ***",'magenta'))
print(colored("[*] You need to type either Heads or Tails.",'magenta'))

while True: 
    print(colored("[?] Heads or Tails ??",'yellow'))
    guess = str(input()) #Taking user input only in Heads and Tails
    if guess == "Heads" or guess == "Tails": #Verifying if the user entered a valid selection or not
        break
    else:
        print(colored("[!!] Please enter either 'Heads' or 'Tails'.",'yellow')) #If it wasn't a valid option, promting again to user

#Converting random selected number to their particular value 
if outcome == 1 : 
    result = "Heads"

elif outcome == 2:
    result = "Tails"

#Checking if the user won or lost
if guess == result:
    print(colored("[+] You won the toss.",'green'))

else:
    print(colored("[-] You lost the toss.",'red'))