from tkinter import *
import math

from pandas.core.common import not_none
from pandas.core.indexers import check_key_length

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    my_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
    checkmark_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1 #start at the first rep
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it is the 8ht rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Time for a break!", bg=YELLOW, fg=RED)
    #if it is the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="Break!", bg=YELLOW, fg=PINK)
    # if it is the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        my_label.config(text="Let's work!", bg=YELLOW, fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}") #just like label config this changes the particular text in particular canvas
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    if count == 0:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)
        #checkmark_label.config(text="✔" * (reps//2)) #easier way to do
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#after - is a method that takes an amount of time that it should wait, after that amount of time,
# #it simply calls a particular func. that you tell it to call passing in any arguments that you want to give it.
#we first give amount to wait in milliseconds 1000ms = 1s
#then we pass in a function to call
#we can give unlimited positional args, that will be passed to the func that we want to call


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#Timer Label
my_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
my_label.grid(column=1, row=0)


#Buttons
start_button = Button(text="Start", highlightthickness=0, bd=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, bd=0, command=reset_timer)
reset_button.grid(column=2, row=2)

#Checkmark Label
checkmark_label = Label(bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3)


window.mainloop()
#so the mainloop is listening, and when the user interacts with the start button,
#it actually calls the start_timer func. which calls the count_down func. and get it to count down from some amount of mins