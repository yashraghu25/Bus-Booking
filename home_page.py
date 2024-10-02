from tkinter import *
root=Tk()
root.title("online bus booking system")
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
Img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=Img).grid(row=0,column=1,columnspan=12,padx=400)
Label(root,text="Online Bus Booking System",fg='red',font=("Arial bold",25),bg='light blue').grid(row=1,column=1,pady=(0,40),columnspan=12,padx=400)
Button(root,text='Seat Booking',bg='pale green',font=( "Arial bold",15)).grid(row=5,column=4,padx=(180,50))
Button(root,text='Checked Booked Seat',bg='lime green',font=("Arial bold",15)).grid(row=5,column=5,padx=30)
Button(root,text='Add Bus Details',bg='forest green',font=("Arial bold",15)).grid(row=5,column=6,pady=20)
Label(root,text="For Admin Only",fg='red',font=("Arial bold",12)).grid(row=6,column=6)

def cover_to_home(event):
    root.destroy()
    self.home_page()

    root.bind("<KeyPress>", cover_to_home)
