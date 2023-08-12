import tkinter as tk
import random

class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")

        self.label = tk.Label(root, text="WELCOME", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 20))
        self.result_label.pack()

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice, font=("Helvetica", 12))
        self.roll_button.pack(pady=10)

    def roll_dice(self):
        dice_result = random.randint(1, 6)
        self.result_label.config(text=f"Rolled: {dice_result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()
