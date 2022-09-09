#Write a recursive python function to calculate sum of squares of first N natural numbers

square=lambda n:1 if n==1 else n**2+square(n-1)

n_val=int(input('Enter N Value : '))
print(square(n_val))