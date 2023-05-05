import tkinter
import mysql.connector as c
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk

class product :
	def __init__(self,home_page) :
		self.home_page=home_page
		self.home_page.geometry('1350x690+1+1')   
		self.home_page.title('Home Page')  
		self.home_page.configure(background='#B0E0E6')
		title=Label(self.home_page,text='Gestion stock',bg='white',fg='black',font=('monospace',14))
		title.pack(fill=X)
		
		manage_frame=Frame(self.home_page,bg='#B0E0E6')
		manage_frame.place(x=0,y=30,width=1300,height=200)

		#variables
		self.id_var=IntVar()
		self.name_var=StringVar()
		self.description_var=StringVar()
		self.price_var=IntVar()
		self.quantity_var=IntVar()
		self.date_in_var=StringVar()
		self.delete_product_var=StringVar()
		self.search_by_var=StringVar()
		self.search_var=StringVar()

		label_id=Label(manage_frame,text='ID :',bg='#B0E0E6')
		id_entry=Entry(manage_frame,bd=2,textvariable=self.id_var)
		label_id.grid(row=1,column=0)
		id_entry.grid(row=1,column=1,padx=8,pady=20)
		
		label_name=Label(manage_frame,text='Name :',bg='#B0E0E6')
		name_entry=Entry(manage_frame,bd=2,textvariable=self.name_var)
		label_name.grid(row=1,column=2)
		name_entry.grid(row=1,column=3,padx=8,pady=20)
		
		label_description=Label(manage_frame,text='Description :',bg='#B0E0E6')
		description_entry=Entry(manage_frame,bd=2,textvariable=self.description_var)
		label_description.grid(row=1,column=4)
		description_entry.grid(row=1,column=5,padx=8,pady=20)
		
		label_price=Label(manage_frame,text='Price :',bg='#B0E0E6')
		price_entry=Entry(manage_frame,bd=2,textvariable=self.price_var)
		label_price.grid(row=2,column=0)
		price_entry.grid(row=2,column=1,padx=8,pady=20)
		
		label_quantity=Label(manage_frame,text='Quantity :',bg='#B0E0E6')
		quantity_entry=Entry(manage_frame,bd=2,textvariable=self.quantity_var)
		label_quantity.grid(row=2,column=2)
		quantity_entry.grid(row=2,column=3,padx=8,pady=20)

		label_date_in=Label(manage_frame,text='Entry date :',bg='#B0E0E6')
		date_in_entry=Entry(manage_frame,bd=2,textvariable=self.date_in_var)
		label_date_in.grid(row=2,column=4)
		date_in_entry.grid(row=2,column=5,padx=8,pady=20)

		label_delete_product=Label(manage_frame,text='Delete product by name :',bg='#B0E0E6')
		delete_product_entry=Entry(manage_frame,bd=2,textvariable=self.delete_product_var)
		label_delete_product.grid(row=3,column=0)
		delete_product_entry.grid(row=3,column=1,padx=8,pady=20)
	
		add_btn=Button(manage_frame,text='ADD',width=20,fg='white',bg='#000080',cursor='hand2',command=self.add_product)
		delete_btn=Button(manage_frame,text='DELETE',width=20,fg='white',bg='#000080',cursor='hand2',command=self.delete_product)
		update_btn=Button(manage_frame,text='UPDATE',width=20,fg='white',bg='#000080',cursor='hand2',command=self.update_product)
		

		add_btn.grid(row=1,column=6,padx=10)
		delete_btn.grid(row=3,column=2,padx=10)
		update_btn.grid(row=2,column=6,padx=10)

		search_frame=Frame(self.home_page,bg='#B0E0E6')
		search_frame.place(x=700,y=170,width=500,height=45)

		label_search=Label(search_frame, text='Search product :',bg='#B0E0E6',fg='black')
		label_search.place(x=0,y=3)	

		search_entry=Entry(search_frame,justify='left',bd='2',textvariable=self.search_var)
		search_entry.place(x=100,y=3)
		
		combo_search=ttk.Combobox(search_frame, justify='left',textvariable=self.search_by_var)
		combo_search['value']=('Name','Price','Quantity','Date')
		combo_search.place(x=230,y=3)

		search_btn=Button(search_frame,text='Search',fg='white',bg='#000080',command=self.search)
		search_btn.place(x=380,y=2,width=120)


		details_frame=Frame(self.home_page)
		details_frame.place(x=0,y=200,width=1300,height=1000)

		self.product_table=ttk.Treeview(details_frame,columns=('ID','NAME','DESCRIPTION','PRICE','QUANTITY','DATE_IN'))
		self.product_table.place(x=0,y=0,width=1300,height=1000)
		self.product_table['show']='headings'
		self.product_table.heading('ID',text="ID")
		self.product_table.heading('NAME',text="NAME")
		self.product_table.heading('DESCRIPTION',text="DESCRIPTION")
		self.product_table.heading('PRICE',text="PRICE")
		self.product_table.heading('QUANTITY',text="QUANTITY")
		self.product_table.heading('DATE_IN',text="DATE_IN")
		self.fetch_all()

	def clear(self):
		self.id_var.set('')
		self.name_var.set('')
		self.description_var.set('')
		self.price_var.set('')
		self.quantity_var.set('')
		self.date_in_var.set('')
		self.delete_product_var.set('')

	def add_product(self):
		mydb = c.connect(
  		host="localhost",
 		user="root",
   		password="",
   		database="stock")
		my_cursor= mydb.cursor()
		query = "SELECT * FROM product WHERE ID=%s"
		my_cursor.execute(query, (self.id_var.get(),))
		row = my_cursor.fetchone()
		if row == None:
			if self.quantity_var.get() <= 5 :
				messagebox.showinfo(title='warning',message='quantity is less than 5')
			if self.id_var.get()=='' or self.name_var.get()=='' or self.description_var.get()=='' or self.price_var.get()=='' or self.quantity_var.get()=='' or self.date_in_var.get()=='' :
				messagebox.showerror(title='Error',message='all the fields are required')
			else :
				my_cursor.execute("insert into product values(%s,%s,%s,%s,%s,%s)",(self.id_var.get(),
																				self.name_var.get(),
																				self.description_var.get(),
																				self.price_var.get(),
																				self.quantity_var.get(),
																				self.date_in_var.get()))
				mydb.commit() # do the operation
				self.fetch_all()
				self.clear()
			mydb.close()
		else:
			messagebox.showerror(title='Error', message='ID already exist')
	def fetch_all(self):
		mydb = c.connect(
  		host="localhost",
 		user="root",
   		password="",
   		database="stock")
		my_cursor= mydb.cursor()
		my_cursor.execute("select * from product")
		rows=my_cursor.fetchall()
		self.product_table.delete(*self.product_table.get_children()) #add only the new product to the tree
		for row in rows :
			self.product_table.insert("",END,values=row)
			mydb.commit() # do the operation
		mydb.close()
		
	def update_product(self):
		mydb = c.connect(
  		host="localhost",
 		user="root",
   		password="",
   		database="stock")
		my_cursor= mydb.cursor()
		query="SELECT * FROM product where ID=%s"
		my_cursor.execute(query,(self.id_var.get(),))
		row=my_cursor.fetchone()
		if row != None :
			my_cursor.execute("update product set NAME=%s,DESCRIPTION=%s,PRICE=%s,QUANTITY=%s,DATE_IN=%s where ID=%s ",(
																	self.name_var.get(),
																	self.description_var.get(),
																	self.price_var.get(),
																	self.quantity_var.get(),
																	self.date_in_var.get(),
																	self.id_var.get()))
			mydb.commit() # do the operation
			self.fetch_all()
			self.clear()			
			mydb.close()
		else:
			messagebox.showerror(title='Error',message='product don t exist')


	def delete_product(self):
		mydb = c.connect(
  		host="localhost",
 		user="root",
   		password="",
   		database="stock")
		my_cursor= mydb.cursor()
		query="delete from product where NAME=%s"
		my_cursor.execute(query,(self.delete_product_var.get(),))
		mydb.commit() # do the operation
		self.fetch_all()
		self.clear()
		mydb.close() 

	def search(self):
		mydb = c.connect(
  		host="localhost",
 		user="root",
   		password="",
   		database="stock")
		my_cursor= mydb.cursor()
		my_cursor.execute("select * from product where " + str(self.search_by_var.get()) + " like '%" + str(self.search_var.get()) + "%'")
		rows=my_cursor.fetchall()
		self.product_table.delete(*self.product_table.get_children()) #add only the new product to the tree
		for row in rows :
			self.product_table.insert("",END,values=row)
			mydb.commit() # do the operation
		mydb.close()
	
	
home_page=Tk()
ob=product(home_page)

def login_page():
    home_page.destroy()
    import login_page
    
menubar=Menu(home_page)
f= Menu(menubar, tearoff=0)
f.add_command(label='Logout',command=login_page)
f.add_separator()
f.add_command(label='Exit',command=home_page.quit)
menubar.add_cascade(label='Menu',menu=f) #cascade to give name to the variable menu
home_page.config(menu=menubar) # for display the menu

home_page.iconbitmap('images/home.ico')

home_page.mainloop()


