import os
import random
from datetime import datetime


class create_file():
	def __init__(self,name_file,data=None,update=None):
		self.name_file = name_file
		self.file = open(self.name_file,"a")

		if data == None:
			self.file.write(" ")
			self.file.close()
		if update == True:
			file = open(self.name_file,"w")
			file.write(data)
			file.close()
		if data:
			self.file.write(data)
			self.file.close()

	def create_format_text(self,text,formats=None,double=None):
		self.text = text
		self.format = formats
		self.double = double
		format_data = {'bold':{'open':'<b>','close':'</b>'},
	    'italic':{'open':'<i>','close':'</i>'},
	    'underline':{'open':'<u>','close':'</u>'},
        'small':{'open':'<small>','close':'</small>'},
	    'strong':{'open':'<strong>','close':'</strong>'},
	    'sub':{'open':'<sub>','close':'</sub>'},
	    'sup':{'open':'<sup>','close':'</sup>'},
	    'ins':{'open':'<ins>','close':'</ins>'},
	    'mark':{'open':'<mark>','close':'</mark>'}
	    }
		if formats and double == None:
			create_file(self.name_file,data=None)
		else:
			data_s = format_data[self.format]['open'] + text + format_data[self.format]['close']
			create_file(self.name_file,data=data_s)



a = create_file("index.html")
a.create_format_text("Anjing", formats="bold")
