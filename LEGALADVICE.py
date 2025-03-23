from tkinter import *
from tkinter import ttk
from aixplain.factories import PipelineFactory
import os

def legal_ad():
    win= Toplevel()
    win.title("Legal Advice")
    win.geometry("750x750")

    label_instruction = Label(win, text="What category query (ex: workplace abuse, marital abuse, etc)?", font=("Century Gothic", 14))
    label_instruction.pack(pady=10)

    bg = PhotoImage(file = "legal.png")
    label1 = Label( win, image = bg)
    label1.image = bg
    label1.place(x = 0, y = 0)

    global entry
    entry= Entry(win, width= 60)
    entry.focus_set()
    entry.pack(pady=10)
        
    def show_text():
        global entry
        user_input = entry.get()  # Get text from entry box
        model = PipelineFactory.get("67dc4b24338999cb9696981d")
         #What measures do you want information on?
        result = model.run({"Input 1": user_input})
        print(result)
        
    heading = Label(win, text="Legal Advice \nWhat category query? \n (ex: workplace abuse, marital abuse, etc)", font=("Century Gothic", 18, "bold"))
    heading.pack(pady=20)

    submitButton=ttk.Button(win, text= "Submit",width= 20, command= show_text)
    submitButton.pack(pady=20)

    win.mainloop()
    
legal_ad()
