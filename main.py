#main


#number game
#guessing_number_game_functions



#number game
import random

# 4536 total possibilites
possibilities = []
for a in range (1,10):
    for b in range (0,10):
        for c in range (0,10):
            for d in range (0,10):
                if a != b and a!=c and a!=d and b != c and b!=d and c != d:
                    if int(str(a) + str(b) + str(c) + str(d)) not in possibilities:
                        possibilities.append(int(str(a) + str(b) + str(c) + str(d)))

cutlist = possibilities[:]
number = random.choice(possibilities)

guess_list = []
correctness_list = []
inplace_list = []

def print_history():
    print("|   Guesses    |   Correct   |   In Position   |")
    for i in range(len(guess_list)):
        print("|     " + str(guess_list[i]) + "     |      " + str(correctness_list[i]) + "      |        " + str(inplace_list[i]) + "        |")

def print_possibilites():
    print(cutlist)


#idea: make an array of 10 digits, when one is no longer a possibility, remove it from the list. and then remove the possibilites from cutlist


def is_number_allowed(number):
    x = str(number)[0]
    y = str(number)[1]
    z = str(number)[2]
    i = str(number)[3]
    if x != y and x != z and x != i and y != z and y != i and z != i:
        return True
    else:
        return False

def play_again_allowed(answer):
    allowed_y = ["y", "yes"]
    allowed_n = ["n", "no"]
    if answer in allowed_y:
        return 1
    elif answer in allowed_n:
        return 2
    else:
        return False

def remove_non_possible(num, cor, inplc,cutlist):#idk why we have to call cutlist yet
    #whenever you call an array in a function, it assigns a new place and original is UNTOUCHED unless you call cutlist[:] or something.
    temp_cutlist = cutlist[:] #otherwise making identical list and modifying one modifies the other
    number = str(num)
    if cor == 4:#need to finish
            if inplc == 0:
                for i in range(len(cutlist)):
                    if number[0] not in str(cutlist[i]) or number[1] not in str(cutlist[i]) or number[2] not in  str(cutlist[i]) or number[3] not in str(cutlist[i]):
                        temp_cutlist.remove(cutlist[i])
                    elif number[0] == str(cutlist[i])[0] or number[1] == str(cutlist[i])[1] or number[2] == str(cutlist[i])[2] or number[3] == str(cutlist[i])[3]:
                        temp_cutlist.remove(cutlist[i])
            if inplc == 1:
                for i in range(len(cutlist)):
                    if number[0] not in str(cutlist[i]) or number[1] not in str(cutlist[i]) or number[2] not in str(cutlist[i]) or number[3] not in str(cutlist[i]):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3]):
                        temp_cutlist.remove(cutlist[i])
                    elif ((number[0] == str(cutlist[i])[0] and number[1] == str(cutlist[i])[1]) or (number[0] == str(cutlist[i])[0] and number[2] == str(cutlist[i])[2]) or (number[0] == str(cutlist[i])[0] and number[3] == str(cutlist[i])[3]) or (number[1] == str(cutlist[i])[1] and number[2] == str(cutlist[i])[2]) or (number[1] == str(cutlist[i])[1] and number[3] == str(cutlist[i])[3]) or (number[2] == str(cutlist[i])[2] and number[3] == str(cutlist[i])[3])):
                        temp_cutlist.remove(cutlist[i])
            if inplc == 2:
                for i in range(len(cutlist)):
                    if number[0] not in str(cutlist[i]) or number[1] not in str(cutlist[i]) or number[2] not in str(cutlist[i]) or number[3] not in str(cutlist[i]):
                        temp_cutlist.remove(cutlist[i])
                    elif ((number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2]) or (number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1] and number[3] != str(cutlist[i])[3]) or (number[0] != str(cutlist[i])[0] and number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3]) or (number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3])):
                        temp_cutlist.remove(cutlist[i])
                    elif ((number[0] == str(cutlist[i])[0] and number[1] == str(cutlist[i])[1] and number[2] == str(cutlist[i])[2]) or (number[0] == str(cutlist[i])[0] and number[1] == str(cutlist[i])[1] and number[3] == str(cutlist[i])[3]) or (number[0] == str(cutlist[i])[0] and number[2] == str(cutlist[i])[2] and number[3] == str(cutlist[i])[3]) or(number[1] == str(cutlist[i])[1] and number[2] == str(cutlist[i])[2] and number[3] == str(cutlist[i])[3])):
                        temp_cutlist.remove(cutlist[i])

    if cor == 3: #need to finish #check correct ALSO ^ is exclisve or

            if inplc == 0:
                for i in range(len(cutlist)):
                    if (number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] == str(cutlist[i])[0] or number[1] == str(cutlist[i])[1] or number[2] == str(cutlist[i])[2] or number[3] == str(cutlist[i])[3]):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
            if inplc == 1:
                for i in range(len(cutlist)):
                    if (number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3]):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
            if inplc == 2:
                for i in range(len(cutlist)):
                    if (number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
                    elif ((number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2]) or (number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1] and number[3] != str(cutlist[i])[3]) or (number[0] != str(cutlist[i])[0] and number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3]) or (number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3])):
                        temp_cutlist.remove(cutlist[i])
                    elif ((number[0] == str(cutlist[i])[0] and number[1] == str(cutlist[i])[1] and number[2] == str(cutlist[i])[2]) or (number[0] == str(cutlist[i])[0] and number[1] == str(cutlist[i])[1] and number[3] == str(cutlist[i])[3]) or (number[0] == str(cutlist[i])[0] and number[2] == str(cutlist[i])[2] and number[3] == str(cutlist[i])[3]) or (number[1] == str(cutlist[i])[1] and number[2] == str(cutlist[i])[2] and number[3] == str(cutlist[i])[3])):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
            if inplc == 3:
                for i in range(len(cutlist)):
                    if (number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
                    elif ((number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1]) or (number[0] != str(cutlist[i])[0] and number[2] != str(cutlist[i])[2]) or (number[0] != str(cutlist[i])[0] and number[3] != str(cutlist[i])[3]) or (number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2]) or (number[1] != str(cutlist[i])[1] and number[3] != str(cutlist[i])[3]) or (number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3])):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])

    if cor == 2:

            if inplc == 0:
                for i in range(len(cutlist)):
                    if((number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i]))):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] == str(cutlist[i])[0] or number[1] == str(cutlist[i])[1] or number[2] == str(cutlist[i])[2] or number[3] == str(cutlist[i])[3]):
                        temp_cutlist.remove(cutlist[i])
            elif inplc == 1:
                for i in range(len(cutlist)):
                    if((number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i]))):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3]):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])

            elif inplc == 2:
                for i in range(len(cutlist)):
                    if((number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i]))):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
                    elif ((number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2]) or (number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1] and number[3] != str(cutlist[i])[3]) or (number[0] != str(cutlist[i])[0] and number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3]) or (number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3])):
                        temp_cutlist.remove(cutlist[i])

    if cor == 1: #check correct
        if inplc == 0: #should output 1260
            for i in range(len(cutlist)):
                if (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                    temp_cutlist.remove(cutlist[i])
                elif (number[0] == str(cutlist[i])[0] or number[1] == str(cutlist[i])[1] or number[2] == str(cutlist[i])[2] or number[3] == str(cutlist[i])[3]):
                    temp_cutlist.remove(cutlist[i])
                elif(number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])):
                    temp_cutlist.remove(cutlist[i])
        elif inplc == 1:
            for i in range(len(cutlist)):
                if (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                    temp_cutlist.remove(cutlist[i])
                elif (number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3]):
                    temp_cutlist.remove(cutlist[i])
                elif(number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])):
                    temp_cutlist.remove(cutlist[i])
    if cor == 0:
        for i in range(len(cutlist)):
            if number[0]  in str(cutlist[i]) or number[1] in str(cutlist[i]) or number[2] in  str(cutlist[i]) or number[3] in str(cutlist[i]):
                temp_cutlist.remove(cutlist[i])
    cutlist[:] = temp_cutlist[:]
    # print(cutlist)
    print("remaining possibilities: " + str(len(cutlist)))



def Correctness(inp_num):
    if inp_num == "q":
        return 0
    global correct
    correct = 0
    global in_place
    in_place = 0
    string_inp = str(inp_num)
    string_num = str(number)
    guess_list.append(inp_num)
    for i in range(4):
        if string_inp[i] == string_num[i]:
            in_place += 1
            correct += 1
        elif string_inp[i] in string_num:
            correct +=1
    correctness_list.append(correct)
    inplace_list.append(in_place)

def print_history():
    print("|   Guesses    |   Correct   |   In Position   |")
    for i in range(len(guess_list)):
        print("|     " + str(guess_list[i]) + "     |      " + str(correctness_list[i]) + "      |        " + str(inplace_list[i]) + "        |")







print("the number is: " + str(number))
print("Welcome to the Number game! To start --- \n ")
play_again_status = 1
guess = ""
while play_again_status == 1:
    play_again=False
    while guess != "q" and guess != str(number) and guess != "quit":
        if guess == str(number):
            print("Congratulations! You guessed it correctly. It took you " + str(len(guess_list)) + " moves!")
        guess = input("input a 4 digit number without any repeating numbers as a guess: (q to exit)")
        if guess == "p":
            print_possibilites()
        elif guess == "q" or guess == "quit":
            print("okay, exiting the game")
        else:
            Correctness(guess)
            print_history()
            remove_non_possible(guess,correct,in_place,cutlist)
    if guess != "q" and guess != "quit":
        print("Congratulations! You got it :)\n")
    while play_again_allowed(play_again) == False :
        play_again = input("\nWould you like to play again? (Y for yes, N for no)").lower()
        if play_again_allowed(play_again) == False:
            print("invalid answer, make sure you give a valid input")
        elif play_again_allowed(play_again) == 2:
            print("thank you for playing!")
            play_again_status = 2
        elif play_again_allowed(play_again) == 1:
            print("Let's go again!")
            play_again_status = 1
            guess = ""
            possibilities = []
            for a in range (1,10):
                for b in range (0,10):
                    for c in range (0,10):
                        for d in range (0,10):
                            if a != b and a!=c and a!=d and b != c and b!=d and c != d:
                                if int(str(a) + str(b) + str(c) + str(d)) not in possibilities:
                                    possibilities.append(int(str(a) + str(b) + str(c) + str(d)))

            cutlist = possibilities[:]
            guess_list = []
            correctness_list = []
            inplace_list = []
            number = random.choice(possibilities)
            print("the number is: " + str(number))
            print("Welcome to the Number game! To start --- \n ")
