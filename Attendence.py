from datetime import *
from tkinter import *
from pymysql import *
from login import *
from tkinter import messagebox as msg
class attendence(Frame,Login):
	def __init__(self,master):
		super().__init__(master)
		
		self.l1=Label(self,bg='light blue',bd=2,text='Employee No',font=('algerian',12))
		
		self.t1=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		
		self.b1=Button(self,font=('algerian',13),bd=2,bg='gray',text='Time in',padx=8,pady=5,command=self.timein)
		
		self.b2=Button(self,font=('algerian',13),bd=2,bg='gray',text='Time Out',padx=8,pady=5)
		
		self.columnconfigure(0, pad=5)
		self.columnconfigure(1, pad=5)
		
		self.rowconfigure(0, pad=5)
		self.rowconfigure(1, pad=5)
		
		self.l1.grid(row=0,column=0)
		self.t1.grid(row=0,column=1)
		
		self.b1.grid(row=1,column=0)
		self.b2.grid(row=1,column=1)
		
		self.pack()
	def timein(self):
		con=connect(db='employee',user='root',passwd='root',host='localhost')
		cur=con.cursor()
		dt=Datetime.now()
		h=dt.hour()
		m1=dt.minute()
		s=dt.second()
		y=dt.year()
		m=dt.month()
		d=dt.day()
		tin=str(h)+':'+str(m1)+':'+str(s)
		tout=0
		adate=str(d)+"-"+str(m)+"-"+str(y)
		try:
			cur.execute("select * from monthly where adate='%s' "%(adate))
			rs=cur.fetchall()
			if len(rs)>0:
				msg.showerror('Error','Duplicate Attendence for date')
		except:
			cur.execute("insert into monthly values(%d,'%s','%s','%s')"%(eno,adate,tin,tout))
			con.commit()
			
			
			
			
			
			
			