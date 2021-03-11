from tkinter import *

window = Tk()
#window.resizable(False,False)
#window.wm_iconphoto('logo.png')
photo = PhotoImage(file="logo.png")
window.iconphoto(False,photo)
window.geometry("700x500")
window.wm_title("Movies & Series")
window.configure(background='black')


C = Canvas(window)

bt = Button(master = window,text="Movies&TV",height=3,bg="blue")
bt.place(x=300, y=250, relwidth=0.2 ,relheight=0.2)

#original = PhotoImage(file = "test.png")
#resized = original.resize((700, 500),Image.ANTIALIAS)
#image = ImageTk.PhotoImage(resized)
#background_label = Label(window, image=resized,justify= 'center')
#background_label.place(x=0, y=0, relwidth=1 ,relheight=1)
#background_label.pack(fill=BOTH, expand=YES)




#filename = PhotoImage(file = "test.png")
#background_label = Label(window, image=resized,justify= 'center')
#background_label.place(x=0, y=0, relwidth=1 ,relheight=1)
#background_label.pack(fill=BOTH, expand=YES)




C.pack(fill=BOTH,expand = YES)


#window.columnconfigure(1, weight=1, minsize=75)
#window.rowconfigure(1, weight=1, minsize=50)


window.mainloop()