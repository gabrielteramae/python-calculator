import tkinter as tk
from tkinter import ttk

BG = "#0c1024"
PANEL = "#1b2038"
BTN = "#262c4a"
BTN_OP = "#ffb84d"
BTN_OP_TEXT = "#0c1024"
BTN_EQ = "#5b8def"
FG = "#e7ecf3"
FG_DIM = "#aab3c8"

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.expression = ""
        self.setup_style()
        self.build_display()
        self.build_buttons()

    def setup_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Digit.TButton", background=BTN, foreground=FG, font=("Helvetica", 18), borderwidth=0)
        style.map("Digit.TButton", background=[("active", BTN)])

        style.configure("Op.TButton", background=BTN_OP, foreground=BTN_OP_TEXT, font=("Helvetica", 18, "bold"), borderwidth=0)
        style.map("Op.TButton", background=[("active", BTN_OP)])

        style.configure("Eq.TButton", background=BTN_EQ, foreground=FG, font=("Helvetica", 18, "bold"), borderwidth=0)
        style.map("Eq.TButton", background=[("active", BTN_EQ)])

    def build_display(self):
        frame = tk.Frame(self, bg=BG, padx=20, pady=20)
        frame.grid(row=0, column=0, sticky="nsew")

        self.history_var = tk.StringVar(value="")
        history_label = tk.Label(
            frame, textvariable=self.history_var, anchor="e",
            bg=BG, fg=FG_DIM, font=("Helvetica", 14)
        )
        history_label.pack(fill="x")

        self.display_var = tk.StringVar(value="0")
        display_label = tk.Label(
            frame, textvariable=self.display_var, anchor="e",
            bg=BG, fg=FG, font=("Helvetica", 42, "bold")
        )
        display_label.pack(fill="x", pady=(4, 0))

    def build_buttons(self):
        grid_frame = tk.Frame(self, bg=PANEL, padx=16, pady=16)
        grid_frame.grid(row=1, column=0, sticky="nsew")

        buttons = [
            ("C", 0, 0, self.clear), ("±", 0, 1, self.negate), ("%", 0, 2, self.percent), ("÷", 0, 3, lambda: self.add_operator("/")),
            ("7", 1, 0, lambda: self.add_digit("7")), ("8", 1, 1, lambda: self.add_digit("8")), ("9", 1, 2, lambda: self.add_digit("9")), ("×", 1, 3, lambda: self.add_operator("*")),
            ("4", 2, 0, lambda: self.add_digit("4")), ("5", 2, 1, lambda: self.add_digit("5")), ("6", 2, 2, lambda: self.add_digit("6")), ("−", 2, 3, lambda: self.add_operator("-")),
            ("1", 3, 0, lambda: self.add_digit("1")), ("2", 3, 1, lambda: self.add_digit("2")), ("3", 3, 2, lambda: self.add_digit("3")), ("+", 3, 3, lambda: self.add_operator("+")),
            ("0", 4, 0, lambda: self.add_digit("0")), (",", 4, 1, self.add_decimal), ("⌫", 4, 2, self.backspace), ("=", 4, 3, self.calculate),
        ]

        for text, row, col, command in buttons:
            is_operator = text in ("÷", "×", "−", "+")
            is_equals = text == "="
            style_name = "Eq.TButton" if is_equals else ("Op.TButton" if is_operator else "Digit.TButton")

            colspan = 1
            btn = ttk.Button(
                grid_frame, text=text, command=command, style=style_name,
                width=6 if colspan == 1 else 13
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=6, pady=6, sticky="nsew", ipady=10)

    def add_digit(self, digit):
        if self.expression == "Erro":
            self.expression = ""
            self.history_var.set("")
        self.expression += digit
        self.update_display()

    def add_decimal(self):
        parts = self.expression.replace("*", " ").replace("/", " ").replace("+", " ").replace("-", " ").split()
        current = parts[-1] if parts else ""
        if "." not in current:
            self.expression += "."
            self.update_display()

    def add_operator(self, operator):
        if self.expression and self.expression[-1] not in "+-*/":
            self.expression += operator
            self.update_display()

    def negate(self):
        if self.expression:
            self.expression = str(-self.evaluate(self.expression))
            self.update_display()

    def percent(self):
        if self.expression:
            self.expression = str(self.evaluate(self.expression) / 100)
            self.update_display()

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def clear(self):
        self.expression = ""
        self.history_var.set("")
        self.update_display()

    def calculate(self):
        if not self.expression:
            return
        result = self.evaluate(self.expression)
        self.history_var.set(self.expression + " =")
        self.expression = str(result)
        self.update_display()

    def evaluate(self, expression):
        try:
            return round(eval(expression), 10)
        except (ZeroDivisionError, SyntaxError):
            return "Erro"

    def update_display(self):
        display_text = self.expression.replace("*", "×").replace("/", "÷") if self.expression else "0"
        self.display_var.set(display_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()