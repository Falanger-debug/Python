import tkinter as tk
import random

def close_app():
    root.destroy()

def roll_dice():
    result = random.randint(1, 6)
    label_result.config(image=images[result - 1])

root = tk.Tk()
root.title("Dice Roller")
root.attributes("-fullscreen", True)

dice_empty = tk.PhotoImage(file="images/dice_empty.png")
images = [tk.PhotoImage(file=f"images/dice_{i}.png") for i in range(1, 7)]

label_result = tk.Label(root)
label_result.pack(pady=20)
label_result.config(image=dice_empty)

button_roll = tk.Button(root, text="Roll a dice", font=("Arial", 14), command=roll_dice, bg="blue", fg="white")
button_roll.pack(pady=10)

button_close = tk.Button(root, text="Close", font=("Arial", 14), command=close_app, bg="red", fg="white")
button_close.pack(pady=10)

root.mainloop()
