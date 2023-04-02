import tkinter as tk
from tkinter import filedialog
import re

class Editor:
    def __init__(self, master):
        # Initialize the text area
        self.textarea = tk.Text(master, font=('Courier New', 14))
        self.textarea.pack(expand=True, fill='both')

        # Create the menu bar
        menubar = tk.Menu(master)
        master.config(menu=menubar)

        # Create the File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='New', command=self.new_file)
        filemenu.add_command(label='Open...', command=self.open_file)
        filemenu.add_command(label='Save', command=self.save_file)
        filemenu.add_command(label='Save As...', command=self.save_file_as)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=master.quit)
        menubar.add_cascade(label='File', menu=filemenu)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.linenumbers.config(state="normal")
        self.linenumbers.delete(1.0, tk.END)
        self.linenumbers.insert(1.0, "1")
        self.linenumbers.config(state="disabled")
        self.filename = None

    def open_file(self):
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
        filename = filedialog.askopenfilename(title="Open File", filetypes=filetypes)
        if filename:
            with open(filename, "r") as f:
                text = f.read()
                self.textarea.delete(1.0, tk.END)
                self.textarea.insert(1.0, text)
                self.update_linenumbers()
            self.filename = filename

    def save_file(self):
        if self.filename:
            text = self.textarea.get(1.0, tk.END)
            with open(self.filename, "w") as f:
                f.write(text)
        else:
            self.save_file_as()

    def save_file_as(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            text = self.textarea.get(1.0, tk.END)
            with open(filename, "w") as f:
                f.write(text)
            self.filename = filename
            self.update_linenumbers()
    def update_linenumbers(self):
        self.linenumbers.config(state="normal")
        self.linenumbers.delete(1.0, tk.END)
        text = self.textarea.get(1.0, tk.END)
        lines = text.split("\n")
        for i in range(1, len(lines)+1):
            self.linenumbers.insert(tk.END, str(i)+"\n")
        self.linenumbers.config(state="disabled")

    def on_key(self, event):
        self.update_linenumbers()

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

    def quit(self):
        self.master.quit()

root = tk.Tk()
editor = Editor(root)
root.mainloop()
