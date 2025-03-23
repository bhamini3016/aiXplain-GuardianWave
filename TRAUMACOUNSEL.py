from tkinter import *
from tkinter import ttk
from aixplain.factories import PipelineFactory
import os
def open_ts():
    win= Toplevel()
    win.title("Trauma Support")
    win.geometry("750x750")

    bg = PhotoImage(file = "trauma.png")
    label1 = Label( win, image = bg)
    label1.image = bg
    label1.place(x = 0, y = 0)
      
    heading = Label(win, text="Trauma Support", font=("Century Gothic", 24, "bold"))
    heading.pack(pady=20)

    trauma=Label(win, text="How can I support you?", font=("Century Gothic", 20, "italic"))
    trauma.pack(pady=30)

    global entry
    entry= Entry(win, width= 60)
    entry.focus_set()
    entry.pack(pady=10)
    
    def show_text():
        
        global entry
        user_input = entry.get()  # Get text from entry box
        model = PipelineFactory.get("67d6f3eb8e9326b58bc21413")
        result = model.run({"Input 1": user_input})
        print(result)

    submitButton=ttk.Button(win, text= "Submit",command=show_text,width= 20)
    submitButton.pack(pady=20)

    win.mainloop()
    show_text()

open_ts()
