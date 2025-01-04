'''keywords
variable---- data ---- datatypes---- data structure(collection)
operator
logic --- condition ---- iteration(for-while) -----break,continue,pass'''
from click import argument
from numpy.ma.core import argsort

'''what is function?

logic ---- prime number 

line number - 13 to 19 --- prime number code ----- use

210--216 ---- prime use

423 --429 --- prime use

cons
----
lines of programming is high :- more memory consume
Time consuming
Resource consuming
product price is high

i want a box ---- i contains  the required logics in that box,--- when i need , i just call that box.

function is a wrapper code of logic, when we will call that function name, automatically logic will
impliment, so that--- pros

how many types of function?

inbuilt function------ are already in python.(print(),id(),eval(),id()....)
user define function ---- as a programmer , we develope our own function for own logic.
syntax
'''

'''
def function_name():
    statements/logic
    return data  '''

'''def wish():
    var = 'Hi Good Morning'
    return var

print(wish())
print(wish())
print(wish())'''

'''
What is parameter?
Parameter is one kind of variable--data,
but parameter pass based on function requirement.
in function parameter pass in parantheisis
'''

#WAP to add two number?

'''def addition(a,b):
    add = a+b
    return add

print(addition(10,20))
print(addition(30,70))'''

#WAP find the number is even or not?

'''def is_even_odd(num):
    if num%2==0:
        return 'Even'
    else:
        return 'Odd'

print(is_even_odd(11))'''


#WAP check the string is pallindrom or not?

'''def is_pallindrom(st):
    if st == st[::-1]:
        return 'Pallindrom'
    else:
        return 'Not a Pallindrom'

print(is_pallindrom('qwerty'))
'''

'''def is_pallidrom(st):
    new_st = ''
    for i in st:
        new_st = i + new_st

    if st == new_st:
        return 'Pallindrom'
    else:
        return 'Not a Pallindrom'

print(is_pallidrom('yui'))'''

#types of arguments?
'''
in python there are 4 types of arguments
1.Positional Arguments
2.Keyword
3.Default
4.Varibale length of arguments

'''

'''def add(a,b):
    res = a+b
    return res

print(add(20,10))'''


'''def f1(p1,p2):#formal argument----- parameter
    pass

f1(dat1,dat2)---- actual argument ---- arguments'''


'''def add(a,b,c,d):
    res = a-b+c-d
    return res

print(add(30,d =40,b = 10,c=20))'''

#default arguments

'''def add(a,b=10):
    res = a+b
    return res

print(add(10,))'''

#variable length argument
'''
*args --- arguments --- element
**kwargs--- keyword arguments -key,value
'''
'''
def add(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

print(add(10,20,30,40,1000,2000))'''


'''def dictt(**kwargs):
    print(kwargs)

dictt(name='A',age=26,salary = 23000)'''


'''def add_sub(a,b):
    add = a+b
    sub = a-b
    return add,sub
print(add_sub(10,20))'''

#Types of variables
'''
global variable:- those declare in outside of function, and it will access by both outside of function and inside the function.
local variable:- those declare in inside of the function, and it will access only inside the func, know as local variable
'''
'''var= 10
print(var)

def f1():
    res = var+40
    return res

print(f1())'''


'''def f1():
    global var
    var = 10#local
    res = var+40
    return res

print(f1())

def f2():
    print(var)
print(f2())'''

'''
lambda function
filter, map, reduce
nested function
decorator
generator
'''

#prac the string function....

# str1 = 'i love india'
'''1.write function count the each occurance of each char of string?
'''
'''i3 2l1o1e1n1a1'''



'''
process:-
declare a function and take a parameter
use a for loop to iterate the string
outiside of the for loop declare a empty dictionary
the count the itration '''

'''str1 = 'i love india'

def count_occurance(st):

    char_count = {}
    for i in st:'''

'''di = {'a':1,'b':1}

di = {'a':1,'b':2,'c':3}'''

'''li = [10,11,10,10,10,11,23,45]

for i in li:
    if li.count(i)==1:
        print(i)'''






