import tkinter as tk

class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.resizable(False, False)

        self.expression = ""
        self.entry_text = tk.StringVar()
        self.entry_text.set("0")

        entry = tk.Entry(self, textvariable=self.entry_text, font=("Arial", 20), bd=5,
                         relief=tk.RIDGE, justify="right")
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

        buttons = [
            ("7","8","9","/"),
            ("4","5","6","*"),
            ("1","2","3","-"),
            ("0",".","=","+"),
        ]

        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                action = lambda ch=char: self.on_button_click(ch)
                tk.Button(self, text=char, width=4, height=2, font=("Arial", 18),
                          command=action).grid(row=r, column=c, padx=5, pady=5)

        # Add Clear button
        tk.Button(self, text="C", width=4, height=2, font=("Arial", 18),
                  bg="#f77", fg="white", command=self.clear).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.entry_text.set(result)
                self.expression = result
            except Exception:
                self.entry_text.set("Error")
                self.expression = ""
        else:
            if self.entry_text.get() == "0" and char not in "+-*/.":
                self.expression = char
            else:
                self.expression += char
            self.entry_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.entry_text.set("0")

if __name__ == "__main__":
    SimpleCalculator().mainloop()
