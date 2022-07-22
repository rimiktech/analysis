#Write the function "recur_factorial",  that will take one number as argument and 
# return  factorial of that number.
If number is negative return  "factorial does not exist for negative numbers"
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  
 
num = int(input("Enter a number: "))  
 
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num)) 