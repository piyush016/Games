import random, sys

print("***Welcome to the ROCK, PAPER & SCISSORS Game***")
print("[*] Rule: (r)ock  (p)aper  (s)cissor  ")
print("[*] Enter 'q' to quit.")

#Counting wins, losses and ties
wins = 0
losses = 0
ties=0

#Until player enters quit, keeping running in the loop
while True:
    print("[+] %s Win(s)  %s Losse(s)  %s Tie(s)"%(wins, losses, ties))
    
    while True: 
        print("Enter your input: ") #Storing players move
        playerMove = input()
    
        if playerMove == 'q': #If the player wants to quit
            print("[!!] It was nice playing with you...Loser!!")
            sys.exit()
            
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's' : #Comparing players move if it's correct or not
            break
            
        else: #If not correct move, then print this 
            print("[!!] Enter a valid option.")
        
        
    if playerMove == 'r':
        print("Rock VS ", end='')
        
    elif playerMove == 'p':
        print("Paper VS ", end='')
        
    elif playerMove == 's':
        print("Scissors VS ", end='')
        
    #Getting random move    
    randomNumber = random.randint(1,3)
    #converting random move to system move
    if randomNumber == 1:
        computerMove = 'r'
        print("Rock")
        
    elif randomNumber == 2:
        computerMove = 'p'
        print("Paper")
        
    elif randomNumber == 3:
        computerMove = 's'
        print("Scissor")
        
        
    #Comparing player move with system move     
    if playerMove == computerMove:
        print("[|] It's a tie.")
        ties = ties+1
        
    elif playerMove == 'r' and computerMove == 's':
        print("[+] You win.")
        wins= wins+1
    
    elif playerMove == 'p' and computerMove == 'r':
        print("[+] You win.")
        wins= wins+1
        
    elif playerMove == 's' and computerMove == 'p':
        print("[+] You win.")
        wins= wins+1
        
    elif playerMove == 'r' and computerMove == 'p':
        print("[-] You lose.")
        losses= losses+1
        
    elif playerMove == 's' and computerMove == 'r':
        print("[-] You lose.")
        losses= losses+1
        
    elif playerMove == 'p' and computerMove == 's':
        print("[-] You lose.")
        losses= losses+1
                
        
        
        
        
        
    
