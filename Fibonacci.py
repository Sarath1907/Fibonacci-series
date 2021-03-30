# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

n=8


if n <= 0: # To verify if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(recur_fibo(i))
	   
Output:

Fibonacci sequence:
0
1
1
2
3
5
8
13
	   
	   
	   
# code for testing 

n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("This is in the Fibonacci series")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("This is in the Fibonacci series")
    else:
        print("This is not in the Fibonacci series")