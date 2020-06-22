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
			data =f'<!DOCTYPE html><html><head><title>{title}</title>'
			create_file(self.name_file,css=None, data=data, update=None)
		if favicon:
			data =f'<link rel="shortcut icon" href="{favicon}">'
			create_file(self.name_file,css=None, data=data, update=None)

	def create_paragraf(self, text, align=None, double=None):
		self.align = align
		self.double = double
		p_align = {'left':{'open':'<p align="left">','close':'</p>'},
		'right':{'open':'<p align="right">','close':'</p>'},
		'center':{'open':'<p align="center">','close':'</p>'},
		'justivy':{'open':'<p align="justivy">','close':'</p>'}}
		if align:
			data_s = format_data[self.align]['open'] + text + format_data[self.align]['close']
			create_file(self.name_file,css=None, data=data_s, update=None)

		if double:
			data_d = f"<{self.double}>" + format_data[self.align]['open'] + text + format_data[self.align]['close'] +f"</{self.double}>"
			create_file(self.name_file,css=None, data=data_d, update=None)




	def create_hyperlink(self,text,url=None, double=None):
		self.url = url
		self.double = double
		if url:
			data_c = f'<a href ="{url}">{text}</a>'
			create_file(self.name_file,css=None, data=data_c, update=None)

		if double:
			data_d = f'<{self.double}>'+f'<a href ="{url}">{text}</a>'+f'</{self.double}>'
			create_file(self.name_file,css=None, data=data_d, update=None)

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
		if formats:
			data_s = format_data[self.format]['open'] + text + format_data[self.format]['close']
			create_file(self.name_file,css=None, data=data_s, update=None)
