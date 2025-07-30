import json
import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image
from src.apis.client import generate_random_facts
from src.storage.saved_facts import load_Facts, dump_fact
from src.utils.ttsx import say
import threading


def launch_app():
    # Create main window
    root = tk.Tk()
    root.title("Factastic")
    root.configure(bg="#2C3E50")
    root.geometry("500x500")
    root.resizable(False, False)

    mute = True
    temporary_facts = []

    # Essa função preeche a lista com factos temporários para deixar o app mais r;ápido (enquanto mostra factos faz requests)
    def preload_facts(count=5):
        for _ in range(count):
            fact = generate_random_facts()
            if fact not in temporary_facts:
                temporary_facts.append(fact)

    preload_facts()

    # Function to get the next fact and update the label
    def next_fact():
        nonlocal temporary_facts
        if not temporary_facts:
            preload_facts()

        fact = temporary_facts.pop(0)
        text_label.config(text=fact)
        threading.Thread(target=say, args=(fact,), daemon=True).start()

        # Recarrega mais factos em segundo plano se o buffer estiver quase vazio
        if len(temporary_facts) < 3:
            threading.Thread(target=preload_facts, daemon=True).start()

    def like_save_fact():
        saved_facts = load_Facts()
        fact = text_label.cget("text")
        if fact and fact != "Click 'Next Fact' to start!":
            dump_fact(saved_facts, fact)

    # Create a frame for the title area
    app_title_lf = tk.LabelFrame(root, text="", bg="#2C3E50", width=30, height=50, bd=0)
    app_title_lf.pack(side="top", fill="x")

    # Load and show the logo image
    img = PhotoImage(file="src/assets/brain.png")
    label_img = tk.Label(app_title_lf, image=img, bg="#2C3E50")
    label_img.image = img  # keep a reference to avoid garbage collection
    label_img.place(x=10, y=5)

    # Show the app title text
    label_txt = tk.Label(app_title_lf, text="Factastic", font=("Segoe UI", 14, "bold"), bg="#2C3E50", fg="#ECF0F1")
    label_txt.place(x=50, y=5)

    # Create settings button
    setting_img = PhotoImage(file="src/assets/setting.png")
    btn_setting = tk.Button(app_title_lf, image=setting_img, bg="#2C3E50", relief="groove", bd=0)
    btn_setting.place(x=450, y=5)

    # Load and display the "Did you know" image
    response_img = PhotoImage(file="src/assets/did-you-know.png")
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
    btn_fav = tk.Button(root,
                        text="Like and Save",
                        width=40,
                        bg="#F39C12",
                        fg="#ECF0F1",
                        font=("Segoe UI", 10, "bold"),
                        command=like_save_fact)
    btn_fav.place(x=90, y=400)

    root.bind("<Return>", lambda event: next_fact())

    root.mainloop()