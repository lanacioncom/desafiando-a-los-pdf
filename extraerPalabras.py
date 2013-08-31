# -*- coding: utf-8 -*-

import sys
import re

for file in sys.argv[1:]:
	with open(file,'r') as myfile:
	    data=myfile.read().replace('\n', '')
	

	data = re.sub(r'\.',' ',data)
	data = re.sub(r'[^a-zA-Z\s]','',data)
	data = re.split('\s|\t|,', data)
	
	for palabra in data:
		if 1 < len(palabra) < 20 and palabra.lower() != palabra.upper():
			print(palabra.lower().strip())
	
	print(len(data))