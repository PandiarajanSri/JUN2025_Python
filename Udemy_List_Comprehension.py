# mystring = 'hello'
#
# mylist = []
#
# for letter in mystring:
#     mylist.append(letter)
#
# print(mylist)
#
# my_list = []
#
# for x in [2,4,6]:
#     for y in [1,10,100]:
#         my_list.append(x*y)
#
# print(my_list)

# my_newlist = "My world is india".split()
# print(my_newlist)

''''Statement Assessment Test'''
'''1. Use for,.split(), and if to create a statement that will print out words that start with 's'''
#
# st = 'Print ony the words that start with s in this sentence'
# #x = input("Enter the sentence which needs to split the word which starts with S : ")
#
# y = st.split()
#
#
# for z in y:
#     if z[0] == 's':
#         print(z)


'''2. Use range() to print all the even numbers from 0 to 10. '''

# for f in range(0,10):  # Here we are not read the question so changed after seeing the result
#     if f % 2 == 0:
#         print(f)

# x = list(range(0,11,2))
#
# print(x)

'''3. Use a List Complrehension to create a list of all numbers between 1 and 50 that are divisible by 3.'''

# list_3 = []
#
# for i in range(1,50):
#     if i % 3 == 0:
#         list_3.append(i)
# print(list_3)

# y = list(range(3,51,3))           #Another way
# print(y)

'''4. Go through the string below and if the length of a word is even print "even!'''

# st = "Print every word is this sentence that has an even number of letters"
#
# new_st = []
#
# new_st = st.split()
#
# for i in new_st:
#     if len(i) % 2 == 0:
#         print(i, "These are even words")



''''5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz instead of the number
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz'''


# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)

# '''6. Use list comprehensive to create list of the first letters of every word in the string below'''

# st = "Create a  list  of the first letters of every word in this string"
#
# my_new_list = []
# first_letter = []
#
# my_new_list = st.split()
#
# for i in my_new_list:
#     first_letter.append(i[0])
#
# print(first_letter)


