#Write a recursive python function to calculate sum of first N even natural numbers

#METHOD : 1 (using recursion)
def sum_even(n,sm=0):
    if n>0:
        sm+=n*2
        sum_even(n-1,sm)
    else:
        print('Sum :',sm)

#METHOD : 2 (using lambda+recursion)
f2=lambda n:n*2 if n==1 else n*2+f2(n-1)

#METHOD : 3 (using only lambda)
f=lambda n:print('Sum :',sum([x*2 for x in range(1,n+1)]))

n_val=int(input('Enter N Value : '))
#sum_even(5)
print('Sum :',f2(n_val))