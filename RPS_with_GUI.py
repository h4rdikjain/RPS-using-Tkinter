import random
import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
window.title("ROCK PAPER SCISSORS GAME")
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""
def word_choice(word):
    rps = {'rock':0,'paper':1,'scissors':2}
    return rps[word]

def num_choice(number):
    rps = {0:'rock',1:'paper',2:'scissors'}
    return rps[number]

def comp_choice():
    return random.choice(['rock','paper', 'scissors'])


def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = word_choice(human_choice)
    comp = word_choice(comp_choice)
    if user == comp:
        print("IT'S A TIE!!")
    elif ((user-comp)%3==1):
        print('You WIN!!')
        USER_SCORE += 1
    else:
        print("Computer WINS!!,You lose")
        COMP_SCORE += 1

    text_area = tk.Text(master = window,height = 12, width = 30,bg="#9bc400")
    text_area.grid(column=0,row = 4)
    answer = "Your Choice: {}\n Computer's Choice: {} \n Your Score: {} \n Computer Score: {}".format(USER_CHOICE,COMP_CHOICE,USER_SCORE,COMP_SCORE)
    text_area.insert(tk.END,answer )

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'rock'
    COMP_CHOICE = comp_choice()
    result(USER_CHOICE,COMP_CHOICE)

def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'paper'
    COMP_CHOICE = comp_choice()
    result(USER_CHOICE,COMP_CHOICE)

def scissors():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'scissors'
    COMP_CHOICE = comp_choice()
    result(USER_CHOICE,COMP_CHOICE)

button1 = tk.Button(text ="    Rock    ",bg="red",command = rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text ="    Paper   ",bg="green",command = paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text ="  Scissors  ",bg="blue",command = scissors)
button3.grid(column=0,row=3)

window.mainloop()
        