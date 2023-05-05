import tkinter
import mysql.connector as c
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk

signup_window=Tk()

mydb = c.connect(
    host="localhost",
    user="root",
    password="",
    database="stock")
my_cursor= mydb.cursor()

def clear():
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    repassword_entry.delete(0,END)

def signup():
    user=username_entry.get()
    passw=password_entry.get()
    repassw=repassword_entry.get()
    if user=='' or passw=='' or repassw=='' :
        messagebox.showerror(title='Error',message='all the fields are required')
    elif passw!=repassw :
        messagebox.showerror(title='Error',message='password mismatch')
    else :
        query="SELECT * FROM users where USERNAME=%s"
        my_cursor.execute(query,(user,))
#execute method expects the second argument to be a tuple if there is one parameter you need to add comma after it to create a tuple with one element. 
        row=my_cursor.fetchone()
        if row != None :
            messagebox.showerror(title='Error',message='Username Already exists')
        else :
            query="INSERT INTO users(USERNAME,PASSWORD) VALUES(%s,%s) "
            my_cursor.execute(query,(user,passw))
            mydb.commit() #do the operation
            mydb.close()
            messagebox.showinfo(title='Success',message='registration is successful')
            clear()
            
def login_page():
    signup_window.destroy()
    import login_page


signup_window.title('Sign up Page')
signup_window.geometry("990x660+50+50")
signup_window.iconbitmap('images/login.ico')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='images/bg.jpg')

bglabel=Label(signup_window,image=background)
bglabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)
heading=Label(frame,text='CREATE AN ACCOUNT',font=("Microsoft Yahei UI Light",18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

username_label=Label(frame,text='username',font=('Microsoft Yahei UI Light',10,'bold'),fg='firebrick1',bg='white')
username_label.grid(row=1,column=0,sticky='w',padx=25) # sticky='w' means stick in the west
username_entry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
username_entry.grid(row=2,column=0,sticky='w',padx=25,pady=10)

password_label=Label(frame,text='password',font=('Microsoft Yahei UI Light',10,'bold'),fg='firebrick1',bg='white')
password_label.grid(row=3,column=0,sticky='w',padx=25)
password_entry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
password_entry.grid(row=4,column=0,sticky='w',padx=25,pady=10)

repassword_label=Label(frame,text='confirm password',font=('Microsoft Yahei UI Light',10,'bold'),fg='firebrick1',bg='white')
repassword_label.grid(row=5,column=0,sticky='w',padx=25)
repassword_entry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
repassword_entry.grid(row=6,column=0,sticky='w',padx=25,pady=10)

signupButton=Button(frame,text='Sign up',font=('open sans',16,'bold'),fg='white',bg='firebrick1',cursor='hand2',activebackground='firebrick1',activeforeground='white',bd=0,width=17,command=signup)
signupButton.grid(row=8,column=0,pady=30)

already_account=Label(frame,text='you have already an account ?',font=('open sans',9,'bold underline'),fg='blue',bg='white')
already_account.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Login',font=('open sans',9,'bold underline'),fg='blue',bg='white',cursor='hand2',activebackground='white',activeforeground='blue',bd=0,command=login_page)
loginButton.place(x=215,y=370)

signup_window.mainloop()