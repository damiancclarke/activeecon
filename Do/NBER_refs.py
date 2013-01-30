import re

ResultA0 = open("ResultA0.txt", "w") # this is the file which will give final output
ResultA1 = open("ResultA1.txt", "w") # this is the file which will give final output

for line in open("A_NBER_papers.txt"):
	folder = line[0:2]
	p = re.findall('w[0-9]+', line)	
	year = line[-11:-7]
	print year
	for a in p:
		papercode = a
		print papercode	
	
	txtpaper = "../" + 'txts' + "/A/" + folder + "/" + papercode + ".txt"
	txtpaperread = open(txtpaper, 'r').read()
	
	#***************************************************************************
	# I just have to make these reasonably poorly stripped bibliographies be
	# written into the files ResultA0, ResultA1.  make a name of 
	#***************************************************************************
	references = re.search('\b references', txtpaperread)
	if references!=None:
		refposition=references.start()
#		print txtpaperread[refposition:refposition+10000]
	References = re.search('References', txtpaperread)
	if References!=None:
		Refposition = References.start()
		ResultA0.write(txtpaperread[Refposition:Refposition+5000] + "\n")
	REFERENCES = re.search('REFERENCES', txtpaperread)
	if REFERENCES!=None:
		REFposition = REFERENCES.start()
		ResultA0.write(txtpaperread[REFposition:REFposition+5000] + "\n")


ResultA0.close()
ResultA1.close()









#	RS = ['References', 'REFERENCES']
#	for r in RS:
#		print r
#		Result.write("\n" + papercode + "\n")
#		line_nr = 0
#		for line in txtpaperread:
#			line_nr += 1
#			has_match = line.find(r)
#			if has_match >= 0:
#				print 'Found in line %d' % (line_nr)
#				string = linecache.getline(txtpaper, line_nr)
#				Result.write(string + "\n")

#Result.close()

