from SalaryMaster import *
from Attendence import *
from tkinter import *
class UserP(Frame):
	def __init__(self,master):
		super().__init__(master)
		self.b1=Button(self,font=('algerian',12,'bold'),bd=4,bg='light blue',padx=8,pady=8,text='Attendence',command=self.attend)
		
		self.b2=Button(self,font=('algerian',12,'bold'),bd=4,bg='light blue',padx=8,pady=8,text='Change Password')
		
		self.b3=Button(self,font=('algerian',12,'bold'),bd=4,bg='light blue',padx=8,pady=8,text='PF')
		
		self.b4=Button(self,font=('algerian',12,'bold'),bd=4,bg='light blue',padx=8,pady=8,text='Salary')
		
		self.columnconfigure(0, pad=5)
		self.columnconfigure(1, pad=5)
		self.columnconfigure(2, pad=5)
		self.columnconfigure(1, pad=5)
		self.rowconfigure(0, pad=3)
		
		
		self.b1.grid(row=0,column=0)
		self.b2.grid(row=0,column=1)
		self.b3.grid(row=0,column=2)
		self.b4.grid(row=0,column=3)
		self.pack()
	def attend(self):
	
		r2=Tk()
		ob=attendence(r2)
		r2.title('Attendence')
		r2.geometry('400x250')
		r2.mainloop()