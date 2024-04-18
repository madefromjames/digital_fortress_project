from tkinter import Tk, Button, Label, Entry, Frame, END, PhotoImage, LEFT
import random
from tkinter import messagebox

def main():

    # Function to display the start page
    def start_page():
        
        # Function to start the main game
        def main_game():

            # Create the main window
            window = Tk()
            window.geometry("500x500+500+100")
            window.resizable(0, 0)
            window.title("Word Shuffle Game")
            window.configure(background="#040402")
            window.iconbitmap(r'wordicon.ico')

            # Load the back button image
            # img1 = PhotoImage(file="back-btn.png")

            # MAIN GAME HERE 😊


            window.mainloop()

        # Function to show main game window
        def show_game():
            # Destroy the start page and start the main game
            main_window.destroy()
            main_game()

        # Create the main window for the start page
        main_window = Tk()
        main_window.geometry("500x500+500+100")
        main_window.resizable(0, 0)
        main_window.title("Word Game")
        main_window.configure(background="#040402")
        main_window.iconbitmap(r'wordicon.ico')

        # Load the image for the start page
        img0 = PhotoImage(file="wordgame.png")

        # Label to display the image
        image_label = Label(main_window, image=img0, bg="#040402")
        image_label.pack(pady=(50, 0))

        # Frame for creator information(made by FHFJ Squad)
        creator_label = Frame(main_window, bg="#040402")
        creator_label.pack()
        
        # Label for "made by"
        madeby_label = Label(creator_label, text="made by", pady=10, bg="#040402", fg="#decac0", font="dubai 13 bold")
        madeby_label.pack(side=LEFT)

        # Label for team name
        names_label = Label(creator_label, text="FHFJ Squad", pady=10, bg="#040402", fg="#decac0", font="Ravie 13 bold")
        names_label.pack(side=LEFT)

        # Start button
        start_btn = Button(main_window, text="Start", width=14, bd=4, bg="#ad8d76", font=("", 10, 'bold',), cursor="hand2", command=show_game)
        start_btn.pack(pady=(35, 10))

        # Exit button
        exit_btn = Button(main_window, text="Exit", width=14, bd=4, bg="#ad8d76", font=("", 10, 'bold',), cursor="hand2", command=lambda: main_window.destroy() if messagebox.askyesno('Exit', 'Are you sure you want to exit?') else None)
        exit_btn.pack(pady=(10))

        main_window.mainloop()

    # Call the start page function
    start_page()

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
