#Write a recursive python function to print binary of a given decimal number.

#METHOD : 1 (USING RECURSION ONLY)
def binary(dec_num,st=''):
    if dec_num>0:
        st=str((dec_num%2))+st
        binary(dec_num//2,st)
    else:
        print('Binary :',st)

#METHOD : 2 (USING RECURSION + LAMBDA)
binary2=lambda number:'' if number==0 else binary2(number//2)+str(number%2)

#METHOD : 3 (USING ONLY LAMBDA)
binary3=lambda number:format(number,'b')#here 'b' means 'binary'

number=int(input('Enter a Decimal Number : '))
print(binary3(number))
