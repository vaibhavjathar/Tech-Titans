from tkinter import *
from textblob import TextBlob

def check_spelling():
    a = TextBlob(spell_check.get())
    spell = Label(window, text="The correct spelling is: ", font=("Arial", 20, "bold"))
    spell.pack()
    correct_text = Label(window, text=str(a.correct()), font=("Arial", 20, "bold"), fg="white", bg="lightgreen")
    correct_text.pack()
    

window = Tk()
window.title("My Spelling Checker")
window.geometry("800x600")
window.config(background="lightblue")

text_heading = Label(window, text="Spelling check", font=("Arial", 40, "bold"), bg="black", fg="white")
text_heading.pack()

t_check = Label(window, text="Enter the spelling:", font=("Arial", 20, "bold"), fg="red")
t_check.pack()

spell_check = Entry(window, font=("Arial", 20, "bold"), width=100, bg="white")
spell_check.pack()

Check_button = Button(window, text="Check!", font=("Arial", 15, "bold"), fg="white", bg="red", command=check_spelling)
Check_button.pack()

window.mainloop()