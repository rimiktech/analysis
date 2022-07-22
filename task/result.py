#Write a program to arrange the students according to their marks in decreasing order?
print("Class 12 student result@")
D = {}
n = int(input('How many student record you want to store?- '))
ls = []

for i in range(0, n):
    x,y = input("Enter the student name and it's percentage: ").split()
    ls.append((y,x))
ls = sorted(ls, reverse = True)

print("Sorted list of students according to their marks in descending order")

for i in ls:
	
	
	print(i[1], i[0])