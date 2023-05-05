import tkinter
import mysql.connector as c
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk



#connection to the database
mydb = c.connect(
    host="localhost",
    user="root",
    password="",
    database="stock")
my_cursor= mydb.cursor()
class users:
    def __init__(self,login_window) :
        #GUI
        login_window.geometry("990x660+50+50")
        login_window.resizable(0,0)
        login_window.title('Login Page')
        login_window.iconbitmap('images/login.ico')

        self.bgImage=ImageTk.PhotoImage(file="images/bg.jpg")

        self.bglabel=Label(login_window,image=self.bgImage)
        self.bglabel.place(x=0,y=0)
        #variables
        self.id=IntVar()
        self.username=StringVar()
        self.password=StringVar()

        heading=Label(login_window,text='USER LOGIN',font=("Microsoft Yahei UI Light",23,'bold'),bg='white',fg='firebrick1')
        heading.place(x=605,y=120)

        self.username=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1') #bd=0 removing the borders
        self.username.insert(0,'username')
        self.username.place(x=580,y=200)
        self.username.bind('<FocusIn>',self.user_entre)  #onclick

        self.password=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1',show='*')
        self.password.insert(0,'password')
        self.password.place(x=580,y=260)
        self.password.bind('<FocusIn>',self.password_entre) 

        frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
        frame1.place(x=580,y=222)
        frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
        frame2.place(x=580,y=282)

        self.closeye=PhotoImage(file='images/closeye.png')
        self.eyebutton=Button(login_window,image=self.closeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=self.show)
        self.eyebutton.place(x=800,y=255)

        loginButton=Button(login_window,text='login',font=('open sans',16,'bold'),fg='white',bg='firebrick1',cursor='hand2',activebackground='firebrick1',activeforeground='white',bd=0,width=19,command=self.login)
        loginButton.place(x=578,y=350)

        orlabel=Label(login_window,text='-------------- OR --------------',font=('open sans',16),fg='firebrick1',bg='white')
        orlabel.place(x=583,y=400)

        signupButton=Button(login_window,text='sign up',font=('open sans',16,'bold'),fg='white',bg='firebrick1',cursor='hand2',activebackground='firebrick1',activeforeground='white',bd=0,width=19,command=self.signup_page)
        signupButton.place(x=578,y=450)
        
    def login(self):
        user = self.username.get()
        passw = self.password.get()
        if user == '' or passw == '':
            messagebox.showerror(title='Error', message='all the fields are required')
        query = "SELECT * FROM users WHERE USERNAME=%s AND PASSWORD=%s"
        my_cursor.execute(query, (user, passw))
        row = my_cursor.fetchone()
        if row != None:
            login_window.destroy()
            import home_page
        else:
            messagebox.showerror(title='Error', message='Invalid Login')

    def user_entre(self,event):
        if self.username.get()=='username':
          self.username.delete(0,END)
    def password_entre(self,event):
       if self.password.get()=='password':
        self.password.delete(0,END)
    def show(self):
        self.closeye.config(file='images/openeye.png')
        self.password.config(show='')
        self.eyebutton.config(command=self.hide)
    def hide(self):
     self.closeye.config(file='images/closeye.png')
     self.password.config(show='*')
     self.eyebutton.config(command=self.show)
    def signup_page(self):
        login_window.destroy()
        import signup_page



        

login_window=Tk()
ob=users(login_window)
login_window.mainloop()
