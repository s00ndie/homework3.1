num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input("Choose operation '+,-,/,*': ")

if op == "+":
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '/':
    if num2 > 0:
        print(num1/num2)
    else:
        print('Second number should be more than 0')
elif op == '*':
    print(num1*num2)
else:
    print('Mistake')