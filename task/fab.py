def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

nterms=int(input("how many terms="))
if nterms<=0:
    print("enter the positive integer")
else:
    print("fibonacci sequence")
    for i in range(nterms):
        print(recur_fibo(i))