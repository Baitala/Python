import tkinter as tk

def hypothenuse(cathetus1, cathetus2):
    return (cathetus1**2 + cathetus2**2)**0.5

def handler1(event):
    answer.set(hypothenuse(float(x_entry.get()), float(y_entry.get())))

main_window = tk.Tk()
main_window.title("Теорема Пифагора")
main_window.geometry("600x150")

x_label = tk.Label(main_window, text="Катет x:", font="Sans 10")
x_entry = tk.Entry(main_window, width=10, font="Sans 20")
x_label.grid(column=0, row=1)
x_entry.grid(column=1, row=1)

y_label = tk.Label(main_window, text="Катет y:", font="Sans 10")
y_entry = tk.Entry(main_window, width=10, font="Sans 20")
y_label.grid(column=0, row=2)
y_entry.grid(column=1, row=2)

answer_text_label = tk.Label(main_window, text="Гипотенуза:", font="Sans 10")
answer = tk.StringVar()
answer_label = tk.Label(main_window, width=30, textvariable = answer, font="Sans 20")
answer_text_label.grid(column=0, row=3)
answer_label.grid(column=1, row=3)


pyth_button = tk.Button(main_window, text="Спифагорить", font="Sans 20")
pyth_button.grid(column=1, row=4)

pyth_button.bind('<Button-1>', handler1)

main_window.mainloop()

