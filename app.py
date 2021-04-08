# !/usr/bin/env python


from parser import expr
from tkinter import (Tk, Button, 
                    Entry, W, E, END, font)

i = 0


def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1


def operation(operator):
    global i
    temp = len(operator)
    display.insert(i, operator)
    i += temp


def clear_display():
    display.delete(0, END)


def undo():
    state = display.get()
    if len(state):
        new_state = state[:-1]
        clear_display()
        display.insert(0, new_state)


def calculate():
    state = display.get()
    if state:
        try:
            expression = expr(state).compile()
            result = eval(expression)
            clear_display()
            display.insert(0, result)
        except Exception:
            clear_display()
            display.insert(0, "Math Error")


if __name__ == '__main__':
    root = Tk()
    root.title("Calculator")
    root.resizable(0, 0)

    calculator_font = font.Font(family='Helvetica', size=15)

    display = Entry(root)
    display.grid(row=1, columnspan=6, sticky=W+E)
    display['font'] = calculator_font

    Button(root, text="1", font=calculator_font,
        command=lambda: get_numbers(1)).grid(row=2, column=0, sticky=W+E)
    Button(root, text="2", font=calculator_font,
        command=lambda: get_numbers(2)).grid(row=2, column=1, sticky=W+E)
    Button(root, text="3", font=calculator_font,
        command=lambda: get_numbers(3)).grid(row=2, column=2, sticky=W+E)

    Button(root, text="4", font=calculator_font,
        command=lambda: get_numbers(4)).grid(row=3, column=0, sticky=W+E)
    Button(root, text="5", font=calculator_font,
        command=lambda: get_numbers(5)).grid(row=3, column=1, sticky=W+E)
    Button(root, text="6", font=calculator_font,
        command=lambda: get_numbers(6)).grid(row=3, column=2, sticky=W+E)

    Button(root, text="7", font=calculator_font,
        command=lambda: get_numbers(7)).grid(row=4, column=0, sticky=W+E)
    Button(root, text="8", font=calculator_font,
        command=lambda: get_numbers(8)).grid(row=4, column=1, sticky=W+E)
    Button(root, text="9", font=calculator_font,
        command=lambda: get_numbers(9)).grid(row=4, column=2, sticky=W+E)

    Button(root, text="AC", font=calculator_font,
        command=lambda: clear_display()).grid(row=5, column=0, sticky=W+E)
    Button(root, text="0", font=calculator_font,
        command=lambda: get_numbers(0)).grid(row=5, column=1, sticky=W+E)
    Button(root, text="%", font=calculator_font,
        command=lambda: operation("%")).grid(row=5, column=2, sticky=W+E)

    Button(root, text="+", font=calculator_font,
        command=lambda: operation("+")).grid(row=2, column=3, sticky=W+E)
    Button(root, text="-", font=calculator_font,
        command=lambda: operation("-")).grid(row=3, column=3, sticky=W+E)
    Button(root, text="*", font=calculator_font,
        command=lambda: operation("*")).grid(row=4, column=3, sticky=W+E)
    Button(root, text="/", font=calculator_font,
        command=lambda: operation("/")).grid(row=5, column=3, sticky=W+E)

    Button(root, text="←", font=calculator_font, 
           bg='#5197FD', command=lambda: undo()).grid(row=2, 
                                                      column=4, columnspan=2, sticky=W+E)
    Button(root, text="exp", font=calculator_font,
        command=lambda: operation("**")).grid(row=3, column=4, sticky=W+E)
    Button(root, text="^2", font=calculator_font, command=lambda: operation(
        "**2")).grid(row=3, column=5, sticky=W+E)
    Button(root, text="(", font=calculator_font,
        command=lambda: operation("(")).grid(row=4, column=4, sticky=W+E)
    Button(root, text=")", font=calculator_font,
        command=lambda: operation(")")).grid(row=4, column=5, sticky=W+E)
    Button(root, text="=", font=calculator_font, 
           bg='#FD5151', command=lambda: calculate()).grid(row=5, 
                                                           column=4, columnspan=2, sticky=W+E)

    root.mainloop()
