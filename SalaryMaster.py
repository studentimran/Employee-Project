from pymysql import *
from tkinter import *
from tkinter import messagebox as msg
class Salary(Frame):
	def __init__(self,master):
		super().__init__(master)
		
		self.l1=Label(self,bg='light blue',bd=2,text='Designation',font=('algerian',12))
		
		self.t1=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		
		self.l2=Label(self,bg='light blue',bd=2,text='Minmum Salary',font=('algerian',12))
		
		self.t2=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		
		self.l3=Label(self,bg='light blue',bd=2,text='Maximum Salary',font=('algerian',12))
		
		self.t3=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		
		
		self.b1=Button(self,font=('algerian',13),bd=2,bg='gray',text='Add',padx=8,pady=5)
		self.b2=Button(self,font=('algerian',13),bd=2,bg='gray',text='Exit',padx=8,pady=5)
		
		self.columnconfigure(0, pad=5)
		self.columnconfigure(1, pad=5)
		
		self.rowconfigure(0, pad=5)
		self.rowconfigure(1, pad=5)
		self.rowconfigure(2, pad=5)
		
		self.l1.grid(row=0,column=0)
		self.t1.grid(row=0,column=1)
		
		self.l2.grid(row=1,column=0)
		self.t2.grid(row=1,column=1)
		
		self.l3.grid(row=2,column=0)
		self.t3.grid(row=2,column=1)
		
		
		self.b1.grid(row=3,column=0)
		self.b2.grid(row=3,column=1)
		
		
		self.pack()
	