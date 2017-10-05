import os, sys
import requests
from requests import *
from tkinter import *
from urllib3 import *



from tkinter import messagebox
	
top=Tk()
top.title("VTU Results")

top.geometry("600x300")

def copy():
	usnfrm=fusn.get()
	usnto=tousn.get()
	semester=sem.get()


	if usnfrm=="":
		msg1=messagebox.showinfo( "Alert", "Enter the starting USN")

	elif usnto=="":
		msg2=messagebox.showinfo( "Alert", "Enter the ending USN")
	elif semester=="":
		msg3=messagebox.showinfo( "Alert", "Enter the semester")
	else:
		usn_list=[]
		prefix=usnfrm[:7]

		begin=usnfrm[7:]
		begin=int(begin)
		end=usnto[7:]
		end=int(end)

		usn_list=[prefix + "{0:0>3}".format(x) for x in range(begin,end+1)]
		os.mkdir("result")

		for usn_no in usn_list:
			url="http://result.vtu.ac.in/cbcs_results2017.aspx?usn="+usn_no+"&sem="+semester+""
			req=requests.get(url)
			req_html=req.text

			f=open("result/"+str(usn_no)+".html","w")
			f.write(req_html)
			f.close()
		msg2=messagebox.showinfo( "Complete", "Requested file downloaded.")


title_head=Label(top,text="VTU Result Downloader v1.0",font=("monospace",13), bg="#374140", fg="#D9CB9E", padx="300", pady="10")
title_head.pack()

url_text=Label(top, text="Enter the USN range and semester:")
url_text.pack()
url_text.place(x=200, y=50)


frtxt=Label(top, text="From (USN)", font=("monospace",8))
frtxt.pack()
frtxt.place(x=100, y=100)

totxt=Label(top, text="To (USN)", font=("monospace",8))
totxt.pack()
totxt.place(x=250, y=100)

semtxt=Label(top, text="Sem", font=("monospace",8))
semtxt.pack()
semtxt.place(x=400, y=100)




fusn=Entry(top,width=13)
fusn.pack()
fusn.place(x=100, y=120)

tousn=Entry(top,width=13)
tousn.pack()
tousn.place(x=250, y=120)

sem=Entry(top,width=6)
sem.pack()
sem.place(x=400, y=120)

button=Button(top, text="Download", bg="#374140", fg="#D9CB9E",command=copy)
button.pack()
button.place(x=250, y=180)


des=Label(top,text="Coded with LOVE by Sohaib Alam", font=("monospace",8))
des.pack(side="bottom", pady=10)
top.mainloop()
