import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image
from src.apis.client import generate_random_facts

def launch_app():
    # Create main window
    root = tk.Tk()
    root.title("Factastic")
    root.configure(bg="#2C3E50")
    root.geometry("500x500")
    root.resizable(False, False)

    # Try to load and set the app icon
    try:
        img = Image.open("assests/brain.png")
        img = img.resize((64, 64))
        icon = ImageTk.PhotoImage(img)
        root.wm_iconphoto(True, icon)
    except:
        print("Erro!")

    # Function to get the next fact and update the label
    def next_fact():
        fact = generate_random_facts()
        text_label.config(text=fact)

    # Create a frame for the title area
    app_title_lf = tk.LabelFrame(root, text="", bg="#2C3E50", width=30, height=50, bd=0)
    app_title_lf.pack(side="top", fill="x")

    # Load and show the logo image
    img = PhotoImage(file="assests/brain.png")
    label_img = tk.Label(app_title_lf, image=img, bg="#2C3E50")
    label_img.image = img  # keep a reference to avoid garbage collection
    label_img.place(x=10, y=5)

    # Show the app title text
    label_txt = tk.Label(app_title_lf, text="Factastic", font=("Segoe UI", 14, "bold"), bg="#2C3E50", fg="#ECF0F1")
    label_txt.place(x=50, y=5)

    # Load and display the "Did you know" image
    response_img = PhotoImage(file="assests/did-you-know.png")
    response_img_label = tk.Label(root, image=response_img, bg="#2C3E50")
    response_img_label.image = response_img  # keep reference
    response_img_label.place(x=50, y=60)

    # Create a frame to show the fact text
    responses_lf = tk.LabelFrame(root, width=400, height=120, bg="#ECF0F1")
    responses_lf.place(x=55, y=145)

    # Label to display the fact text, starts with a welcome message
    global text_label
    text_label = tk.Label(
        responses_lf,
        text="Click 'Next Fact' to start!",
        wraplength=380,
        justify="left",
        bg="#ECF0F1",
        fg="#2C3E50",
        font=("Segoe UI", 11)
    )
    text_label.place(x=15, y=18)

    # Button to get the next fact
    btn_next = tk.Button(root, text="Next Fact", width=40, bg="#6C5CE7", fg="#ECF0F1",
                         font=("Segoe UI", 10, "bold"), command=next_fact)
    btn_next.place(x=90, y=340)

    # Button to like and save a fact
    btn_fav = tk.Button(root, text="Like and Save", width=40, bg="#F39C12", fg="#ECF0F1",
                        font=("Segoe UI", 10, "bold"))
    btn_fav.place(x=90, y=400)


    root.mainloop()
