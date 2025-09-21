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


def user_choice():
    # Variable input

    #Initial value check whether it is int or anything else ?
    choice = "wrong"
    acceptable_value = range(0,11)
    within_range = False


     #Two Conditions To check
    # Is input is Digit or Within Range == False


    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter the number which is (0-10) : ")

        #Digit Check :
        if choice.isdigit() == False:
            print("Sorry enter number is not a digit")

        #Range Check :
        if choice.isdigit() == True:
            if int(choice) in acceptable_value:
                within_range = True
            else:
                print("Sorry entered number is not in range!")
                within_range = False



    return choice

print(user_choice())

