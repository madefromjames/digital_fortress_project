import tkinter as tk
import random

class WordShuffle:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Shuffle")
        self.root.geometry("312x324")

        self.grid_size = 4
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.current_word = ""
        
        self.input_frame()
        self.create_grid()
        self.create_buttons()

    def input_frame(self):
        pass
        
    def create_grid(self):
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack()

        self.buttons = []
        for _ in range(self.grid_size):
            row = []
            for _ in range(self.grid_size):
                letter = random.choice(self.letters)
                button = tk.Button(self.grid_frame, text=letter, width=4, height=2, command=lambda letter=letter: self.select_letter(letter))
                button.grid(row=7, column=_, padx=5, pady=100)
                row.append(button)
            self.buttons.append(row)

    def create_buttons(self):
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_word)
        self.clear_button.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_word)
        self.submit_button.pack()

    def select_letter(self, letter):
        self.current_word += letter

    def clear_word(self):
        pass

    def submit_word(self):
        pass

def main():
    win = tk.Tk()
    game = WordShuffle(win)
    win.mainloop()

if __name__ == "__main__":
    main()
