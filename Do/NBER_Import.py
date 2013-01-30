#  NBER_Import 1.00           Damian C Clarke                    vers:2013-01-29
#---|----1----|----2----|----3----|----4----|----5----|----6----|----7----|----8
#
# This is a program which imports all papers from NBER and strips the bibliogra-
# phic information from them.  The program is written for unix based systems, as
# the command pdftotext (line 93) is a unix shell based command.  For windows
# users the program can be run using python's pdf2txt module (comment out line
# 93 and comment in line 94), however the performance is considerably slower, 
# (approximately 10 times slower when run on my machine).
#
# Comments or questions can be sent to damian.clarke@economics.ox.ac.uk

#*******************************************************************************
# (1) Import required packages, set-up names used in urls and to save files
#*******************************************************************************
import os
import urllib
import urllib2
from urllib2 import urlopen, URLError, HTTPError
import re
import webbrowser

papers = open("NBER_papers.txt", "w")

url1 = 'http://www.nber.org/jel/'
url2 = 'http://www.nber.org/papers/'
url3 = '_index.html'
url4 = '.html'

savefile1 = "../pdfs/"
savefile2 = "../txts/"

#*******************************************************************************
# (2) For each JEL code get all relevant JEL subcode
#*******************************************************************************
JEL = "ABCDEFGHIJKLMNOPQRZ"
for x in JEL:
	if not os.path.exists(savefile1 + "/" + x): # make files to save pdfs
		os.makedirs(savefile1 + "/" + x)
		
	suburl = url1 + x + url3
	JELpage = urllib2.urlopen(suburl).read()
	preJEL = re.findall('\(<b>[A-Z][0-9]</b>\) [a-zA-Z0-9 ]*', JELpage) # find JEL subcode
	for m in preJEL:
		subJEL1 = m[4:6]
		if not os.path.exists(savefile1 + "/" + x + "/" + subJEL1): # make subfiles for pdfs
			os.makedirs(savefile1 + "/" + x + "/" + subJEL1)

		subJELtitle = m[12:]
		subJEL = url1 + subJEL1 + url4
		print m
		subJELpage = urllib2.urlopen(subJEL).read()
		paperpage = re.findall('<a href="http://www.nber.org/papers/w[0-9]*', subJELpage) # find address of each paper
		#***********************************************************************
		# (3) Take each paper from this JEL code page (eg A0, A1,...) and unpack
		#***********************************************************************		
		for p in paperpage: #strip paper names, authors, dates and urls
			print p
			papercode = p[36:]
			paperurl = p[9:]
			print(papercode)
			print(paperurl)
			openpaper = urllib2.urlopen(paperurl).read()
			papername = re.findall('<meta name="citation_title" content="[a-zA-Z0-9 -:\(\)?\$<>/]*"', openpaper)
			for n in papername: # should be one name
				pname = n[37:-1]
				print pname
				
			author = re.findall('<meta name="citation_author" content="[a-zA-Z, ]*"', openpaper)
			aname = "authors:"
			for a in author: # could be multiple authors
				aname = aname + a[38:-1] + ";"
			date = re.findall('<meta name="citation_date" content="[0-9]*-[0-9]*-[0-9]*"', openpaper)

			for d in date: # should be one date
				dname = d[36:-1]

			download = re.findall('<meta name="citation_pdf_url" content="http://www.nber.org/papers/w[0-9]*.pdf"', openpaper)
			for w in download: # must be one url
				wname = w[39:-1]

			#***********************************************************************
			# (4) Write file with all papers and their details and download
			#***********************************************************************		
			papers.write(subJEL1 + "\t" + subJELtitle + "\t" + papercode + "\t" + pname + "\t" + aname + "\t" + dname + "\n")
			savename1 = savefile1 + x + "/" + subJEL1 + "/" + papercode + ".pdf"
			savename2 = savefile2 + "/" + x + "/" + subJEL1 + "/" + papercode + ".txt"
			
			urllib.urlretrieve(wname ,savename1) #get paper, save on OS

			system = "pdftotext " + savename1 # create UNIX-based system cmd
			#system = "pdf2txt.py -o " + savename2 + " " + savename1
			os.system(system)

papers.close()

#*******************************************************************************
# (5) Get references and reference years from txts
#*******************************************************************************

