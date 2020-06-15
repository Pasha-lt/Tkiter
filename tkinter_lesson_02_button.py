from tkinter import *
window = Tk()
window.title('Buttom Example')

btn_end = Button(window, text='Close', command=exit)


def tog():
    """Функция которая переключает цвет фона окна после нажатие еще одной кнопки."""
    if window.cget('bg') == 'yellow':  # Если установлен цвет фона желтый переключаем его на серый.
        window.configure(bg = 'gray')
    else:
        window.configure(bg = 'yellow')

btn_tog = Button(window, text='change color', command=tog)

btn_end.pack(padx=150, pady=20)
btn_tog.pack(padx=150, pady=20)

window.mainloop()