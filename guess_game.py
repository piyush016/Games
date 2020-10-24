import random #Import Random Module

secretNumber = random.randint(1, 20) #Secret Number will be between 1-20

print("***This is a guessing game***")
print("[*] You need to guess the number which the system is thinking.")
print("[*] Limits: 1 - 20 .")
print("[*] You only have 6 chances to guess")

for guessTaken in range(1, 7) : #For 7 chances
	print("[*] Take the guess.") 
	guess = int(input()) #Storing the input in guess. We have also converted strto int
	
	if guess < secretNumber : #If guess is greater than secret number
		print("[!!] Guess too low.")
		
	elif guess > secretNumber : #If guess is lesser than secret number
		print("[!!] Guess too high.")
		
	else : #If guess is equal to secret number
		break
		

if secretNumber == guess: #We have reached here if we guessed the secret number right
	print("[+] Voila!! Correct Guess.")
	print("You guessed my numeber in " + str(guessTaken) + " chance(s).")
	
else: #If we lost all our chances and couldn't guess the secret number
	print("[-] Sorry!! Incorrect Guess.")
	print("The number was " + str(secretNumber) + "." )
	
