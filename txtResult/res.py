from requests import *
import requests
from bs4 import BeautifulSoup
import os

usn_list=[]
prefix="1JB15CS"

begin=1
end=200
file=open("result.txt","w")
usn_list=[prefix + "{0:0>3}".format(x) for x in range(begin,end+1)]
print(usn_list)
print("Copying...")
for usn_no in usn_list:
	url="http://result.vtu.ac.in/cbcs_results2017.aspx?usn="+usn_no+"&sem=3"
	print(url)

	req=requests.get(url)
	htm=req.text
	soup = BeautifulSoup(htm, 'html.parser')
	try:
		name=soup.find('input',{'id':'txtName'}).get('value')
		usnn=soup.find('input',{'id':'txtUSN'}).get('value')
		sgpa=soup.find('span',{'id':'lblSGPA'}).string
		print(usnn)
		file.write(usnn+"\t"+name+"\t"+sgpa+"\n")
	except:
		pass
file.close()

print("Done!")
