#Write a Program to Display Floyd's Triangle using the for loop?
rows = int(input("Please Enter the total Number of Rows  : "))

print("Floyd's Triangle") 
for i in range(1, rows + 1):
    for j in range(1, i + 1):        
        print('* ', end = '  ')
    print()