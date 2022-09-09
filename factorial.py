#Write a recursive python function to calculate the factorial of a number.

fact=lambda n:1 if n==1 else n*fact(n-1)

n_val=int(input('Enter N Value : '))
print('Factorial :',fact(n_val))