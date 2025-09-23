'''Updated visual Representation -> User input -> Function -> Updates --> Updated visual Representation'''

'''Displaying the tic tac toe board with function :'''


# row1 = [' ',' ',' ']
# row2 = [' ',' ',' ']
# row3 = [' ',' ',' ']
#
# row2[1] = 'O'
#
# def display(row1,row2,row3):
#     print(row1)
#     print(row2)
#     print(row3)
#
# display(row1,row2,row3)
#
#
#
# some_value = 100
#
# print(some_value.is_integer())


# def user_choice():
#     # Variable input
#
#     #Initial value check whether it is int or anything else ?
#     choice = "wrong"
#     acceptable_value = range(0,11)
#     within_range = False
#
#
#      #Two Conditions To check
#     # Is input is Digit or Within Range == False
#
#
#     while choice.isdigit() == False or within_range == False:
#         choice = input("Please enter the number which is (0-10) : ")
#
#         #Digit Check :
#         if choice.isdigit() == False:
#             print("Sorry enter number is not a digit")
#
#         #Range Check :
#         if choice.isdigit() == True:
#             if int(choice) in acceptable_value:
#                 within_range = True
#             else:
#                 print("Sorry entered number is not in range!")
#                 within_range = False
#
#
#
#     return choice
#
# print(user_choice())

game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current list : ")
    print(game_list)

# display_game(game_list)

def position_choice():
    choice = 'wrong'

    while choice not in ['0','1','2']:

        choice = input("Pick a position (0,1,2) : ")

        if choice not in ['0','1','2']:
            print("It is an invalid choice!")

    return int(choice)

# position_choice()

def replacement_choice(game_list,position):
    user_replacement = input("Type a string to place at position : ")

    game_list[position] = user_replacement

    return game_list

#replacement_choice(game_list,position_choice())

def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y', 'N']:
        choice = input("Keep playing ? (Y or N) : ")

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, Please choose Y or N")

    if choice == 'Y':
        return True
    else:
        return False



# print(gameon_choice())

game_on = True
game_list = [0,1,2]

while game_on == True:
    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list,position)

    display_game(game_list)

    game_on = gameon_choice()

