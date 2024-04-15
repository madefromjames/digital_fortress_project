import tkinter as tk
import random

class WordShuffle:
    def __init__(self, root):
        # Initialize the WordShuffle class with a tkinter root window
        self.root = root
        self.root.title("Word Shuffle")  # Set the title of the window
        self.root.geometry("312x324")    # Set the size of the window

        # Define the properties of the game
        self.grid_size = 4  # Number of buttons in a row
        self.letters = ['test', 'sink', 'hiss', 'when']  # List of words to be displayed
        self.current_word = ""  # Store the current word being formed
        
        # Create the input frame, grid of buttons, and control buttons
        self.create_input_frame()  
        self.create_grid()
        self.create_buttons()

    def create_input_frame(self):
        # Placeholder for any input frame widgets you want to add
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        self.word_label = tk.Label(self.input_frame, text='Word')
        self.word_label.pack()

        self.input_entry = tk.Entry(self.input_frame, width=20, bd=6)
        self.input_entry.pack()
        
    def create_grid(self):
        # Create a frame to hold the grid of buttons
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack()

        # Randomly choose a word from the list and shuffle its letters
        word = random.choice(self.letters)
        letters = list(word.upper())  # Convert the word to uppercase and create a list of its letters
        random.shuffle(letters)  # Shuffle the letters randomly

        self.buttons = []  # List to store the button widgets
        # Create buttons for each letter in the shuffled word
        for i, letter in enumerate(letters):
            # Add an empty row for spacing between buttons and any other widgets above
            tk.Label(self.grid_frame, text="").grid(row=6)
            # Create a button with the letter as its text
            button = tk.Button(self.grid_frame, text=letter, width=4, height=2, command=lambda l=letter: self.select_letter(l))
            button.grid(row=7, column=i, padx=5, pady=5)  # Position the button in the grid
            self.buttons.append(button)  # Add the button to the list of buttons

    def create_buttons(self):
        # Create control buttons for the game
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_word)
        self.clear_button.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_word)
        self.submit_button.pack()

    def select_letter(self, letter):
        # Function to handle when a letter button is clicked
        self.current_word += letter  # Add the clicked letter to the current word

    def clear_word(self):
        # Function to clear the current word
        self.current_word = ""  # Clear the current word

    def submit_word(self):
        # Function to handle when the Submit button is clicked
        pass  # Placeholder for submitting the word

    # Lets work on a new game with no classes

def main():
    # Create the tkinter root window and initialize the WordShuffle game
    win = tk.Tk()
    game = WordShuffle(win)
    win.mainloop()  # Start the tkinter event loop

if __name__ == "__main__":
    main()
