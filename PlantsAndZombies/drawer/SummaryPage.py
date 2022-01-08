import tkinter as tk


class SummaryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Summary Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Restart Game",
                            command=lambda: controller.show_frame("StartPage"))
        button1.pack(side='bottom')
