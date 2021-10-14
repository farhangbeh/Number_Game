from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random



class NumberGame(Widget):

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
            # if inplc == 2:
            #     for i in range(len(cutlist)):
            #         if :
            #             temp_cutlist.remove(cutlist[i])
            # if inplc == 3:
            #     for i in range(len(cutlist)):
            #         if :
            #             temp_cutlist.remove(cutlist[i])
        if correct == 3: #need to finish #check correct ALSO ^ is exclisve or
            for i in range(len(cutlist)):
                if (number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[0] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i])) or (number[1] not in str(cutlist[i]) and number[3] not in str(cutlist[i])) or (number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])):
                    temp_cutlist.remove(cutlist[i])
                if inplc == 0:
                    if (number[0] == str(cutlist[i])[0] or number[1] == str(cutlist[i])[1] or number[2] == str(cutlist[i])[2] or number[3] == str(cutlist[i])[3]):
                        temp_cutlist.remove(cutlist[i])
            # if inplc == 1:
            #     for i in range(len(cutlist)):
            #         if :
            #             temp_cutlist.remove(cutlist[i])
            # if inplc == 2:
            #     for i in range(len(cutlist)):
            #         if :
            #             temp_cutlist.remove(cutlist[i])
        if correct == 2: #need to finish
            for i in range(len(cutlist)):
                if(number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])):
                    temp_cutlist.remove(cutlist[i])
                if (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                    temp_cutlist.remove(cutlist[i])
                if inplc == 0:
                    if (number[0] == str(cutlist[i])[0] or number[1] == str(cutlist[i])[1] or number[2] == str(cutlist[i])[2] or number[3] == str(cutlist[i])[3]):
                        temp_cutlist.remove(cutlist[i])
            # if inplc == 1:
            #     for i in range(len(cutlist)):
            #         if :
            #             temp_cutlist.remove(cutlist[i])
            #
        if correct == 1: #check correct
            if inplc == 0: #should output 1260
                for i in range(len(cutlist)):
                    if (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] == str(cutlist[i])[0] or number[1] == str(cutlist[i])[1] or number[2] == str(cutlist[i])[2] or number[3] == str(cutlist[i])[3]):
                        temp_cutlist.remove(cutlist[i])
                    elif(number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
            if inplc == 1:
                for i in range(len(cutlist)):
                    if (number[0] in str(cutlist[i]) and number[1] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[0] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[2] in str(cutlist[i])) or (number[1] in str(cutlist[i]) and number[3] in str(cutlist[i])) or (number[2] in str(cutlist[i]) and number[3] in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
                    elif (number[0] != str(cutlist[i])[0] and number[1] != str(cutlist[i])[1] and number[2] != str(cutlist[i])[2] and number[3] != str(cutlist[i])[3]):
                        temp_cutlist.remove(cutlist[i])
                    elif(number[0] not in str(cutlist[i]) and number[1] not in str(cutlist[i]) and number[2] not in str(cutlist[i]) and number[3] not in str(cutlist[i])):
                        temp_cutlist.remove(cutlist[i])
        if correct == 0:
            for i in range(len(cutlist)):
                if number[0]  in str(cutlist[i]) or number[1] in str(cutlist[i]) or number[2] in  str(cutlist[i]) or number[3] in str(cutlist[i]):
                    temp_cutlist.remove(cutlist[i])
        cutlist[:] = temp_cutlist[:]


    def Correctness(self, inp_num):
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
        print("Cows: " + str(correct))
        print("Bulls: " + str(in_place))



    def register_answer(self):
        print("your guess is: ", self.ids.text_input.text)
        self.Correctness(self.ids.text_input.text)
        return("Cows: " + str(correct) + " \nBulls: " + str(in_place))
    pass


class Number_gameApp(App):
    def build(self):
        game = NumberGame()
        return game




if __name__ == '__main__':
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
    number=3865
    Number_gameApp().run()





def print_history():
    print("|   Guesses    |   Correct   |   In Position   |")
    for i in range(len(guess_list)):
        print("|     " + str(guess_list[i]) + "     |      " + str(correctness_list[i]) + "      |        " + str(inplace_list[i]) + "        |")

def print_possibilites():
    print(cutlist)


#idea: make an array of 10 digits, when one is no longer a possibility, remove it from the list. and then remove the possibilites from cutlist
