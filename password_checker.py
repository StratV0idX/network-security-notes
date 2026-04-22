# Simple Password Strength Checker
# Original Author: Shannel Segwabe
# Contributor: Roshan Jeffrin R
# Changes: Added scoring system, improved validation, user feedback

import re, os
from tkinter import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # path of this code
logo_path = os.path.join(BASE_DIR, "assets", "icon.ico")  # path of icon file
wordlist_path = os.path.join(BASE_DIR, "assets", "wordlist.txt")

common_passwords = set()


def load_wordlist():
    global common_passwords
    try:
        with open(wordlist_path, "r", encoding="latin-1") as f:
            common_passwords = set(line.strip() for line in f)
    except FileNotFoundError:
        common_passwords = set()


def check_password_strength(password):
    score = 0
    feedback = []

    if password in common_passwords:
        feedback.append("Common password detected (found in wordlist)")
        return 0, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add number")

    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1
    else:
        feedback.append("Add special character")

    return score, feedback


def get_strength(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def analyze():
    password = e.get()

    if not password.strip():
        result_label.config(text="Password cannot be empty", font=("Arial", 12))
        return

    score, feedback = check_password_strength(password)
    strength = get_strength(score)

    if strength == "Strong":
        color = "green"
    elif strength == "Medium":
        color = "orange"
    else:
        color = "red"

    output = f"Strength: {strength}\nScore: {score}/5\n"

    if feedback:
        output += "\nSuggestions:\n"
        for f in feedback:
            output += f"- {f}\n"

    result_label.config(text=output, font=("Arial", 12), fg=color)


# Initiating Frame
frame = Tk()
frame.title("Password Checker")
frame.iconbitmap(logo_path)
frame.geometry("350x330")

load_wordlist()

Label(frame, text="Password Checker", font=("Arial", 30)).pack()
Label(frame, text="Password: ", font=("Arial", 12)).pack()
e = Entry(frame, width=25)
e.pack()
Button(frame, text="ANALYSE", command=analyze).pack()

result_label = Label(frame, text="", justify="left", wraplength=300)
result_label.pack()
frame.mainloop()
