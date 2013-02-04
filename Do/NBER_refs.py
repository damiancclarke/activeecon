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

NoRefs = open('NoRefs.txt', 'w')


JEL = "ABCDEFGHIJKLMNOPQRZ"
for x in JEL:
	if not os.path.exists("../refs"): # make files to save biblio txts
		os.makedirs("../refs")
	if not os.path.exists("../refs/" + x): # make files to save biblio txts
		os.makedirs("../refs/" + x)

for y in range(2000,2014):	
	for line1 in open('JEL_codes.txt'):
		filename = '../refs/' + line1[0:1] + '/Result' + line1[0:2] + str(y) + '.txt'
		key = open(filename, 'w')
	
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

			references = None
			References = None
			REFERENCES = None

			if line1[0:2]==line[0:2] and str(y) == str(year):
#				print papercode, folder, subfolder
				txtpaper = "../" + "pdfs" + "/" + folder + "/" + subfolder + "/" + papercode + ".txt"
				txtpaperread = open(txtpaper, 'r').read()
	
				#***************************************************************
				# I just have to make these reasonably poorly stripped bibliographies be
				# written into the files ResultA0, ResultA1.  make a name of 
				#***************************************************************
#				references = re.search('\b references', txtpaperread)
#				if references!=None:
#					refposition=references.start()
				References = re.search('References', txtpaperread)
				if References!=None:
					Refposition = References.start()
					key.write("PAPERNUMBER=" + papercode + subfolder + "\n")
					key.write(txtpaperread[Refposition:Refposition+10000] + "\n")
				REFERENCES = re.search('REFERENCES', txtpaperread)
				if REFERENCES!=None:
					REFposition = REFERENCES.start()
					key.write(txtpaperread[REFposition:REFposition+10000] + "\n")
				REF2 = re.search('R EFERENCES', txtpaperread)
				if REF2!=None:
					REF2position = REF2.start()
					key.write(txtpaperread[REF2position:REF2position+10000] + "\n")					
				REF3 = re.search('Bibliography', txtpaperread)
				if REF3!=None:
					REF3position = REF3.start()
					key.write(txtpaperread[REF3position:REF3position+10000] + "\n")					
				REF4 = re.search('Referemces', txtpaperread)
				if REF4!=None:
					REF4position = REF4.start()
					key.write(txtpaperread[REF4position:REF4position+10000] + "\n")					
				REF5 = re.search('Works Cited', txtpaperread)
				if REF5!=None:
					REF5position = REF5.start()
					key.write(txtpaperread[REF5position:REF5position+10000] + "\n")					
				REF6 = re.search('Literature Cited', txtpaperread)
				if REF6!=None:
					REF6position = REF6.start()
					key.write(txtpaperread[REF6position:REF6position+10000] + "\n")					
				REF7 = re.search('Literature cited', txtpaperread)
				if REF7!=None:
					REF6position = REF7.start()
					key.write(txtpaperread[REF7position:REF7position+10000] + "\n")					
				REF8 = re.search('Further Reading', txtpaperread)
				if REF8!=None:
					REF8position = REF8.start()
					key.write(txtpaperread[REF8position:REF8position+10000] + "\n")					
				REF9 = re.search('WORKS CITED', txtpaperread)
				if REF9!=None:
					REF9position = REF9.start()
					key.write(txtpaperread[REF9position:REF9position+10000] + "\n")					






				if REFERENCES==None and References==None and REF2==None and REF3==None and REF4==None and REF5==None and REF6==None and REF7==None and REF8==None and REF9==None:
					print subfolder, papercode
					NoRefs.write(subfolder + '\t' + papercode + '\n')

	

		key.close()
NoRefs.close()
