import tkinter as tk
from .main import calculator


class InputFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.input_text = tk.StringVar()

        self.input_field = tk.Entry(
            self.parent, font=('arial', 18, 'bold'), textvariable=self.input_text,
            width=50, bg="#eee", bd=0, justify=tk.LEFT)
        self.input_field.focus()
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field

    def btn_click(self, item):
        curser_position = self.input_field.index(tk.INSERT)
        expression = self.input_field.get()
        expression = expression[:curser_position] + str(item) + expression[curser_position:]
        self.input_text.set(expression)
        self.input_field.icursor(curser_position+1)

    def btn_function_click(self, item):
        s = str(item) + '()'
        expression = self.input_field.get()
        curser_position = self.input_field.index(tk.INSERT)
        expression = expression[:curser_position] + s + expression[curser_position:]
        self.input_text.set(expression)
        self.input_field.icursor(curser_position+len(s)-1)

    def bt_clear(self):
        self.input_text.set("")

    def curser_previous(self):
        curser_position = self.input_field.index(tk.INSERT)
        self.input_field.icursor(curser_position-1)

    def curser_next(self):
        curser_position = self.input_field.index(tk.INSERT)
        self.input_field.icursor(curser_position+1)

    def bt_equal(self,):
        expression = self.input_field.get()

        result = calculator(expression)
        expression = ''
        if result[0] != 0:
            expression += str(result[0])
        if result[0] != 0 and result[1] != 0 and result[1] > 0:
            expression += '+'
        if result[1] != 0:
            expression += str(result[1])
        if result[0] == 0 and result[1] == 0:
            expression += '0'

        self.input_text.set(expression)


class ButtonFrame(tk.Frame):
    def __init__(self, parent, input_frame, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.input_frame = input_frame
        self.parent = parent

        self.clear = tk.Button(
            self, text="C", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
            command=lambda: self.input_frame.bt_clear()
        ).grid(row=0, column=0, padx=1, pady=1)
        self.previous = tk.Button(
            self, text="<-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
            command=lambda: self.input_frame.curser_previous()
        ).grid(row=0, column=1, padx=1, pady=1)
        self.before = tk.Button(
            self, text="->", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
            command=lambda: self.input_frame.curser_next()
        ).grid(row=0, column=2, padx=1, pady=1)

        self.divide = tk.Button(
            self, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_click("/")
        ).grid(row=0, column=3, padx=1, pady=1)
        self.open = tk.Button(
            self, text="(", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_click("(")
        ).grid(row=0, column=4, padx=1, pady=1)
        self.close = tk.Button(
            self, text=")", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_click(")")
        ).grid(row=0, column=5, padx=1, pady=1)

        # second row

        self.seven = tk.Button(
            self, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
            cursor="hand2", command=lambda: self.input_frame.btn_click(7)
        ).grid(row=1, column=0, padx=1, pady=1)
        self.eight = tk.Button(
            self, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
            cursor="hand2", command=lambda: self.input_frame.btn_click(8)
        ).grid(row=1, column=1, padx=1, pady=1)
        self.nine = tk.Button(
            self, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
            cursor="hand2", command=lambda: self.input_frame.btn_click(9)
        ).grid(row=1, column=2, padx=1, pady=1)
        self.multiply = tk.Button(
            self, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_click("*")
        ).grid(row=1, column=3, padx=1, pady=1)
        self.sin = tk.Button(
            self, text="sin", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("sin")
        ).grid(row=1, column=4, padx=1, pady=1)
        self.cos = tk.Button(
            self, text="cos", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("cos")
        ).grid(row=1, column=5, padx=1, pady=1)

        # third row

        self.four = tk.Button(
            self, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
            cursor="hand2", command=lambda: self.input_frame.btn_click(4)
        ).grid(row=2, column=0, padx=1, pady=1)
        self.five = tk.Button(
            self, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
            cursor="hand2", command=lambda: self.input_frame.btn_click(5)
        ).grid(row=2, column=1, padx=1, pady=1)
        self.six = tk.Button(
            self, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
            cursor="hand2", command=lambda: self.input_frame.btn_click(6)
        ).grid(row=2, column=2, padx=1, pady=1)
        self.minus = tk.Button(
            self, text="-", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_click("-")
        ).grid(row=2, column=3, padx=1, pady=1)
        self.tan = tk.Button(
            self, text="tan", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("tan")
        ).grid(row=2, column=4, padx=1, pady=1)
        self.cot = tk.Button(
            self, text="cot", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("cot")
        ).grid(row=2, column=5, padx=1, pady=1)

        # fourth row

        self.one = tk.Button(
            self, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
            cursor="hand2", command=lambda: self.input_frame.btn_click(1)
        ).grid(row=3, column=0, padx=1, pady=1)
        self.two = tk.Button(
            self, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
            cursor="hand2", command=lambda: self.input_frame.btn_click(2)
        ).grid(row=3, column=1, padx=1, pady=1)
        self.three = tk.Button(
            self, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
            cursor="hand2", command=lambda: self.input_frame.btn_click(3)
        ).grid(row=3, column=2, padx=1, pady=1)
        self.plus = tk.Button(
            self, text="+", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_click("+")
        ).grid(row=3, column=3, padx=1, pady=1)
        self.log = tk.Button(
            self, text="log", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("log")
        ).grid(row=3, column=4, padx=1, pady=1)
        self.ln = tk.Button(
            self, text="ln", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_function_click("ln")
        ).grid(row=3, column=5, padx=1, pady=1)

        # fourth row

        self.zero = tk.Button(
            self, text="0", fg="black", width=24, height=3, bd=0, bg="#fff", cursor="hand2",
            command=lambda: self.input_frame.btn_click(0)
        ).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        self.point = tk.Button(
            self, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_click(".")
        ).grid(row=4, column=2, padx=1, pady=1)
        self.equals = tk.Button(
            self, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.bt_equal()
        ).grid(row=4, column=3, padx=1, pady=1)
        self.pi = tk.Button(
            self, text="\u03C0", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_click("\u03C0")
        ).grid(row=4, column=4, padx=1, pady=1)
        self.i = tk.Button(
            self, text="i", fg="black", width=10, height=3, bd=0, bg="#eee",
            cursor="hand2", command=lambda: self.input_frame.btn_click("i")
        ).grid(row=4, column=5, padx=1, pady=1)


def run_gui():
    root = tk.Tk()

    root.geometry("650x375")
    root.resizable(0, 0)  # this is to prevent from resizing the window
    root.title("Calculator")

    input_frame = InputFrame(
        root, bd=0,
        highlightbackground="black", highlightcolor="black",
        highlightthickness=2
    )
    input_frame.pack(side=tk.TOP)

    btn_frame = ButtonFrame(root, input_frame=input_frame, bg="grey")
    btn_frame.pack()

    root.mainloop()
