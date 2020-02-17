#Author: Emmanuel Mtera
#This scripts is able to help you write the same text of information across multiple files
#websites : www.vijanatech.com
#programming language : Python

#here we are going to write out this information

information = """ This is my new written file """


create = [
	'filename', 'filename', 'filename'
]

ext = '.html'

for n in create:
	file = open('{}{}'.format(n,ext), 'w')
	file.write(information)
	file.close()
