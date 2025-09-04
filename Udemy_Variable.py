'''Variable has LEGB Rule where
L : Local - Names assigned in any way within a function (def or lambda)
E : Enclosing functional locals - Names in the local scope of any and all enclosing  functions (def or lambda)m from inner to outer
G : Global(module) - Names assigned at the top level of a module file or declared global in a def within the file
B : Built-in (Python) - Names preassigned in the built-in names module : open,range,syntaxError '''

'''Local Variable'''

# #Global Variable
# name = 'This is a global variable'
#
# def greet():
#     #name = "This is a enclosed variable"    # This is a Enclosed variable
#
#     def hello():
#         # Local variable
#         #name = "This is the local variable"
#         print('Hello ' + name)
#
#     hello()
#
# greet()

# x = 50  # Global assignement
#
# def func(x):
#     print("X is ",x)
#     #print(f'X is {x}')
#
#     x = 200 #Local Assignment
#     print("I just locally changed to ", x)
#
# func(x)
#
# print(x)

x = 50  # Global assignement

def func():
    global x

    print("X is ",x)
    #print(f'X is {x}')

    x = 'New value' #Local Assignment
    print("I just changed to global assignment ", x)

func()

print(x)










