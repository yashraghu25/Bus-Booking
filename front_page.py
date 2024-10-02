from tkinter import *
root=Tk()
root.title("online bus booking system")
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
Img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=Img).pack()
Label(root,text="Online Bus Booking System",fg='red',font=("Arial bold",25),bg='light blue').pack(pady=(0,30))
Label(root,text="Name : Saurabh Shukla",fg="blue",font=("arial bold",12)).pack(pady=(0,15))
Label(root,text="Er : 211B283",fg="blue",font=("arial bold",12)).pack(pady=(0,15))
Label(root,text="Mobile No.: 8957440271",fg="blue",font=("arial bold",12)).pack()
Label(root,text="Submitted To : Dr.Mahesh Kumar",fg='red',font=("Arial bold",17),bg='light blue').pack(pady=(50,0))
Label(root,text="Project Based Learning ",fg='red',font=("Arial bold",12)).pack()

def cover_to_home(event):
    root.destroy()
    root.home_page()
root.bind("<KeyPress>", cover_to_home)
      
