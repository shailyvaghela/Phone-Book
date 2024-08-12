from tkinter import *
from tkinter import ttk
from views import * #to add method for logic
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
col0="white"
col1="black"
col2="green"
#for creating the window 
window = Tk()
window.title("MY PHONEBOOK")
window.geometry('500x500')
window.configure(background=col0)
window.resizable(width=FALSE,height=FALSE)#it will stop the maximize 

print("Login Here")
user=input("Enter your credientials to open phonebook")

if user=="a" or user=="ADMIN":


    #for frames
    title_frame=Frame(window,width=500,height=50,bg=col2)#bg for background color
    title_frame.grid(row=0,column=0,padx=0,pady=1)#grid to arrange the frame in particular sequences

    mid_content=Frame(window,width=500,height=170,bg=col0)
    mid_content.grid(row=1,column=0,padx=0,pady=1)

    frame_table=Frame(window,width=500,height=150,bg=col0,relief='solid')
    frame_table.grid(row=2,column=0,columnspan=2,padx=1,pady=50,sticky='nw')#pad x for padding from x and pad y from y axis and STICKY is for fixing the element

    #functions for all
    def show():
        global tree_v #global coz it is used multiple times 
        heading=['Name','Contact_No','Email']#heading with a list

        #DEMO DATA
        #demo_list=[['urv','1234','urv@gmail.com']]#stored as an object to maintain sequence
        demo_list=view()#retriving info from views.py

        #tree_v is a table treeview is a widget
        tree_v=ttk.Treeview(frame_table,selectmode="extended",columns=heading,show="headings")#treeview is a widget used as a table widget and its is a hierarchical list 

        #creating both horizontal and vertical scroll bar
        v_bar=ttk.Scrollbar(frame_table,orient="vertical",command=tree_v.yview)#command is used to allow scrollbar widgets to communicate with the scrollable widgets
        h_bar=ttk.Scrollbar(frame_table,orient="horizontal",command=tree_v.xview)

        #to activate both scroll bar (scrollable widgets)
        tree_v.configure(yscrollcommand=v_bar.set,xscrollcommand=h_bar.set)#scrollable widgets have 2 option yscrollcommand/xscrollcomtree_v
        #aranging the elements 
        tree_v.grid(column=0,row=0,sticky='nwes')
        v_bar.grid(column=1,row=0,sticky='ns')#here sticky is used for extending the length of both bars
        h_bar.grid(column=0,row=1,sticky='ew')

        #creating an heading for a table 
        tree_v.heading(0,text='Name',anchor=NW)
        tree_v.heading(1,text='Contact_No',anchor=NW)
        tree_v.heading(2,text='Email',anchor=NW)

        #sizing the column width
        tree_v.column(0,width=150,anchor=NW)
        tree_v.column(1,width=150,anchor=NW)
        tree_v.column(2,width=180,anchor=NW)

        #to add an demo entry in a table
        for i in demo_list:
            tree_v.insert('','end',values=i) 
    show()


    #for addd
    def insert():
        name=io1.get()
        number=io2.get()
        email=io3.get()

        data=[name,number,email]

        if name == '' or number == '' or email =='':
            messagebox.showwarning('data','Please enter the data in all fields')
        else:
            add(data)
            messagebox.showinfo('data','data added successfully')

            io1.delete(0,'end')
            io2.delete(0,'end')
            io3.delete(0,'end')

            show()

    #for update
    def change():
        try:
            tree_data=tree_v.focus()
            tree_d=tree_v.item(tree_data)
            tree_list=tree_d['values']

            name=str(tree_list[0])
            number=str(tree_list[1])
            email=str(tree_list[2])

            io1.insert(0,name)
            io2.insert(0,number)
            io3.insert(0,email)

            def confirm():
                new_n=io1.get()
                new_no=io2.get()
                new_email=io3.get()

                data=[new_no,new_n,new_no,new_email]
                update(data)

                messagebox.showinfo('successful','data updated sucessfully')

                io1.delete(0,'end')
                io2.delete(0,'end')
                io3.delete(0,'end')

                for widget in frame_table.winfo_children():
                    widget.destroy()

                b_confirm.destroy()

                show()
            b_confirm=Button(mid_content,text="confirm",height=1,width=10,bg=col2,font=('Ivy 8 bold'),fg=col0,relief='solid',command=confirm)
            b_confirm.place(x=290,y=110)
        except IndexError:
            messagebox.showerror('error','select one of them from the table')

    #fro remove
    def delete():
        try:
            tree_data=tree_v.focus()
            tree_d=tree_v.item(tree_data)
            tree_list=tree_d['values']
            tree_number=str(tree_list[1])

            remove(tree_number)
            messagebox.showinfo('success','data has been deleted')

            for widget in frame_table.winfo_children():
                widget.destroy()
            show()

        except IndexError:
            messagebox.showerror('error','select one of them from the table')

    #to search
    def find():
        number=io4.get()
        data=search(number)

        def delete_command():
            tree_v.delete(*tree_v.get_children())

        delete_command()

        for i in data:
            tree_v.insert('','end',values=i)
        io4.delete(0,'end')


    #for web mess
    def scrap():
        try:
            f=open("data.txt",'a')
            URL="https://bangalore.idbf.in/hotels"
            HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
            webpage = requests.get(URL, headers=HEADERS)
            #print(webpage)- to check for conections
            soup = BeautifulSoup(webpage.content, "html.parser")
            #print(soup)- to print all the content of the website
            links = soup.find_all("a")
            #print(links[5])
            for i in range(5,30,2):
                link=links[i].get('href')
                #print(link)
                product_list="" + link
                new_webpage = requests.get(product_list, headers=HEADERS)
                #print(new_webpage)
                new_soup = BeautifulSoup(new_webpage.content, "html.parser")
                #print(new_soup)
                ans= new_soup.find("div",attrs={"class":"list-group"}).text
                f.write(ans)
            messagebox.showinfo('success','Web scrapping done')
        except:
            messagebox.showinfo('success','Erro in Web scrapping process')


    #title
    name=Label(title_frame,text="PhoneBook",height=1,fg=col1,bg=col2,font=('Ivy 20 bold'))#fg for text color
    name.place(x=5,y=5)

    #adding widgets to mid_content l(l1) for label, io(io1) for input 
    #for name
    l1_name=Label(mid_content,text="Name:",width=20,height=1,font='10',bg=col0,anchor=NW)#anchor to move the elements left right top center using directions
    l1_name.place(x=10,y=20)
    io1=Entry(mid_content,width=20,justify='left',relief='solid')#relif for border visibility 
    io1.place(x=130,y=25)

    #for no
    l2_no=Label(mid_content,text="Contact_No:",width=20,height=1,font='2',bg=col0,anchor=NW)#anchor to move the elements left right top center using directions
    l2_no.place(x=10,y=50)
    io2=Entry(mid_content,width=20,justify='left',relief='solid')#relif for border visibility 
    io2.place(x=130,y=55)

    #for email
    l2_email=Label(mid_content,text="Email:",width=20,height=1,font='10',bg=col0,anchor=NW)#anchor to move the elements left right top center using directions
    l2_email.place(x=10,y=80)
    io3=Entry(mid_content,width=20,justify='left',relief='solid')#relif for border visibility 
    io3.place(x=130,y=85)

    #for search
    btn_search=Button(mid_content,text="Search",height=1,bg=col2,font=('Ivy 8 bold'),fg=col0,relief='solid',command=find)
    btn_search.place(x=290,y=20)
    io4=Entry(mid_content,width=22,justify='left',relief='solid')
    io4.place(x=344,y=23)

    #for view
    btn_view=Button(mid_content,text="View All",width=10,height=1,bg=col2,font=('Ivy 8 bold'),fg=col0,relief='solid',command=show)
    btn_view.place(x=290,y=50)

    #for add
    btn_add=Button(mid_content,text="Add",height=1,width=10,bg=col2,font=('Ivy 8 bold'),fg=col0,relief='solid',command=insert)
    btn_add.place(x=20,y=140)

    #for update
    btn_update=Button(mid_content,text="Update",height=1,width=10,bg=col2,font=('Ivy 8 bold'),fg=col0,relief='solid',command=change)
    btn_update.place(x=150,y=140)

    #for delete
    btn_delete=Button(mid_content,text="Delete",height=1,width=10,bg=col2,font=('Ivy 8 bold'),fg=col0,relief='solid',command=delete)
    btn_delete.place(x=280,y=140)

    #for web-scrapping
    btn_scrap=Button(mid_content,text="Web Scrap",height=1,width=10,bg=col2,font=('Ivy 8 bold'),fg=col0,relief='solid',command=scrap)
    btn_scrap.place(x=400,y=140)

    


    window.mainloop()   #to run