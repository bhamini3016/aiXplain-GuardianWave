import tkinter as tk
from aixplain.factories import PipelineFactory
import os


    # Create main window
root = tk.Tk()
root.title("User Input Window")
root.geometry("600x400")  # Set window size

    # Label for instruction
label_instruction = tk.Label(root, text="What measures do you want information on?", font=("Century Gothic", 14))
label_instruction.pack(pady=10)

    # Entry box for user input
global entry
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=5)

def show_text():
    global entry
    user_input = entry.get()  # Get text from entry box
    model = PipelineFactory.get("67d6f3eb8e9326b58bc21413")
     #What measures do you want information on?
    result = model.run({"Input 1": user_input})
    print(result)

    # Button to submit input
btn_submit = tk.Button(root, text="Submit", command=show_text, font=("Century Gothic", 12), bg="lightblue")
btn_submit.pack(pady=10)

    
    # Label to display output
label_output = tk.Label(root, text="", font=("Arial", 14), fg="green")
label_output.pack(pady=10)

    # Run the window
root.mainloop()
show_text()

    
