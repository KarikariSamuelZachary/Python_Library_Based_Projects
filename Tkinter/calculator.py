import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_results.delete(1.0, "end")
    text_results.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result=str(eval(calculation))
        text_results.delete(1.0,"end")
        text_results.insert(1.0, result)

    except:
        clear_field()
        text_results.insert(1.0,"error")

def clear_field():
    global calculation
    calculation=""
    text_results.delete(1.0, "end")


window =tk.Tk()
window.geometry("400x300")

text_results= tk.Text(window, height=2, width=16, font=("Arial", 24))
text_results.grid(columnspan=5)

button_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1), width="5", font=("Arial",14))
button_1.grid(row=2, column=1)
button_2 = tk.Button(window, text="2", command=lambda: add_to_calculation(2), width="5", font=("Arial",14))
button_2.grid(row=2, column=2)
button_3 = tk.Button(window, text="3", command=lambda: add_to_calculation(3), width="5", font=("Arial",14))
button_3.grid(row=2, column=3)
button_4 = tk.Button(window, text="4", command=lambda: add_to_calculation(4), width="5", font=("Arial",14))
button_4.grid(row=3, column=1)
button_5 = tk.Button(window, text="5", command=lambda: add_to_calculation(5), width="5", font=("Arial",14))
button_5.grid(row=3, column=2)
button_6 = tk.Button(window, text="6", command=lambda: add_to_calculation(6), width="5", font=("Arial",14))
button_6.grid(row=3, column=3)
button_7 = tk.Button(window, text="7", command=lambda: add_to_calculation(7), width="5", font=("Arial",14))
button_7.grid(row=4, column=1)
button_8 = tk.Button(window, text="8", command=lambda: add_to_calculation(8), width="5", font=("Arial",14))
button_8.grid(row=4, column=2)
button_9 = tk.Button(window, text="9", command=lambda: add_to_calculation(9), width="5", font=("Arial",14))
button_9.grid(row=4, column=3)
button_0 = tk.Button(window, text="0", command=lambda: add_to_calculation(0), width="5", font=("Arial",14))
button_0.grid(row=5, column=2)
button_plus = tk.Button(window, text="+", command=lambda: add_to_calculation("+"), width="5", font=("Arial",14))
button_plus.grid(row=2, column=4)
button_minus = tk.Button(window, text="-", command=lambda: add_to_calculation("-"), width="5", font=("Arial",14))
button_minus.grid(row=3, column=4)
button_mul = tk.Button(window, text="*", command=lambda: add_to_calculation("*"), width="5", font=("Arial",14))
button_mul.grid(row=4, column=4)
button_div = tk.Button(window, text="/", command=lambda: add_to_calculation("/"), width="5", font=("Arial",14))
button_div.grid(row=5, column=4)
button_open = tk.Button(window, text="(", command=lambda: add_to_calculation("("), width="5", font=("Arial",14))
button_open.grid(row=5, column=1)
button_close = tk.Button(window, text=")", command=lambda: add_to_calculation(")"), width="5", font=("Arial",14))
button_close.grid(row=5, column=3)
button_equals = tk.Button(window, text="=", command=evaluate_calculation, width="11", font=("Arial",14))
button_equals.grid(row=6, column=3,columnspan=2,)
button_clear = tk.Button(window, text="clear", command= clear_field, width="11", font=("Arial",14))
button_clear.grid(row=6, column=1,columnspan=2,)

window.mainloop()
