# from tkinter import *
# imports all public classes, functions, and variables from the tkinter module 
# You don’t need to prefix Tkinter classes or functions with tk.. but
# It imports everything and can lead to naming conflicts 
# choose: import tkinter as tk

import tkinter as tk
from tkinter import messagebox
import webbrowser
import random


def show_custom_warning(message):
	warning = tk.Toplevel(root)
	warning.title("Warning")
	warning.geometry("300x150")
	warning.configure(bg="grey")
	label = tk.Label(warning, text=message, bg="grey", font=('Helvetica', 10))
	label.pack(pady=10)
	ok_button = tk.Button(warning, text="OK", command=warning.destroy, bg="grey", fg="black")
	ok_button.pack(pady=10)
	warning.grab_set() #interactive window
	root.wait_window(warning)#parent window waits for a child

def show_custom_information(message):
	information = tk.Toplevel(root)
	information.geometry("400x300")
	information.configure(bg="hotpink")
	label = tk.Label(information, text=message, bg="hotpink", font=('Helvetica', 12), wraplength=300, justify="center")
	label.pack(pady=10)
	ok_button = tk.Button(information, text="OK", command=information.destroy, bg="white", fg="black")
	ok_button.pack(pady=10)
	information.grab_set() 
	root.wait_window(information)

def start_game():
	start_button.pack_forget()
	github_button.pack_forget()
	input_frame.pack(expand=True, fill="both")

def open_git():
	url = "https://github.com/akrepkov"
	webbrowser.open(url)

def check_guess():
	guess = entry.get().strip()
	if len(guess) != 2 or not guess.isdigit():
		show_custom_warning("Invalid input\n")
		return
	else:
		secret_number = str(random.randint(00, 99)).zfill(2)
		input_frame.pack_forget()
		if guess == secret_number:
			message = f"Congratulations! You've guessed the number {secret_number}."
		else:
			message = f"Try Again! Wrong guess. The secret number was {secret_number}."
		show_custom_information(message)
		entry.delete(0, tk.END)
		input_frame.pack(expand=True, fill="both")

def give_up():
	root.destroy()

root = tk.Tk()
root.title("Guess the Number")
root.geometry("600x600")
root.configure(background="pink")

#It acts as a parent widget that can be used to group related widgets together
#rames can be used to apply layout management methods (pack, grid, or place) to a set of widgets as a single unit. 
start_frame = tk.Frame(root, bg="pink")
start_frame.pack(expand=True)
start_button = tk.Button(start_frame, text="Start Game", width=20, height=2, bg="white", fg="black", command=start_game)
start_button.pack()
github_button = tk.Button(start_frame, text="Check the Code", width=20, height=2, bg="white", fg="black", command=open_git)
github_button.pack(pady=10)

#Second frame for input window, consist of directions, input, check and give up buttons
input_frame = tk.Frame(root, bg="pink")
submit_label = tk.Label(input_frame, text="Enter your guess (a 2-digit number):", bg="pink")
submit_label.pack()
entry = tk.Entry(input_frame, width=20, font=('Helvetica', 18))
entry.pack(pady=10)
check_button = tk.Button(input_frame, text="Play", width=20, height=2, bg="white", fg="black", command=check_guess)
check_button.pack(pady=10)
give_up_button = tk.Button(input_frame, text="Give up", width=10, height=1, bg="grey", fg="black", command=give_up)
give_up_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)
# Create and pack the submit button (initially hidden)
# Start the Tkinter event loop
root.mainloop()

