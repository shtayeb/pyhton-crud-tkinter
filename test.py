from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to code')
root.iconbitmap('logo.png')

my_image = ImageTk.PhotoImage(Image.open('logo.png'))
my_labe = Label(image=my_image)
my_labe.pack()






button_quit = Button(root,text="Exit",command = root.quit)
button_quit.pack()


root.mainloop()