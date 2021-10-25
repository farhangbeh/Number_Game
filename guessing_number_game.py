#number game
import random
from guessing_number_game_functions import *
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
play_again_status = True
play_again=""
while play_again_status:
    guess = ""
    while guess != "q" and guess != str(number):
        print("guess = " + guess)
        if guess == str(number):
            print("Congratulations! You guessed it correctly. It took you " + str(len(guess_list)) + " moves!")
        guess = input("input a 4 digit number without any repeating numbers as a guess: (q to exit)")
        if guess == "p":
            print_possibilites()
        elif guess == "q":
            break
        else:
            Correctness(guess)
            print_history()
            remove_non_possible(guess,correct,in_place,cutlist)
    if guess != "q":
        print("Congratulations! You got it :)\n")
    while not play_again_allowed(play_again):
        play_again = input("\nWould you like to play again? (Y for yes, N for no)").lower()
        if play_again_allowed(play_again) == False:
            print("invalid answer, make sure you give a valid input")
        elif play_again_allowed(play_again) == 0:
            print("thank you for playing!")
            play_again_status = False
        elif play_again_allowed(play_again) == 1:
            print("Let's go again!")
