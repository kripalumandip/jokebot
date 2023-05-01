# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "jokebot.py" program of Assignment 2
# of CSI6208 in Semester 1, 2023.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter as tk
import tkinter.messagebox
import tkinter.font as font
import json
from tkinter import messagebox


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data file and creating the user interface.
        # See Points 1 to 4 "Requirements of jokebot.py" section of the assignment brief. 
        try:
            # open the JSON file and load the data
            with open("data.txt", "r") as f:
                self.data = json.load(f)

            # set the current joke index to 0
            self.currentJoke = 0

            # TODO: add the rest of the GUI code here

        except (FileNotFoundError, json.JSONDecodeError):
            # show an error message box and destroy the main window
            # messagebox.showerror("Error", "Missing/Invalid file")
            # self.root.destroy()

            # halt the constructor so that the program ends cleanly
            return

        # create the main window
        self.root = tk.Tk()
        self.root.title("Joke Bot")
        self.root.geometry("600x450")

        self.currentJoke = 0

        #add widget and other things
        #Create a custom font
        custom_font = font.Font(size=20)
        #joke setup at top
        self.joke_setup = tkinter.StringVar()
        self.welcomeMessage = tkinter.Label(self.root, textvariable=self.joke_setup)
        self.welcomeMessage['font'] = custom_font
        self.welcomeMessage.pack(padx=10,pady=50)

        #punchline
        self.joke_punchline = tkinter.StringVar()
        self.welcomeMessage = tkinter.Label(self.root, textvariable = self.joke_punchline)
        self.welcomeMessage['font'] = custom_font
        self.welcomeMessage.pack(padx=10,pady=10)

        #number of ratings
        self.joke_numOfRatings = tkinter.StringVar()
        if int(self.data[self.currentJoke]["sumOfRatings"]) == 0:
            self.number = tkinter.Label(self.root, text="Joke has not been rated.")
        else:
            self.number = tkinter.Label(self.root, textvariable = self.joke_numOfRatings)
        self.number['font'] = font.Font(size=12)
        self.number.pack()

        #sum of ratings
        self.joke_sumOfRatings = tkinter.StringVar()
        self.average = tkinter.Label(self.root, textvariable = self.joke_sumOfRatings)
        self.average['font'] = font.Font(size=12)
        self.average.pack(padx=5,pady=5)

        #Your rating
        self.welcomeMessage = tkinter.Label(self.root, text='Your Rating:')
        self.welcomeMessage['font'] = font.Font(size=12)
        self.welcomeMessage.pack(padx=10,pady=10)
        #entry
        self.demoEntry = tkinter.Entry(self.root, width=15)
        self.demoEntry.pack()
        self.demoEntry.focus_set()  # Set focus to the rating entry widget

        #Submit button
        self.button = tkinter.Button(self.root, text="Submit", command=self.rateJoke)
        self.button['font'] = font.Font(size=12)

        self.button.pack(padx=10,pady=10)

        self.showJoke()

        # start the main event loop
        self.root.mainloop()

    def showJoke(self):
        # This method is responsible for displaying a joke in the GUI.
        # See Point 1 of the "Methods in the GUI class of jokebot.py" section of the assignment brief.
        setup = self.data[self.currentJoke]["setup"]
        self.joke_setup.set(setup)
        punchline = self.data[self.currentJoke]["punchline"]
        self.joke_punchline.set(punchline)
        numOfRatings = self.data[self.currentJoke]["numOfRatings"]
        if numOfRatings == 0:
            pass
        else:
            numOfRatings = str(numOfRatings)
            self.joke_numOfRatings.set("Rated "+ numOfRatings + " time(s).")
            sumOfRatings = self.data[self.currentJoke]["sumOfRatings"]
            average = int(sumOfRatings)/int(numOfRatings)
            average = round(average,1)
            average = str(average)
            self.joke_sumOfRatings.set("Average rating is " + average + "/5.")






    def rateJoke(self):
        # This method is responsible for validating and recording the rating that a user gives a joke.
        # See Point 2 of the "Methods in the GUI class of jokebot.py" section of the assignment brief.

        #validatain from 1 to 5
        try:
            rating = int(self.demoEntry.get())
            if rating < 1 or rating > 5:
                messagebox.showerror("Error", "Rating must be between 1 and 5.")
                return
            # Update the joke's rating data
            self.data[self.currentJoke]["numOfRatings"] = int(self.data[self.currentJoke]["numOfRatings"])
            self.data[self.currentJoke]["numOfRatings"] += 1
            self.data[self.currentJoke]["sumOfRatings"] = int(self.data[self.currentJoke]["sumOfRatings"])
            self.data[self.currentJoke]["sumOfRatings"] += rating
            # Write the data to file
            with open("data.txt", "w") as f:
                json.dump(self.data, f)
            messagebox.showinfo("Success", f"You rated the joke {rating} out of 5.")
        except ValueError:
            messagebox.showerror("Error", "Please enter an integer between 1 and 5.")
        #Move to next joke
        if self.currentJoke == len(self.data) - 1: # check if the current joke is the last one
            messagebox.showinfo("End of Jokes", "You have rated all the jokes! Thanks for playing!")
            self.root.destroy() # end the program
        else:
            self.currentJoke += 1 # move on to the next joke
            self.demoEntry.delete(0, "end") # clear the rating entry widget
            self.showJoke() # show the next joke


    

# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
