"""
A program that stores Movies and Series that you watched
By : Shahryar Tayeb

"""
from tkinter import *
import backend

selected_tuple = None


def get_selected_row(event):
    #index = list1.curselection()[0]
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),director_text.get(),year_text.get(),imdb_text.get()):
        list1.insert(END,row)
def add_command():
    
    if title_text.get() =="" or director_text.get() =="" or year_text.get() =="" or imdb_text.get() == "":
        lbl_msg["text"] = "Please, Fill The Form Completely !!!"
        
    else:
        backend.insert(title_text.get(),director_text.get(),year_text.get(),imdb_text.get())
        lbl_msg["text"] = "                                                                          "
        view_command()
    

def delete_command():
    try:
        backend.delete(selected_tuple[0])
        view_command()
    except:
        pass

def update_command():
    try:
        backend.update(selected_tuple[0],title_text.get(),director_text.get(),year_text.get(),imdb_text.get())
        view_command()
    except:
        pass

def clear_command():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    lbl_msg["text"]="A Python Program By : Shahryar Tayeb"
    #lbl_msg["text"] = "                                                                     "
    
def show_info():
    lbl_msg["text"] = "For More Information Visit @Shahryar_tayeb "



window = Tk()
#window.resizable(False,False)
#window.wm_iconphoto('logo.png')
photo = PhotoImage(file="logo.png")
window.iconphoto(False,photo)
window.geometry("600x400")

window.wm_title("Movies & Series")
window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=50)



#window.title("Book list")

#Drop down menu 
#cb = Canvas(master="window", cnf={}, **kw)
#cb.grid(row=6,column=0)


# ......................................Start of movie Frame..................................


movie_frame = Frame()

frame_entries = Frame(master = movie_frame )
frame_buttons = Frame(master = movie_frame )
frame_listbox = Frame(master = movie_frame )



#Lables
l1 = Label(master = frame_entries,text="Title", background = "#34A2FE",width=5,padx=5,pady=5)
l1.grid(row=0,column=0,sticky="nsew")

l2 = Label(master = frame_entries,text="Director", background = "#34A2FE",width=5,padx=5,pady=5)
l2.grid(row=0,column=2,sticky="nsew")

l3 = Label(master = frame_entries,text="Year", background = "#34A2FE",width=5,padx=5,pady=5)
l3.grid(row=1,column=0,sticky="nsew")

l4 = Label(master = frame_entries,text="Rating", background = "#34A2FE",width=5,padx=5,pady=5)
l4.grid(row=1,column=2,sticky="nsew")

lbl_msg = Label(master = movie_frame,text="A Python Program By : Shahryar Tayeb" , borderwidth = 5)
lbl_msg.grid(row=2,column=1)

# for entries
title_text = StringVar()
e1= Entry(master = frame_entries,textvariable=title_text,width=30,selectbackground='blue')
e1.grid(row=0,column=1,padx = 5,sticky="nsew")

director_text = StringVar()
e2= Entry(master = frame_entries,textvariable=director_text,width=30)
e2.grid(row=0,column=3,padx = 5,sticky="nsew")

year_text = StringVar()
e3= Entry(master = frame_entries,textvariable=year_text,width=30)
e3.grid(row=1,column=1,padx = 5,sticky="nsew")

imdb_text = StringVar()
e4= Entry(master = frame_entries,textvariable=imdb_text,width=30)
e4.grid(row=1,column=3,padx = 5,sticky="nsew")



frame_entries.grid(row=0,column=1 ,padx=5,pady=5,sticky="nsew")

#list box
list1 = Listbox(master = frame_listbox,height=12,width=65,bd=2.5,highlightcolor="#cceeff",relief=FLAT)
list1.grid(row=2,column=1,rowspan=5,sticky="nsew",padx=30,pady=35)

sb1 = Scrollbar(master = frame_listbox)
sb1.grid(row=2,column=2,rowspan=6,sticky="nsew")

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

frame_listbox.grid( row=1,column=1,sticky="nsew")

#buttons

b1=Button(master = frame_buttons,text="View all",width=12,command=view_command, background = "#34A2FE", relief = FLAT)
b1.grid(row=2,column=3,sticky="nsew") 

b2=Button(master = frame_buttons,text="Search Entry",width=12,command=search_command, background = "#34A2FE", relief = FLAT)
b2.grid(row=3,column=3,sticky="nsew")

b3=Button(master = frame_buttons,text="Add Entry",width=12,command=add_command, background = "#34A2FE", relief = FLAT)
b3.grid(row=4,column=3,sticky="nsew")

b4=Button(master = frame_buttons,text="Update Selected",width=12,command=update_command, background = "green", relief = FLAT)
b4.grid(row=5,column=3,sticky="nsew")

b5=Button(master = frame_buttons,text="Delete Selected",width=12,command=delete_command, background = "green", relief = FLAT)
b5.grid(row=6,column=3,sticky="nsew")

b6=Button(master = frame_buttons,text="Close",width=12,command=window.destroy, background = "red", relief = FLAT)
b6.grid(row=7,column=3,sticky="nsew")

be = Button(master = frame_buttons,text="Clear All", width = 12 ,command=clear_command, background = "red", relief = FLAT) 
be.grid(row=0,column=3,sticky="nsew")

bt = Button(master = movie_frame,text="Movies&TV",height=3,bg="yellow",command = show_info)
bt.grid(row=0,column=2,sticky="nsew",pady=5,padx=3)

frame_buttons.grid(row=1,column=2,pady=20,padx=3,sticky="nsew")




movie_frame.grid(row = 0,column=0)

#..............................................End of movie Frame..........................................


#home_frame = Frame(master=window)







#home_frame.grid(row=0,column=0)



window.mainloop()       

