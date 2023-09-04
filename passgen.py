import tkinter as tk

import random

import string

 

def generate_password():

    password_length = 12  

    password_characters = ""

    if use_letters.get():

        password_characters += string.ascii_letters

    if use_numbers.get():

        password_characters += string.digits

    if use_special_chars.get():

        password_characters += string.punctuation

 

    if not password_characters:

        result_label.config(text="Please select at least one option.", fg="red")

        return

 

    password = ''.join(random.choice(password_characters) for _ in range(password_length))

    password_entry.delete(0, tk.END)

    password_entry.insert(0, password)

    result_label.config(text="Password Generated:", fg="green")

root = tk.Tk()

root.title("Password Generator")

root.configure(bg="#3498db")  

#  radio buttons

use_letters = tk.BooleanVar()

use_numbers = tk.BooleanVar()

use_special_chars = tk.BooleanVar()

 

letters_radiobutton = tk.Radiobutton(root, text="Letters", variable=use_letters, value=True, bg="#3498db", fg="white")

letters_radiobutton.pack()

letters_radiobutton.select()

 

numbers_radiobutton = tk.Radiobutton(root, text="Numbers", variable=use_numbers, value=True, bg="#3498db", fg="white")

numbers_radiobutton.pack()

 

special_chars_radiobutton = tk.Radiobutton(root, text="Special Characters", variable=use_special_chars, value=True, bg="#3498db", fg="white")

special_chars_radiobutton.pack()

 

# Button Created

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#e74c3c", fg="white")

generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#3498db", fg="black")

result_label.pack(pady=10)

password_entry = tk.Entry(root, width=20, font=("Helvetica", 14))

password_entry.pack(pady=10)

root.mainloop()