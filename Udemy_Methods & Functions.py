# my_list = [1,2,3,4,5]
#
# my_list.append(6)
#
# my_list.pop()
#
# help(my_list.insert)
#
# my_list.insert(4,'a')
#
# print(my_list)
#
#
# def name_of_wife(relation):
#     print("Poorni" + relation)
#
# name_of_wife(' is my wife')

# def _say_hello_():
#     print("Hello")
#
# _say_hello_()


# def _say_hello_(name = "Poorni"):
#     print("Phsyco " + name)
#
# _say_hello_("Deekshanaasri")


# def _return_(num1,num2):
#     return num1 + num2
#
# result = _return_(50,20)
#
# print(result)


# def _even_check(number):
#     return number % 2 == 0
#
# print(_even_check(21))

'''Return True if any number is even inside a list'''

# def _even_check_list(my_list):
#     for i in my_list:
#         if i % 2 == 0:
#             return True
#         else:
#             pass
#             #return False    # This is wrong, Here loop will stop at first number because return will end the function
#     return False
#
# print(_even_check_list([5,9,7,2]))
#
# print(_even_check_list([5,9,7,1]))

'''Return all even numbers in list'''

# def _even_num_list(my_list):
#
#     result = []
#
#     for i in my_list:
#         if i % 2 == 0:
#             result.append(i)
#
#         else:
#             pass
#
#     return result
#
# new_result = _even_num_list([1,2,3,4,5,6,7,8,9])
# print(new_result)
#
# #print(_even_num_list([1,3,5,7,9]))


'''Tuples unpacking with Python Function'''

# work_hours = [('Pandi',600),('Poorni',700),('Deekshanaasri',300)]
#
# def employee_Check(work_hours):
#     current_max = 0
#     emplyee_of_month = ''
#
#     for employee,hours in work_hours:
#         if hours > current_max:
#             current_max = hours
#             emplyee_of_month = employee
#
#         else:
#             pass
#     return(emplyee_of_month,current_max)
#
# print(employee_Check(work_hours))

# example = [1,2,3,4,5,6,7]
from random import shuffle
#
# # shuffle(example)
# #
# # print(example)
# #print("sri")
#
# def shuffle_list(mylist):
#     shuffle(mylist)
#     return mylist
# #
# # result = shuffle_list(example)
# # print(result)
#
#
# '''Game with single ball with 3 container and Finds correct container which has ball'''

# my_list = [' ', ' O ', ' ']
#
# def ball_game(game_list):
#     shuffle(game_list)
#     return(game_list)
#
# result =  shuffle_list(my_list)
#
#
# def player_guess():
#     guess = ""
#     while guess not in ['0', '1', '2']:
#         guess = input("Pick a number : 0, 1 or 2 : ").strip()     #strip will delete unwanted spaces. Here after that only condition is passing
#     return int(guess)
#
# player_guess()
#
# myindex = player_guess()
# print(myindex)
#
# def check_guess(result,player_guess):
#     if result[player_guess] == 'O':
#         print("correct")
#
# print(result)

# from random import shuffle
#
# mylist = [' ', 'O', ' ']
#
# def shuffle_list(mylist):
#     shuffle(mylist)
#     return mylist
#
# def player_guess():
#     guess = ''
#     while guess not in ['0', '1', '2']:
#         guess = input("Pick a number : 0, 1 or 2 : ").strip()
#     return int(guess)
#
# # Shuffle the list
#
#
# # Get the player's guess
# my_index = player_guess()
# print("Player guessed index:", my_index)
#
# def check_guess(mylist,guess):
#     if mylist[guess] == '0':
#         print("Correct!")
#     else:
#         print("Wrong Guess!")
#         print(mylist)
#
# mixedup_list = shuffle_list(mylist)
# guess = player_guess()
# check_guess(mixedup_list,guess)

# Finally above code is not working as expected


'''*args & **kwargs'''

#* args - Uses to give n number of arguments in tuples. * followed by any key word. *spam also same. After * is a arbitary choice.
#Better use *args

# **kwargs - Uses to give n number of arguments and return key word. Basically it makes as input as dictinory


# def my_func(*args):  # If we declare *args in function, User can assign any number of arguments
#     print(args)
#     return 0.05 * sum((args))
#
#
# print(my_func(20,30,100))

# def my_new_func(*pandi):
#     for i in pandi:
#         print(i)
#     return sum((pandi))
#
# print(my_new_func(10,20,30,40,50,60))


# def new_arg(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print("My fruit of choice is ", kwargs['fruit'])
#     else:
#         print("I did not find any fruit here")
#
# new_arg(fruits="apple",veggie="shawarma")

# def my_mixed_func(*args,**kwargs):  # args should come first that is syntax
#     print(args)
#     print(kwargs)
#     print("My argument is", args[0],kwargs['food'])
#
#
# my_mixed_func(10,20,30,40,fruit="orange",food="shawarma")


# def myfunc(*arg):
#     my_list = []
#
#     for i in arg:
#         if i % 2 == 0:
#             my_list.append(i)
#     return my_list
# print(myfunc(2,4,5,9,10))


# def myfunc(s):
    #return ''.join([char.lower() if i % 2 == 0 else char.upper() for i, char in enumerate(s)])

# a = "Deekshanaasri"
#
# for i, char in enumerate(a):
#     if i % 2 == 0:
#         char.lower()
#     else:
#         char.upper()
# (enumerate(a))

'''50. Function Practice
Write a function that return the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd'''

# def odd_or_even(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         print("even")
#         if a < b:
#             return (a)
#         else:
#             return (b)
#
#     else:
#         print("odd")
#         if a > b:
#             return (a)
#         else:
#             return (b)
#
#
# print(odd_or_even(2,4))

'''Animal Crackers : Write a function takes a two-word string and returns True if both the words begin with same letter

animal_crackers('Levelheaded Llama') -> True
animal_crackers('crazy Kangaroo') -> False '''

# def animal_crackers(text):
#     wordlist = text.split()
#     print(wordlist)
#     if (wordlist[0][0]) == (wordlist[1][0]):
#         print("True")
#     else:
#         print("False")
#
#
# animal_crackers("Levelheaded Llama")
# animal_crackers('crazy Kangaroo')

'''Makes Twenty : Given two integers, return True if the sum of the integers is 20 or if one of the integer is 20. If not, return false'''

# def _Twenty_(a,b):
#     if a + b == 20 or (a == 20 or b == 20):
#         print("True")
#
#     else:
#         print ("False")
#
# _Twenty_(20,3)

'''Solution Level One'''
'''1. OLD MACDONALD : Write a function that capitalizes the first and fourth lettets of a name
old_macdonald('macdonald') -> MacDonald
Note : 'macdonald.capitalize() returns 'Macdonald'''''

# def capital(name):
#     first_letter = name[0]
#     inbetween_letter = name [1:3]
#     fourth_letter = name[3]
#     rest_of_letters = name[4:9] # [4:]
#     capital_first_letter = name[0].upper()
#     capital_fourth_letter = name[3].upper()
#     #print(capital_first_letter + inbetween_letter + capital_fourth_letter + rest_of_letters)
#     print(first_letter.upper() + inbetween_letter + fourth_letter.upper() + rest_of_letters)
#
#
# capital('macdonald')


'''2. Master Yoda : Given a sentence, reutn a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready')  --> 'ready are We'''''

# def master_yoda(text):
#     wordlist = text.split()
#     reversed_list = wordlist[::-1]
#     joint_list = ' '.join(reversed_list)
#     print(joint_list)
#
#
# master_yoda("I am home")

'''3. Given an integer n, return True if n is within 10 of either 100 or 200'''

# def almost_there(n):
#     return (abs(100-n) <= 10 or abs(200-n) <= 10)
#     # if n in range (100,111) or n in range (200,211):
#     #     print(True)
#     # else:
#     #     print(False)
#
# print(almost_there(210))

'''Solution Level Two'''
'''1. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
has_33([1,3,3])  -> True
has_33([1,3,1,3]) -> False
has_33([3,1,3])  -> False'''

# def has_33(nums):
#     for x in range(0,len(nums)-1):
#         if nums[x] == 3 and nums[x+1] == 3:
#             return True
#
#     return False
#
# print(has_33([3,1,3]))


'''2.  Paper Doll : Given a string,return a string where for every character in the origin there are three
characters

paper_doll('Hello') -> 'HHHeeellllllooo 
paper_doll('') -> 'MMMiiissssssiiissssssiiippppppi' '''


# def paper_doll(string):
#     result = ''
#     for i in string:
#         result += i*3
#         #interemediate_Result = i*3
#         #result = result + interemediate_Result
#     print(result)
#
# paper_doll('Mississippi')

'''3. Black Jack : Given three integers between 1 and 11, if their sum is less than or equal to 21.
return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19'''

# def blackjack(a,b,c):
#     if a + b + c <= 21:
#         print(a+b+c)
#
#     elif 11 in [a,b,c] and (a + b + c) - 10 <= 21:
#         print(a + b + c - 10)
#     else:
#         print('BUST')
#
# blackjack(9,9,9)

'''4. Summer of 69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
and extending to the next 9 (every 6 will be followed by least one 9). Return 0 for no numbers'''

# def summer_69(arr):
#     result = 0            #As it is hard, I left even after explain. Refer the 59th video in udemy
#     for x in arr:
#
#
#         result = result + x
#     print(result)
#
# summer_69([1,3,5])
# summer_69([4,5,6,7,8,9])

''''5. Challenge Problems
SPY GAME : Write a function that takes in a list of integers and returns True if it contains 007 in order

(spy_game([1,2,4,0,0,7,5])) --> True
(spy_game([1,0,2,4,0,5,7])) --> True
(spy_game([1,7,2,0,4,5,0])) --> False'''

# def spy_game(arr):
#     code = [0,0,7,'x']
#     for x in arr:
#         if x == code[0]:
#             code.pop(0)
#     return len(code) == 1
#
#
# #print(spy_game([1,2,4,0,0,7,5]))
# #print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))


''' Lambda Expressions Map & Filter'''

# def square(num):
#     return num **2
#
# my_nums = [1,2,3,4,5,6]
#
# for item in (map(square,my_nums)):
#     print(item)
#
# print(list(map(square,my_nums)))

def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'Even'
    else:
        return my_string[0]

names = ['Pandiarajan','PoornimaDevi','Deekshanaasri']

print(list(map(splicer,names)))