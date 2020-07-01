"""
A program that stores this book information
Title, Author,
Year, ISBN

User can do below actions:

View all records
Search an entry
Add and entry
update an  entry
Delete an entry
Close
"""
from tkinter import *
from backend import Database


database=Database()

def view_command():
    lstBox.delete(0,END)
    rows= database.view()
    for row in rows:
        lstBox.insert(END, row)


def search_command():
    lstBox.delete(0,END)
    rows=database.search(title=title_var.get(), author=author_var.get(), year=year_var.get(), isbn=isbn_var.get())
    for row in rows:
        lstBox.insert(END, row)


def addEntry_command():
    lstBox.delete(0,END)
    database.insert(title=title_var.get(), author=author_var.get(), year=year_var.get(), isbn=isbn_var.get())
    lstBox.insert(END, (title_var.get(), author_var.get(), year_var.get(), isbn_var.get()))

def getSelectedRow(event):
    try:

        index=lstBox.curselection()
        print("index ",index)
        global selected_tuple
        selected_tuple =lstBox.get(index)
        print(selected_tuple)
        ent1.delete(0,END)
        ent1.insert(END,selected_tuple[1])

        ent2.delete(0,END)
        ent2.insert(END,selected_tuple[3])

        ent3.delete(0,END)
        ent3.insert(END,selected_tuple[2])

        ent4.delete(0,END)
        ent4.insert(END,selected_tuple[4])

    except  TclError:
        pass

    
    

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    print(selected_tuple)
    print(title_var.get(),author_var.get(),year_var.get(),isbn_var.get(),selected_tuple[0])
    database.update(title_var.get(),author_var.get(),year_var.get(),isbn_var.get(),selected_tuple[0])


    





window =Tk()
window.wm_title("BookStore")

title_var=StringVar()
lb1 =Label(window,text=" Title")
lb1.grid(row = '0', column='0')

ent1= Entry(window,textvariable=title_var)
ent1.grid(row='0',column='1')

year_var=StringVar()
lb2 =Label(window,text=" Year")
lb2.grid(row = '1', column='0')

ent2= Entry(window,textvariable=year_var)
ent2.grid(row='1',column='1')

author_var=StringVar()
lb3 =Label(window,text=" Author")
lb3.grid(row = '0', column='2')
ent3= Entry(window,textvariable=author_var)
ent3.grid(row='0',column='3')

isbn_var=StringVar()
lb4 =Label(window,text=" ISBN")
lb4.grid(row = '1', column='2')
ent4= Entry(window,textvariable=isbn_var)
ent4.grid(row='1',column='3')

lstBox=Listbox(window,height=10,width=35)
lstBox.grid(row='2', column='0', rowspan='6', columnspan='2')
lstBox.bind('<<ListboxSelect>>',getSelectedRow)

sb1=Scrollbar(window)
sb1.grid(row='2', column='2', rowspan='6')




b1= Button(window,text="View Entry",command=view_command ,width=12)
b1.grid(row='2', column='3')

b2= Button(window,text="Search Entry", command= search_command,width=12)
b2.grid(row='3', column='3')

b3= Button(window,text="Add Entry", command=addEntry_command,width=12)
b3.grid(row='4', column='3')

b4= Button(window,text="Update",command= update_command, width=12)
b4.grid(row='5', column='3')

b5= Button(window,text="Delete",command=delete_command ,width=12)
b5.grid(row='6', column='3')

b6= Button(window,text="Close",command=window.destroy, width=12)
b6.grid(row='7', column='3')


window.mainloop()