#number game
import random
possibilities = []
for a in range (1,10):
    for b in range (0,10):
        for c in range (0,10):
            for d in range (0,10):
                if a != b and a!=c and a!=d and b != c and b!=d and c != d:
                    if int(str(a) + str(b) + str(c) + str(d)) not in possibilities:
                        possibilities.append(int(str(a) + str(b) + str(c) + str(d)))



guess_list = []
correctness_list = []
inplace_list = []

def print_history():
    for i in range(len(guess_list)):
        print("|   Guesses    |   Correct   |   In Position   |")
        print("|       " + str(guess_list[i]) + "      |      " + str(correctness_list[i]) + "      |        " + str(inplace_list[i]) + "        |")




number = random.choice(possibilities)
def Correctness(inp_num):
    if inp_num == "q":
        return 0
    correct = 0
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
    print("Correct Numbers: " + str(correct) + "\nIn Place: " +str(in_place))
# print (len(possibilities))
print("the number is: " + str(number))
print("Welcome to the Number game! To start --- \n ")
guess = 0
while guess != "q" and int(guess) != number:
    if int(guess) == number:
        print("Congratulations! You guessed it correctly. It took you " + str(len(guess_list)) + " moves!")
    guess = input("input a 4 digit number without any repeating numbers as a guess: (q to exit)")
    Correctness(guess)
    print_history()
