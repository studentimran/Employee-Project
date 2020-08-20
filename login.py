from admin import *
from pymysql import *
from tkinter import *
from tkinter import messagebox as msg
from UserPanel import *
class Login(Frame):
	def __init__(self,master):
		super().__init__(master)
		global eno	
		self.l1=Label(self,bg='light blue',bd=2,text='User Name',font=('algerian',12))
			
		self.l2=Label(self,bg='light blue',bd=2,text='Password',font=('algerian',12))
			
		self.t1=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		self.t2=Entry(self,bg='light blue',show='*',bd=3,font=('olephant',12,'bold'),justify='center')
			
		self.b1=Button(self,font=('algerian',13),bd=2,bg='gray',text='login',padx=8,pady=5,command=self.check)
		
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
	def check(self):
		con=connect(db='employee',user='root',passwd='root',host='localhost')
		cur=con.cursor()
		userid=self.t1.get()
		passwd=self.t2.get()
		try:
			i=cur.execute("select usertype,userid from login where userid='%s' and passwd='%s'"%(userid,passwd))
			rs=cur.fetchall()
			if rs[0][0]=='admin':
				r1=Tk()
				ob1=Admin(r1)
				r1.title('Admin Form')
				r1.geometry('600x100')
				r1.mainloop()
			else:
				r1=Tk()
				eno=rs[0][1]
				ob1=UserP(r1)
				r1.title('User Form')
				r1.geometry('600x100')
				r1.mainloop()
		except:
			msg.showerror('Error Info','either username or password is wrong')
root=Tk()
obj=Login(root)
root.title('Login Form')
root.geometry('500x150')
root.mainloop()
			
			
			
			
			
			
			
			
			
