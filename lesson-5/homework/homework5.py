sql = int(input('Do you know SQL? 1 means \'YES\', 0 means \'NO\''))
python = int(input('Do you know Python?: 1 means \'YES\', 0 means \'NO\''))


if sql and python == 1:
    print('BI Developer')
elif sql == 1 and python == 0:
    print('Data Analyst')
elif sql == 0 and python == 1:
    print('Data Engineer')
elif sql and python == 1:
    print('Not Qualified')
else:
    print('Error 404')

year = int(input('Input the year: '))

if year % 100 == 0:
    if year % 400 == 0:
        print('a Leap Year')
    else:
        print('Not a Leap Year')    
elif year % 4 == 0:    
    print('a Leap Year')    
else:
    print('Not a Leap Year')    

# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# without else

number = int(input('Input the number: '))


if number % 2 == 0:
        if number in [2,4]:
            print('Not Weird')
        elif number in [6,8,10,12,14,16,18,20]:
            print('Weird') 
        elif number > 20:
            print('Not Weird')       
elif number % 2 == 1:
    print('Weird')    


# with else

number = int(input('Input the number: '))

if number % 2 == 0:
        if number in [2,4]:
            print('Not Weird')
        elif number in [6,8,10,12,14,16,18,20]:
            print('Weird') 
        elif number > 20:
            print('Not Weird')       
else:
    print('Weird')    
