from SalaryMaster import *
from AddEmployee import *
from AddDept import *
from tkinter import *
class Admin(Frame):
	def __init__(self,master):
		super().__init__(master)
		
		self.b1=Button(self,font=('algerian',12,'bold'),bd=4,bg='light blue',padx=8,pady=8,text='Add Dept',command=self.dept)
		
		self.b2=Button(self,font=('algerian',12,'bold'),bd=4,bg='light blue',padx=8,pady=8,text='Add Employee',command=self.addemp)
		
		self.b3=Button(self,font=('algerian',12,'bold'),bd=4,bg='light blue',padx=8,pady=8,text='Create Salary',command=self.salary)
		
		self.columnconfigure(0, pad=5)
		self.columnconfigure(1, pad=5)
		self.columnconfigure(2, pad=5)
		
		self.rowconfigure(0, pad=3)
		
		self.b1.grid(row=0,column=0)
		self.b2.grid(row=0,column=1)
		self.b3.grid(row=0,column=2)
		
		self.pack()
	def dept(self):
		root=Tk()
		ob=Dept(root)
		root.title('Department')
		root.geometry('500x200')
		root.mainloop()
	def addemp(self):
		root=Tk()
		ob=Employee(root)
		root.title('Employee')
		root.geometry('700x300')
		root.mainloop()
	def salary(self):
		root=Tk()
		ob=Salary(root)
		root.title('Salary Master')
		root.geometry('500x200')
		root.mainloop()	