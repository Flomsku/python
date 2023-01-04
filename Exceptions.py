try: #basics to try and except
    print(1 + 'hi')
except TypeError:
    print('you cannot add string to integer')

def print_sum(num1, num2):
    try:
        print('sum of your numbers:',num1+num2)
    except Exception:
        print('Could not add those numbers, you have to enter two integers')

def print_sumconditional(num1,num2): #raise exception method for types
    if type(num1) != int or type(num2) != int:
        raise Exception('Inputs to the print_sumconditional function must be integers')
    print(num1 + num2)
    

print_sum(1,2)
print_sum('asd',1)
print_sumconditional(1,2)


try:
    print_sumconditional('hi',2)
except Exception as e: #e as standard name for exception variables
    print(f'Something went wrong: {e}')
