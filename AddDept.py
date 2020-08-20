from pymysql import *
from tkinter import *
from tkinter import messagebox as msg
class Dept(Frame):
	def __init__(self,master):
		super().__init__(master)
		
		self.l1=Label(self,bg='light blue',bd=2,text='Department No',font=('algerian',12))
		
		self.t1=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		
		self.l2=Label(self,bg='light blue',bd=2,text='Department Name',font=('algerian',12))
		
		self.t2=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		
		self.b1=Button(self,font=('algerian',13),bd=2,bg='gray',text='Save',padx=8,pady=5,command=self.save)
		
		self.columnconfigure(0, pad=5)
		self.columnconfigure(1, pad=5)
		
		
		self.rowconfigure(0, pad=5)
		self.rowconfigure(1, pad=5)
		self.rowconfigure(2, pad=5)
		
		self.l1.grid(row=0,column=0)
		self.t1.grid(row=0,column=1)
		
		self.l2.grid(row=1,column=0)
		self.t2.grid(row=1,column=1)
		
		self.b1.grid(columnspan=2)
		self.pack()
	def save(self):
		con=connect(db='employee',user='root',passwd='root',host='localhost')
		cur=con.cursor()
		dno=(int)(self.t1.get())
		dnam=self.t2.get()
		try:
			i=cur.execute("insert into dept values(%d,'%s')"%(dno,dnam))
			if i>=1:
				con.commit()
				msg.showinfo('Confirmation','Record Saved')
				self.t1.delete(0,'end')
				self.t2.delete(0,'end')
				self.t1.focus()
			con.close()
		except:
			msg.showerror('Error','Record Not Saved')