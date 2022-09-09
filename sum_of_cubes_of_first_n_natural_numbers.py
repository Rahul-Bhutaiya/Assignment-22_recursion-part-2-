#Write a recursive python function to calculate sum of cubes of first N natural numbers

cubes=lambda n:1 if n==1 else n**3+cubes(n-1)

n_val=int(input('Enter N Value : '))
print('Sum :',cubes(n_val))