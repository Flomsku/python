print("hello", "world") #print is the name of the function, "hello" and "world" are the arguments that calls the function

other_print = print     #Just referring to the print function and not calling it
other_print("this is just a print with new name") #calling the print function with argument


#example calculation and function
#num1 = 5
#num2 = 7

def do_math(num1,num2=7): #defining function and calling it with arguments. Num2 is an optional argument and can be called with only one argument but it is possible to use two arugments
    result = num1 * num2
    result += 10
    result /= 1.5
    result -= num1
    return  result  #passes value to the caller of the function

print(do_math(4,2)) #calling function with two arguments
print(do_math(4,7))
print(do_math(4)) #calling function with one arguments
print(do_math(8,10))

try:
    print(do_math("hello","world"))
except:
    print("You cannot send strings to function 'do_math' that requires integers as arguments")

import operator # bad conduct to use import in the middle of the code, imports should be in the start of the code
print(operator.add(2,2)) # 2 + 2
print(operator.not_(True)) # Not True

def other_function(arg1, arg2='a', arg3=None, arg4=True, arg5='hello'): # 2 to 5 arguments are 'keyword' arguments / optional arguments
    pass

other_function(1, arg4= False) #specifying only arg1 and arg4
