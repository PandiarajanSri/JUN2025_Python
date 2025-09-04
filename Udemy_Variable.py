'''Variable has LEGB Rule where
L : Local - Names assigned in any way within a function (def or lambda)
E : Enclosing functional locals - Names in the local scope of any and all enclosing  functions (def or lambda)m from inner to outer
G : Global(module) - Names assigned at the top level of a module file or declared global in a def within the file
B : Built-in (Python) - Names preassigned in the built-in names module : open,range,syntaxError '''

'''Local Variable'''

lambda num : num **2

print(num(10))

'''This line is added now for testing'''