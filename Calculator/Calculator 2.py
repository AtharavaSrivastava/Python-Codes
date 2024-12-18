print('Information about the Calculator :')
print('')
print('1.This Calculator does not follow the rules of BODMAS')
print('2.Only four Operators can be used in this Calculator "+","-","*"and"/"')
print('3.Currently this Calculator can take only 2-15 operands')
print('')

      
operands = int(input('How many operands does your question have ?'))
print('')

#Operands = 2
               
if (operands == 2):
    num1 = int(input('Enter the First Number = '))
    num2 = int(input('Enter the Second Number = '))
    op1 = input('Enter the First Operator = ')

    if( op1 == '+'):
        ot1 = num1+num2
        print('The sum of the numbers is =',ot1)
    elif (op1 == '-'):
        ot1 = num1-num2
        print('The differnece of the numbers is =',ot1)
    elif (op1 == '*'):
        ot1 = num1*num2
        print('The product of the numbers is =',ot1)
    elif (op1 == '/'):
        ot1 = num1/num2
        print('The quotient of the numbers is =',ot1 )
    else :
        print('Wrong Operator')

        
#Operands = 3

elif (operands == 3):
    num1 = int(input('Enter the First Number = '))
    num2 = int(input('Enter the Second Number = '))
    op1 = input('Enter the First Operator = ')

    if( op1 == '+'):
        ot1 = num1+num2
        print('The sum of the numbers is =',ot1)
    elif (op1 == '-'):
        ot1 = num1-num2
        print('The differnece of the numbers is =',ot1)
    elif (op1 == '*'):
        ot1 = num1*num2
        print('The product of the numbers is =',ot1)
    elif (op1 == '/'):
        ot1 = num1/num2
        print('The quotient of the numbers is =',ot1 )
    else :
        print('Wrong Operator')

        print('')
        print('----------------')
        print('')
        
    num3 = int(input('Enter the Third Number = '))
    op2 = input('Enter the Second Operator = ')
    if( op2 == '+'):
        ot2 = ot1+num3
        print('The sum of the numbers is =',ot2)
    elif (op2 == '-'):
        ot2 = ot1-num3
        print('The differnece of the numbers is =',ot2)
    elif (op2 == '*'):
        ot2 = ot1*num3
        print('The product of the numbers is =',ot2)
    elif (op2 == '/'):
        ot2 = ot1/num3
        print('The quotient of the numbers is =',ot2)
    else :
        print('Wrong Operator')

    
#Operands = 4
    
elif (operands == 4):
    num1 = int(input('Enter the First Number = '))
    num2 = int(input('Enter the Second Number = '))
    op1 = input('Enter the First Operator = ')
    
    if( op1 == '+'):
        ot1 = num1+num2
        print('The sum of the numbers is =',ot1)
    elif (op1 == '-'):
        ot1 = num1-num2
        print('The differnece of the numbers is =',ot1)
    elif (op1 == '*'):
        ot1 = num1*num2
        print('The product of the numbers is =',ot1)
    elif (op1 == '/'):
        ot1 = num1/num2
        print('The quotient of the numbers is =',ot1 )
    else :
        print('Wrong Operator')
        
        print('')
        print('----------------')
        print('')
    
    num3 = int(input('Enter the Third Number = '))
    op2 = input('Enter the Second Operator = ')
    if( op2 == '+'):
        ot2 = ot1+num3
        print('The sum of the numbers is =',ot2)
    elif (op2 == '-'):
        ot2 = ot1-num3
        print('The differnece of the numbers is =',ot2)
    elif (op2 == '*'):
        ot2 = ot1*num3
        print('The product of the numbers is =',ot2)
    elif (op2 == '/'):
        ot2 = ot1/num3
        print('The quotient of the numbers is =',ot2)
    else :
        print('Wrong Operator')

        print('')
        print('----------------')
        print('')
        
    num4 = int(input('Enter the Fourth Number = '))
    op3 = input('Enter the Third Operator = ')
    if( op3 == '+'):
        ot3 = ot2+num4
        print('The sum of the numbers is =',ot3)
    elif (op3 == '-'):
        ot3 = ot2-num4
        print('The differnece of the numbers is =',ot3)
    elif (op3 == '*'):
        ot3 = ot2*num4
        print('The product of the numbers is =',ot3)
    elif (op3 == '/'):
        ot3 = ot2/num4
        print('The quotient of the numbers is =',ot3)
    else :
        print('Wrong Operator')

#Operands = 5
elif (operands == 5):
    num1 = int(input('Enter the First Number = '))
    num2 = int(input('Enter the Second Number = '))
    op1 = input('Enter the First Operator = ')
    
    if( op1 == '+'):
        ot1 = num1+num2
        print('The sum of the numbers is =',ot1)
    elif (op1 == '-'):
        ot1 = num1-num2
        print('The differnece of the numbers is =',ot1)
    elif (op1 == '*'):
        ot1 = num1*num2
        print('The product of the numbers is =',ot1)
    elif (op1 == '/'):
        ot1 = num1/num2
        print('The quotient of the numbers is =',ot1 )
    else :
        print('Wrong Operator')
    
    print('')
    print('----------------')
    print('')
    num3 = int(input('Enter the Third Number = '))
    op2 = input('Enter the Second Operator = ')  
    if( op2 == '+'):
        ot2 = ot1+num3
        print('The sum of the numbers is =',ot2)
    elif (op2 == '-'):
        ot2 = ot1-num3
        print('The differnece of the numbers is =',ot2)
    elif (op2 == '*'):
        ot2 = ot1*num3
        print('The product of the numbers is =',ot2)
    elif (op2 == '/'):
        ot2 = ot1/num3
        print('The quotient of the numbers is =',ot2)
    else :
        print('Wrong Operator')

    print('')
    print('----------------')
    print('')

    num4 = int(input('Enter the Fourth Number = '))
    op3 = input('Enter the Third Operator = ')
    if( op3 == '+'):
        ot3 = ot2+num4
        print('The sum of the numbers is =',ot3)
    elif(op3 == '-'):
        ot3 = ot2-num4
        print('The differnece of the numbers is =',ot3)
    elif (op3 == '*'):
        ot3 = ot2*num4
        print('The product of the numbers is =',ot3)
    elif (op3 == '/'):
        ot3 = ot2/num4
        print('The quotient of the numbers is =',ot3)
    else :
        print('Wrong Operator')

    print('')
    print('----------------')
    print('')

    num5 = int(input('Enter the Fifth Number = '))
    op4 = input('Enter the Fourth Operator = ')
    if( op4 == '+'):
        ot4 = ot3+num5
        print('The sum of the numbers is =',ot4)
    elif (op4 == '-'):
        ot4 = ot3-num5
        print('The differnece of the numbers is =',ot4)
    elif (op4 == '*'):
        ot4 = ot3*num5
        print('The product of the numbers is =',ot4)
    elif (op4 == '/'):
        ot4 = ot3/num5
        print('The quotient of the numbers is =',ot4)
    else :
        print('Wrong Operator')
        
