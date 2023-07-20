import tkinter as tk
class Example(tk.Tk):
      def  __init__(self):
            super().__init__()
            self.canvas = tk.Canvas(self,width=800,height=600)
            self.canvas.create_text(400,200,text='Starlight',font='Arial 20 bold')
            self.canvas.create_text(400,325,text='Press a button to start a game',font='Arial 20')
            self.canvas.pack()
            self.a = 400
            self.b = 500
            self.canvas.bind('<Button-1>',self.start)
            self.canvas.bind('<Button-3>',self.start)
            self.canvas.bind_all('<Left>',self.move_any)
            self.canvas.bind_all('<Right>',self.move_any)
            self.canvas.bind_all('<Up>',self.move_any)
            self.canvas.bind_all('<Down>',self.move_any)
            
      def start(self,Coordinates):
            self.canvas.delete('all')
            self.canvas.create_rectangle(self.a-20,self.b,self.a+20,self.b-50)
            
      def move_any(self,event):
            self.canvas.delete('all')
            x = event.keysym
            if x == 'Left':
                  self.a -= 100
            if x == 'Right':
                  self.a += 100
            if x == 'Up':
                  self.b -= 100
            if x == 'Down':
                  self.b += 100
            self.canvas.create_rectangle(self.a-20,self.b,self.a+20,self.b-50)
                
            
if __name__ == '__main__':
      Example().mainloop()
          