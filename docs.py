import os
import random
from datetime import datetime


class create_file():
	def __init__(self,name_file,css=None,data=None,update=None):
		self.name_file = name_file
		self.file = open(self.name_file,"a")
		self.css = css

		if css:
			data = f'<link rel="stylesheet" type="text/css" href="{self.css}">'
			self.file.write(data)
		if data:
			self.file.write(data)
		if update :
			file = open(self.name_file,"w")
			file.write(data)
			
	def start(self, title=None, favicon=None):
		if title:
			data =f'<!DOCTYPE html><html><head><title>{title}</title></head><body>'
			create_file(self.name_file,css=None, data=data, update=None)
		if favicon:
			data =f'<link rel="shortcut icon" href="{favicon}">'
			create_file(self.name_file,css=None, data=data, update=None)

	def create_paragraf(self, text,double=None):
		self.align = align
		self.double = double
		if align:
			data_s = f"<p>{ text }</p>"
			create_file(self.name_file,css=None, data=data_s, update=None)

		if double:
			data_d = f"<{self.double}>" + "<p>"+ text + "</p>" +f"</{self.double}>"
			create_file(self.name_file,css=None, data=data_d, update=None)
	
	def create_header(self, text, size=None, double=None):
		self.size = size
		header_data = {'1':{'open':'<h1>','close':'</h1>'},
	    '2':{'open':'<h2>','close':'</h2>'},
	    '3':{'open':'<h3>','close':'</h3>'},
	    '4':{'open':'<h4>','close':'</h4>'},
	    '5':{'open':'<h5>','close':'</h5>'},
	    '6':{'open':'<h6>','close':'</h6>'}
		}
		if double:
			data_d = f"<{double}"+ header_data[self.size]['open'] + text + header_data[self.size]['close'] + f"</{double}>"
			create_file(self.name_file,css=None, data=data_d, update=None)
		else:
			data_s = header_data[self.size]['open'] + text + header_data[self.size]['close']
			create_file(self.name_file,css=None, data=data_s, update=None)
	
	def create_list(self, data=None, type=None):
		self.type = type
		data_list = {'ul':{'open':'<ul>','close':'</ul>'},'ol':{'open':'<ol>','close':'</ol>'}}
		data_s = data_list[self.type]['open']
		create_file(self.name_file,css=None, data=data_s, update=None)
		for x in range(len(data)):
			data_c = f"<li>{data[x]}</li>"
			create_file(self.name_file,css=None, data=data_c, update=None)
		create_file(self.name_file,css=None, data=data_list[self.type]['close'], update=None)
		
	def create_table(self, header=None, data=None,border=None):
		self.header = header
			
		create_file(self.name_file,css=None, data=f"<table border='{border}'><tr>", update=None)
			
		for x in range(len(header)):
			data_s = f"<th>{header[x]}</th>"
			create_file(self.name_file,css=None, data=data_s, update=None)
		create_file(self.name_file,css=None, data="</tr><tr>", update=None)
			
			
		for x in range(len(data)):
			data_d = f"<td>{data[x]}</td>"
			create_file(self.name_file,css=None, data=data_d, update=None)
		create_file(self.name_file,css=None, data="</tr>")
	
	def create_iframe(self, url=None , height=None, width=None):
		data_s = '<iframe src = "{url}" height="{height}" width="{witdh}"></iframe>'
		create_file(self.name_file,css=None, data=data_s, update=None)
	
	
	def create_form(self,data=None, action=None, method=None):
		self.action = action
		self.method = method
		
		data_c = f"<form action='{self.action}' method='{self.method}'>"
		create_file(self.name_file,css=None, data=data_c, update=None)
		
		def add_form(n):
			key = list(data[n].keys())
			valu = list(data[n].values())
			result = []
			for x in range(len(key)):
				key_valu = f"{key[x]}" +"="+ f"'{valu[x]}'"
				result.append(key_valu)
				data_s = "<input " +" ".join(result) + "><br>"
			create_file(self.name_file,css=None, data=data_s, update=None)
				
		for x in range(len(data)):
			add_form(x)
		
		
		
		create_file(self.name_file,css=None, data="</form>", update=None)
	
	

	def create_hyperlink(self,text,url=None, double=None):
		self.url = url
		self.double = double

		if double:
			data_d = f'<{self.double}>'+f'<a href ="{url}">{text}</a>'+f'</{self.double}>'
			create_file(self.name_file,css=None, data=data_d, update=None)
		
		else:
			data_c = f'<a href ="{url}">{text}</a>'
			create_file(self.name_file,css=None, data=data_c, update=None)

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
	    'mark':{'open':'<mark>','close':'</mark>'},
	    'code':{'open':'<code>','close':'</code>'}
	    }
	    	
		if double:
			data_d = f"<{self.double}>" + format_data[self.format]['open'] + text + format_data[self.format]['close'] +f"</{self.double}>"
			create_file(self.name_file,css=None, data=data_d, update=None)
			
		else:
			data_s = format_data[self.format]['open'] + text + format_data[self.format]['close']
			create_file(self.name_file,css=None, data=data_s, update=None)
			
	def end(self, view=None):
			
		if view == True:
			data = "</body></html>"
			create_file(self.name_file,css=None, data=data, update=None)
			ukuran = os.path.getsize(self.name_file)
			name = self.name_file
			print(f"Name : { name }  Size : { ukuran }KB")
			f = open(self.name_file,"r").read()
			print(f)
			input("[ OKE ]")
		else:
			data = "</body></html>"
			create_file(self.name_file,css=None, data=data, update=None)
