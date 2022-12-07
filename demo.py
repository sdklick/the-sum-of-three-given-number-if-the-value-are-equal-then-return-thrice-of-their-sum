'''
calculate the sum of three given number if the 
value are equal then return thrice of their sum
'''

num1=int(input('enter 1st number : '))
num2=int(input('enter 2nd number : '))
num3=int(input('enter 3rd number : '))

if num1==num2==num3:
    sum=num1+num2+num3
    print('sum of three number is : ',sum)
else:
    print('number is not equal')    

