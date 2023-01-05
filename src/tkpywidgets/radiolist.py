import tkinter as tk
from tkinter import ttk


# A list of checkbuttons that can be selected and deselected by code or user
class Radiolist(tk.LabelFrame):

    # Creates the checkbuttons from listvariable and adds them to the frame
    def __init__(self, parent, options: list, title: str = None, command: str = None, **kwargs):
        tk.LabelFrame.__init__(self, parent, text=title, **kwargs)

        self.parent = parent
        self.command = command

        self.frame = self.edit_frame = tk.Frame(self)

        self.frame.grid(row=0, column=0)
        self.choice = tk.StringVar(value=options[0])

        self.radiobuttons = {}

        for option in options:
            rb = tk.Radiobutton(self.edit_frame, variable=self.choice, text=option, value=option, anchor="w")

            if self.command:
                rb['command'] = (lambda parent=self.parent, command=self.command, button=rb: self.run_command(parent, command, button))

            rb.grid(row=len(self.radiobuttons), column=0, sticky='w')
            self.radiobuttons[option] = rb


    # Returns a list of the values of the checked buttons
    def get_choice(self):
        return self.choice.get()

    def add_items(self, items: list):
        for item in items:
            rb = tk.Radiobutton(self.edit_frame, variable=self.choice, text=item, value=item, anchor="w")

            rb.grid(row=len(self.radiobuttons), column=0, sticky='w')
            self.radiobuttons[item] = rb

    def remove_items(self, items: list):
        for item in items:
            if item in self.radiobuttons.keys():
                self.radiobuttons[item].grid_forget()
                self.radiobuttons.pop(item)

    def remove_all_items(self):
        for item in self.radiobuttons.keys():
            item.grid_forget()
        self.radiobuttons = {}

    # Selects a button
    def select(self, item:str):
        if item in self.radiobuttons.keys():
            self.choice.set(item)

    def run_command(self, parent, command, button):
        button.focus_set()
        func = getattr(parent, command)
        func(button['text'])