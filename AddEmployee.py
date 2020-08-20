from pymysql import *
from tkinter import *
from tkinter import messagebox as msg
class Employee(Frame):
	def __init__(self,master):
		super().__init__(master)
		
		self.l1=Label(self,bg='light blue',bd=2,text='Employee No',font=('algerian',12))
		
		self.t1=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		
		self.l2=Label(self,bg='light blue',bd=2,text='Employee Name',font=('algerian',12))
		
		self.t2=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		
		self.l3=Label(self,bg='light blue',bd=2,text='Salary',font=('algerian',12))
		
		self.t3=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		
		self.l4=Label(self,bg='light blue',bd=2,text='Designation',font=('algerian',12))
		
		self.t4=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		
		self.l5=Label(self,bg='light blue',bd=2,text='Department No',font=('algerian',12))
		
		self.t5=Entry(self,bg='light blue',bd=3,font=('olephant',12,'bold'),justify='center')
		
		self.b1=Button(self,font=('algerian',13),bd=2,bg='gray',text='Add Employee',padx=8,pady=5,command=self.addEmp)
		
		self.b2=Button(self,font=('algerian',13),bd=2,bg='gray',text='Modify',padx=8,pady=5)
		
		self.b3=Button(self,font=('algerian',13),bd=2,bg='gray',text='Search',padx=8,pady=5)
		
		self.b4=Button(self,font=('algerian',13),bd=2,bg='gray',text='Exit',padx=8,pady=5)
		
		self.columnconfigure(0, pad=5)
		self.columnconfigure(1, pad=5)
		self.columnconfigure(2, pad=5)
		self.columnconfigure(3, pad=5)
		
		self.rowconfigure(0, pad=5)
		self.rowconfigure(1, pad=5)
		self.rowconfigure(2, pad=5)
		self.rowconfigure(3, pad=5)
		self.rowconfigure(4, pad=5)
		
		self.l1.grid(row=0,column=0)
		self.t1.grid(row=0,column=1)
		
		self.l2.grid(row=0,column=2)
		self.t2.grid(row=0,column=3)
		
		self.l3.grid(row=1,column=0)
		self.t3.grid(row=1,column=1)
		
		self.l4.grid(row=1,column=2)
		self.t4.grid(row=1,column=3)
		
		self.l5.grid(row=2,column=0)
		self.t5.grid(row=2,column=1)
		
		self.b1.grid(row=3,column=0)
		self.b2.grid(row=3,column=1)
		
		self.b3.grid(row=3,column=2)
		self.b4.grid(row=3,column=3)
		
		self.pack()
	def addEmp(self):
		con=connect(db='employee',user='root',passwd='root',host='localhost')
		cur=con.cursor()
		eno=(int)(self.t1.get())
		ename=self.t2.get()
		sal=(int)(self.t3.get())
		desig=self.t4.get()
		dno=(int)(self.t5.get())
		try:
			cur.execute("select * from dept where deptno=%d"%(dno))
			rs=cur.fetchall()
			if len(rs)>0:
				try:
					cur.execute("select maxsal,minsal from salarymaster where desig='%s'"%(desig))
					rs1=cur.fetchall()
					mins=rs1[0][1]
					maxs=rs1[0][0]
					if sal>=mins and sal<=maxs:
						usr='user'
						cur.execute("insert into masterroll values(%d,'%s',%d,'%s',%d)"%(eno,ename,sal,desig,dno))
						con.commit()
						cur.execute("insert into login values(%d,'%s','%s')"%(eno,desig,usr))
						con.commit()
						msg.showinfo('Save','Record Saved')
				except:
					msg.showerror('Desig Error','Designation Not created')
		except Exception as e:
			msg.showwarning('Warning','Department Not Created')
			
			
			
			
			
			
			
			
			
			
			