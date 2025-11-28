"""from tkinter import *
from main import generate_password, prompt_int
from random import randint
import pyperclip

root = Tk()
root.title('Password Generator/Manager')
root.geometry("500x300")
password = generate_password()

def new_rand():
    pw_entry.delete(0, END)
    
    pw_length = prompt_int()

def clipper():
    pass

lf = LabelFrame(root, text="How many characters?")
lf.pack(pady=20)

user_entry = Entry(lf, font=("Helvetica", 24))
user_entry.pack(pady=20, padx=20)

pw_entry = Entry(root, text='', font=("Helvetica", 24))
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()"""
