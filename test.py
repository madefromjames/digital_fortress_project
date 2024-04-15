import tkinter as tk
import random

def create_input_frame(root):
    # Create the input frame and its widgets
    input_frame = tk.Frame(root, pady=20)
    input_frame.pack()

    word_label = tk.Label(input_frame, text='Word')
    word_label.pack()

    input_entry = tk.Entry(input_frame, width=20, bd=5)
    input_entry.pack()

    return input_frame, input_entry

def create_grid(root, input_entry):
    # Create the grid of buttons and its widgets
    grid_frame = tk.Frame(root)
    grid_frame.pack()

    letters = ['test', 'sink', 'hiss', 'when']  # List of words to be displayed
    word = random.choice(letters)
    letters = list(word.upper())  # Convert the word to uppercase and create a list of its letters
    random.shuffle(letters)  # Shuffle the letters randomly

    buttons = []  # List to store the button widgets
    for i, letter in enumerate(letters):
        # Create a button with the letter as its text
        button = tk.Button(grid_frame, text=letter, width=4, height=2, cursor="hand2")
        button.grid(row=7, column=i, padx=5, pady=5)  # Position the button in the grid
        button.config(command=lambda l=letter, btn=button, input_entry=input_entry: select_letter(l, btn, input_entry))
        buttons.append(button)  # Add the button to the list of buttons

    return grid_frame, buttons

def create_buttons(root):
    # Create the control buttons and their commands
    clear_button = tk.Button(root, text="Clear", command=clear_word)
    clear_button.pack()

    submit_button = tk.Button(root, text="Submit", command=submit_word)
    submit_button.pack()

def select_letter(letter, button, input_entry):
    # Function to handle when a letter button is clicked
    current_word = input_entry.get()  # Get the current word from the input entry
    current_word += letter  # Add the clicked letter to the current word
    input_entry.delete(0, tk.END)
    input_entry.insert(tk.END, current_word)

    if button not in selected_buttons:
        button.config(state=tk.DISABLED)
        selected_buttons.append(button)

def clear_word():
    # Function to clear the current word
    global current_word
    current_word = ""  # Clear the current word
    for button in buttons:
        button.config(state=tk.NORMAL)

def submit_word():
    # Function to handle when the Submit button is clicked
    print("Submitted word:", current_word)

# Initialize the tkinter root window
root = tk.Tk()
root.title("Word Shuffle")
root.geometry("312x324")

# Initialize the input frame and its widgets
input_frame, input_entry = create_input_frame(root)

# Initialize the grid of buttons and its widgets
grid_frame, buttons = create_grid(root, input_entry)

# Initialize the control buttons and their commands
create_buttons(root)

# Initialize the list of selected buttons
selected_buttons = []

# Start the tkinter event loop
root.mainloop()