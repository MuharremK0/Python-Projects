from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols=[random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers=[random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list=password_letters+password_symbols+password_numbers
    random.shuffle(password_list)

    password="".join(password_list)
    entry3.delete(0,END)
    entry3.insert(0,f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website=entry1.get()
    email_username=entry2.get()
    password=entry3.get()

    if (len(website) == 0 or len(password) == 0):
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty.")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail/Username: {email_username}\nPassword: {password}\nIs it ok to save ?")
        if is_ok:
            details= open("./day_29/PasswordManager/details.txt","a")
            details.write(f"{website} | {email_username} | {password}\n")
            entry1.delete(0,END)
            entry3.delete(0,END)
        
        
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

#img
canvas=Canvas(width=200,height=200,)
lock_img=PhotoImage(file="./day_29/PasswordManager/logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

#Label1
lab1=Label(text="Website:")
lab1.grid(column=0,row=1)

#Label2
lab2=Label(text="Email/Username:")
lab2.grid(column=0,row=2)

#Label3
lab1=Label(text="Password:")
lab1.grid(column=0,row=3)

#Entry1
entry1=Entry(width=35)
entry1.grid(column=1,row=1,columnspan=2,sticky="w")
entry1.focus()

#Entry2
entry2=Entry(width=35)
entry2.grid(column=1,row=2,columnspan=2,sticky="w")
entry2.insert(0,"k0@gmail.com")
#Entry3
entry3=Entry(width=16)
entry3.grid(column=1,row=3,sticky="w")

#Button1
button1=Button(text="Generate Password",width=14,command=generate_password)
button1.grid(column=1,row=3,sticky="e",columnspan=2)

#Button2
button2=Button(width=29,text="Add",command=save_info)
button2.grid(column=1,row=4,columnspan=2)




window.mainloop()