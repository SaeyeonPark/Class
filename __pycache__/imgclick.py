from tkinter import *
from tkinter import messagebox

def clickImage(event) :
    messagebox.showinfo("마우스", "고양이에서 마우스가 클릭됨")

window = Tk()
window.geometry("400x400")

photo = PhotoImage(file="C:\Users\saeyo\OneDrive\바탕 화면\2\AI\AICLASS\cat.gif")
label1 = Label(window, image=photo)

Label1.bind("<Button>", clickImage)

Label1.pack(expand = 1, anchor = CENTER)
window.mainloop()