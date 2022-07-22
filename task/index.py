#Write a program to implement direct index mapping with negative values allowed?
#Given a limited range array contains both positive and non-positive numbers.
def search(X):

	if X >= 0:
		return has[X][0] == 1


	X = abs(X)
	return has[X][1] == 1

def insert(a, n):

	for i in range(0, n):
		if a[i] >= 0:
			has[a[i]][0] = 1
		else:
			has[abs(a[i])][1] = 1


if __name__ == "__main__":

	a = [-1, 9, -5, -8, -5, -2]
	n = len(a)

	MAX = 1000
	
	#
	has = [[0 for i in range(2)]
			for j in range(MAX + 1)]
	insert(a, n)

	X = int(input("ebnter the no-:"))
	if search(X) == True:
		print("Present")
	else:
		print("Not Present")