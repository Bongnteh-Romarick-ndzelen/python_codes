from tkinter import *
window = Tk() #instantiae the instance of the window
window.geometry("420x420")
window.title("Romarick first GUI program")
icon = PhotoImage(file="Romaricklogo.png")
window.iconphoto(True, icon)
window.config(background="#5cfcff")
label = Label(window, text="Hello Romarick",
              font=("Arial",40, "bold"),
              fg="#00ff00",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20)

label.pack()

window.mainloop() #place window on the computer screen, listen for event