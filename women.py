import tkinter as tk
from PIL import Image, ImageTk

def legal_advice():
    import LEGALADVICE

def trauma_support():
    import TRAUMACOUNSEL

def safety_measures():
    import SAFETYMEASURES

def self_defense():
    """Change the background and remove all widgets when Self-Defense is clicked."""
    global bg_photo, new_bg_photo

    for widget in root.winfo_children():
        if widget != canvas:
            widget.destroy()

    canvas.itemconfig(bg_canvas_image, image=new_bg_photo)

def create_buttons():
    global root, canvas, bg_canvas_image, bg_photo, new_bg_photo

    root = tk.Tk()
    root.title("Guardian Wave")
    root.state("zoomed")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    bg_image = Image.open("bg.png").resize((screen_width, screen_height), Image.LANCZOS)
    new_bg_image = Image.open("Video.png").resize((screen_width, screen_height), Image.LANCZOS)

    bg_photo = ImageTk.PhotoImage(bg_image) 
    new_bg_photo = ImageTk.PhotoImage(new_bg_image) 

    canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="#B4A7D6")
    canvas.pack(fill="both", expand=True)

    bg_canvas_image = canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    title_label = tk.Label(root, text="Guardian Wave", font=("Century Gothic", 24, "bold"), bg="#B4A7D6")
    title_label.place(relx=0.5, y=50, anchor="center")

    frame1 = tk.Frame(root, bg="#B4A7D6")
    frame1.place(relx=0.5, rely=0.30, anchor="center")

    frame2 = tk.Frame(root, bg="#B4A7D6")
    frame2.place(relx=0.5, rely=0.55, anchor="center")

    btn_legal = tk.Button(frame1, text="Legal Advice", command=legal_advice, width=15, height=5, bg="pink", font=("Century Gothic", 18, "bold"))
    btn_legal.pack(side=tk.LEFT, padx=10)

    btn_trauma = tk.Button(frame1, text="Trauma Support", command=trauma_support, width=15, height=5, bg="pink", font=("Century Gothic", 18, "bold"))
    btn_trauma.pack(side=tk.LEFT, padx=10)

    btn_safety = tk.Button(frame2, text="Safety Measures", command=safety_measures, width=15, height=5, bg="pink", font=("Century Gothic", 18, "bold"))
    btn_safety.pack(side=tk.LEFT, padx=10)

    btn_defense = tk.Button(frame2, text="Self-Defense", command=self_defense, width=15, height=5, bg="pink", font=("Century Gothic", 18, "bold"))
    btn_defense.pack(side=tk.LEFT, padx=10)

    root.mainloop()

create_buttons()
