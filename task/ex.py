def maxSumSubarrayRemovingOneEle(arr, n):
	
	fw = [0 for k in range(n)]
	bw = [0 for k in range(n)]

	cur_max, max_so_far = arr[0], arr[0]
	fw[0] = cur_max

	for i in range(1,n):
		cur_max = max(arr[i], cur_max + arr[i])
		max_so_far = max(max_so_far, cur_max)

	
		fw[i] = cur_max

	
	cur_max = max_so_far = bw[n-1] = arr[n-1]
	i = n-2
	while i >= 0:
		cur_max = max(arr[i], cur_max + arr[i])
		max_so_far = max(max_so_far, cur_max)

		
		bw[i] = cur_max
		i -= 1


	fans = max_so_far

	
	for i in range(1,n-1):
		fans = max(fans, fw[i - 1] + bw[i + 1])

	return fans


arr = []
n = int(input())
for i in range (o,n):
    ele=int(input())
    arr.append(ele)
temp=[len(arr)-1]
p=0
for i in range(0,len(temp)):
    temp[p]=arr[i+1]
    p+=1
    print (maxSumSubarrayRemovingOneEle(temp, n))

