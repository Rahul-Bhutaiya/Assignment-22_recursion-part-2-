#Write a recursive python function to find the Nth term of the Fibonacci series.

def fibonacci(n,f1=0,f2=1):
    if n>0:
        print(f1,end=' ')
        f1,f2=f2,f1+f2
        fibonacci(n-1,f1,f2)

n_val=int(input('Enter N Value : '))
fibonacci(n_val)