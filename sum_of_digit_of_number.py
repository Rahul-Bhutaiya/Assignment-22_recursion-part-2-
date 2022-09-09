#Write a recursive python function to calculate sum of the digits of a given number

#METHOD : 1 (USING RECURSION ONLY)
def sum_digit(number,digit=0):
    if number>0:
        digit+=number%10
        sum_digit(number//10,digit)
    else:
        print('Sum :',digit)

#METHOD : 2 (USING RECURSION + LAMBDA)
sum_digit2=lambda number:0 if number==0 else number%10+sum_digit2(number//10)

#METHOD : 3 (USING ONLY LAMBDA)
f=lambda number:print('Sum :',sum([int(x) for x in str(number)]))
#METHOD : 4 (USING ONLY LAMBDA)
f2=lambda number:sum([int(x) for x in str(number)])

number=int(input('Enter N Value : '))
#sum_digit(number)
#print('Sum :',sum_digit2(number))
print('Sum :',f2(number))