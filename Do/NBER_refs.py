#  NBER_refs 1.00           Damian C Clarke                    vers:2013-01-29
#---|----1----|----2----|----3----|----4----|----5----|----6----|----7----|----8
#
# This is the bibliography scraping component associated with the NBER paper 
# import script.  Here I am finding all occurrences of References in NBER papers
# and stripping out bibliography entries.  The main aim is to capture the date
# of items being cited.  Error capture is not great yet - I need to work on this
# and to test sensitivity of small changes in bibliography removal specificati-
# ons.
#
# Comments or questions can be sent to damian.clarke@economics.ox.ac.uk

#*******************************************************************************
# (1) Import required packages, set-up names used in urls and to save files
#*******************************************************************************
import os
import re

JEL = "ABCDEFGHIJKLMNOPQRZ"
for x in JEL:
	if not os.path.exists("../refs"): # make files to save biblio txts
		os.makedirs("../refs")
	if not os.path.exists("../refs/" + x): # make files to save biblio txts
		os.makedirs("../refs/" + x)

d = {}
for line1 in open('JEL_codes.txt'):
	dictname = '../refs/' + line1[0:1] + '/Result' + line1[0:2] + '.txt'
	d[line1[0:2]] = dictname


for key, value in d.iteritems():
	key = open(value, 'w')

	#***************************************************************************
	# (2) Strip data from bibliography
	#***************************************************************************
	for line in open("NBER_papers.txt"):
		subfolder = line[0:2]
		folder = line[0:1]
		p = re.findall('w[0-9]+', line)	
		year = line[-11:-7]
		name = 'Result' + subfolder
		for a in p:
			papercode = a

		for y in range(2000,2014):	
			if str(y) == str(year) and line1[0:2]==line[0:2]:
				txtpaper = "../" + "pdfs" + "/" + folder + "/" + subfolder + "/" + papercode + ".txt"
				txtpaperread = open(txtpaper, 'r').read()
	
				#***************************************************************
				# I just have to make these reasonably poorly stripped bibliographies be
				# written into the files ResultA0, ResultA1.  make a name of 
				#***************************************************************
				references = None
				References = None
				REFERENCES = None
				
				references = re.search('\b references', txtpaperread)
				if references!=None:
					refposition=references.start()
				References = re.search('References', txtpaperread)
				if References!=None:
					Refposition = References.start()
#					print txtpaperread[Refposition:Refposition+5000]
					key.write(txtpaperread[Refposition:Refposition+5000] + "\n")
				REFERENCES = re.search('REFERENCES', txtpaperread)
				if REFERENCES!=None:
					REFposition = REFERENCES.start()
					key.write(txtpaperread[REFposition:REFposition+5000] + "\n")
				
				if REFERENCES==None and References==None:
					print subfolder, papercode
	
	key.close()
