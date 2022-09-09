#Write a recursive python function to print octal of a given decimal number

#METHOD : 1 (USING RECURSION ONLY)
def octal(dec_number,oc=''):
    if dec_number>0:
        oc=str(dec_number%8)+oc
        octal(dec_number//8,oc)
    else:
        print('Octal :',oc)

#METHOD : 2 (USING RECURSION ONLY)
def octal2(dec_number):
    if dec_number==0:
        return ''
    else:
        return octal2(dec_number//8)+str(dec_number%8)
    
#METHOD : 3 (USING RECURSION + LAMBDA)
octal3=lambda n:'' if n==0 else octal3(n//8)+str(n%8)

#METHOD : 4 (USING ONLY LAMBDA)
octal4=lambda n:format(n,'o')

dec_num=int(input('Enter a Decimal Number : '))
print(octal4(dec_num))