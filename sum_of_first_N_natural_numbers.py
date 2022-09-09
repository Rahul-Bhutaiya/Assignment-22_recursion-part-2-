#Write a recursive python function to calculate sum of first N natural numbers

#METHOD : 1
def sum(n,sm=0):
    if n>0:
        sm+=n
        sum(n-1,sm)
    else:
        print(sm)

#METHOD : 2
def sum2(n):
    if n==1:
        return 1
    return n+sum2(n-1)

#METHOD : 3
f=lambda n:1 if n==1 else n+f(n-1)

n_val=int(input('Enter N Value : '))
#sum(n_val)
#print('Sum :',sum2(n_val))
print('Sum :',f(n_val))
