from cProfile import label
from cgitb import text
import numbers
import random
from tkinter import *
#tkinter is the standard GUI library for python. It helps in creating GUI applications

root = Tk()
root.title("Random Password Generator")
root.geometry('450x450') 

alpha = 'abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = ""
symbols= ""

def isChecked(numbers,symbols):
    if checkbtn1.get()==1:
        numbers=numbers.replace("",'0123456789')
    #print(characters)

    if checkbtn2.get()==1:
        symbols=symbols.replace("",'!@#$%^&*_+-,./=;:')

checkbtn1 = IntVar()
checkbtn2 = IntVar()

btnnumbers = Checkbutton(root,
                        text="Include numbers from 0 to 9", 
                        variable=checkbtn1, 
                        onvalue = 1,
                        offvalue = 0,
                        command= isChecked(numbers,symbols)
                    )
btnsymbols = Checkbutton(root,
                        text="Include special symbols",
                        variable=checkbtn2,
                        onvalue = 1,
                        offvalue = 0,
                        command= isChecked(numbers,symbols)
                    )

btnnumbers.pack()
btnsymbols.pack()


characters = alpha + numbers + symbols

#The Label is used to specify the container box where we can place the text or images.
label_characters = Label(root, text = "Enter length : ", font=('Arial',12)).pack(padx=10, pady=10)
#This entry is used to provide the user a single line text box for taking a value from the user
character_length = Entry(root,font= 'Arial 14',fg= 'red')

#The Pack geometry manager packs widgets relative to the earlier widget
character_length.pack(padx=10)

def generate_password():
    length = character_length.get()
    password = "".join(random.sample(characters, int(length)))
    label_password.config(text = 'Generated Password : ' + password)

Button(root,text="Genreate Password",command= generate_password, font=('Arial' , 12) ).pack(padx=10)
label_password = Label(root, font=('Arial' , 14) )
label_password.pack()

#This mainloop() function brings the GUI screen
root.mainloop()