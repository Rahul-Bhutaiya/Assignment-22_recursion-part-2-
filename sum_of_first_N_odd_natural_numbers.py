#Write a recursive python function to calculate sum of first N odd natural numbers

#METHOD : 1 (using recursion)
def sum_odd(n,sm=0):
    if n>0:
        sm+=(n*2-1)
        sum_odd(n-1,sm)
    else:
        print('Sum :',sm)

#METHOD : 2 (using lambda+recursion)        
f2=lambda n:1 if n==1 else (n*2-1)+f2(n-1)

#METHOD : 3 (using only lambda)
f=lambda n:print('Sum :',sum([x*2-1 for x in range(1,n+1)]))

n_value=int(input('Enter a Number : '))
print('Sum :',f2(n_value))
#sum_odd(n_value)