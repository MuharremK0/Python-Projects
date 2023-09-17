from tkinter import *

FONT=("Arial",24,"italic")

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=150)
window.config(padx=20,pady=20) #adding padding


#Label1
label1=Label(text="Miles",font=FONT)
label1.grid(column=2,row=0)

#Label2
label2=Label(text="is equal to",font=FONT)
label2.grid(column=0,row=1)

#Label3
label3=Label(text="0",font=FONT)
label3.grid(column=1,row=1)

#Label4
label4=Label(text="Km",font=FONT)
label4.grid(column=2,row=1)

#Entry
input=Entry(width=10)
input.grid(column=1,row=0)

#Button
def button_clicked():
    km=round(float(input.get())*1.609,2)
    label3.config(text=km)

button=Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)



window.mainloop()