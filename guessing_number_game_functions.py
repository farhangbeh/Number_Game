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
        return 0
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


number = random.choice(possibilities)
