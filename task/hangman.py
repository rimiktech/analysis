name = input("Enter your name: ")
print("Hello, " + name, "Let's play hangman!")

print("So what's your first guess?")


word = "najmus"


guesses = ''


turns = 10


while turns > 0:         

    
    failed = 0             

        
    for char in word:      

    
        if char in guesses:    
          print(char)
        else:
   
        
            print("_")
       
        
            failed += 1    

   
    if failed == 0:        
        print("You won")

    
        break              

    print()
    
    guess = input("guess a character:") 

   
    guesses += guess                    

    
    if guess not in word:  
 
     
        turns -= 1        
        print("Wrong Guess")    
 
   
        print("You have", + turns, 'more guesses')  
   
        if turns == 0:           
    
       
            print ("You Lose")
              