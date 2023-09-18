from tkinter import * 
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    lab1.config(text="Timer")
    lab2.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if(reps%8==0):
        count_down(long_break_sec)
        lab1.config(text="Break",fg=RED)
    elif(reps%2==1):
        count_down(work_sec)
        lab1.config(text="Work",fg=GREEN)
    elif(reps%2==0):
        count_down(short_break_sec)
        lab1.config(text="Break",fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute=math.floor(count/60)
    second=count%60

    if(second<10):
        second=f"0{second}"
        
    canvas.itemconfig(timer_text,text=f"{minute}:{second}")

    if(count > 0):
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        lab2.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#Label1
lab1=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
lab1.grid(column=1,row=0)

#Label2
lab2=Label()
lab2.config(fg=GREEN,bg=YELLOW)
lab2.grid(column=1,row=3)

#Button1
btn1=Button(text="Start",highlightthickness=0,command=start_timer)
btn1.grid(column=0,row=2)

#Button2
btn2=Button(text="Reset",highlightthickness=0,command=reset_timer)
btn2.grid(column=2,row=2)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="./day_28/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00.00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


window.mainloop()