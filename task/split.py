#Write a program to given an array of integers nums and a positive integer k, 
# check whether it is possible to divide this array into sets of k consecutive numbers.
# Return true if it is possible. Otherwise, return false.
from collections import defaultdict


def groupInKConsecutive(arr, K):


	count = defaultdict(int)

	for h in arr:
		count[h] += 1


	for key, value in count.items():
		cur = key
		n = value

		
		if (n > 0):

		
			for i in range(1, K):

			
				if ((cur + i) not in count):
					return False

				count[cur + i] -= n

				
				if (count[cur + i] < 0):
					return False
					
	return True


if __name__ == "__main__":

	arr = [ 1, 6, 2,
			3, 4, 7, 5, 7, 3 ]
	k = 2
	
	if (groupInKConsecutive(arr, k)):
		print("True")
	else:
		print("False")