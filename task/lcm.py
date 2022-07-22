#Write the function "comput_LCM",  that will take two number as argument and return the LCM of two numbers.
def compute_lcm(x, y):
    if x > y:
        greater= x
    else:
        greater= y
        
    while(True):
        if((greater % x == 0)and(greater % y== 0)):
            lcm = greater
            break
        greater += 1
        
    return lcm

num1=int(input("enter first Number="))
num2=int(input("enter second Number="))

print("The L.C.M is", compute_lcm(num1, num2)) 
