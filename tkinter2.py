from tkinter import *

def click():
      print('You click the button')
window = Tk()

Button = Button(window,
                text="click me!",
                command=click,
                font=('comic sans', 30),
                bg="black",
                fg='#00ff00',
                activeforeground='#00ff00',
                activebackground='black')
Button.pack()

window.mainloop()