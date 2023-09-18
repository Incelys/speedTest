import tkinter as tk

class Window:
    def __init__(self, title, color):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.configure(bg=color)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

    def set_result_text(self, text):
        self.result_label.configure(text=text)

    def set_result_text_color(self, color):
        self.result_label.configure(fg=color)

    def run(self):
        self.window.mainloop()