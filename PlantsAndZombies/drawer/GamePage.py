import tkinter as tk


class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Game Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Summary", command=lambda: controller.show_frame("SummaryPage"))
        button1.pack(side='bottom')
