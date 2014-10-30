import re

skippingKeywords = ["Table" , "Course" , "Code"]
instKeywords = ["Indian Institute" , "Indian School" , "Institute of Technology,"]
raw = open("programmeCode.txt",'rb')
regex = re.compile("^[A-Z][0-9][0-9][0-9][0-9]")
regexnum = re.compile("[0-9]([0-9])?([0-9])?")
lastInsti =""
positionOne=0
positionTwo=0
count=0
flag = "true"
def toString(words):
	string = ""
	for i in range(0 , len(words) ):
		string = string +" "+ words[i]

	if len(string) == 0:
		return ""
	return string[1:]
def replace_tab(s, tabstop = 4):
  result = str()
  for c in s:
    if c != '\t':
    	result += c    
  return result

formattedFile = open("Formatted.txt" , 'a')
leftColoumn =[]
rightColoumn = []
for line in raw.readlines():
	words = line.split()
	if len(words) == 0 or len(words) == 1:
		continue
	else:
		if words[0] in skippingKeywords:
			continue
	#leftColoumn.append( re.sub("\t" , "",re.sub("\s\s+" , " ", line[0:72])))
	#rightColoumn.append(re.sub("\t" , "",re.sub("\s\s+" , " ", line[72:])))
	leftColoumn.append(re.sub("\s\s+" , "", line[0:72]))
	rightColoumn.append(re.sub("\s\s+" , "", line[72:]))


for i in leftColoumn:
	formattedFile.write(i)
	formattedFile.write('\n')
for j in rightColoumn:
	formattedFile.write(j)
	formattedFile.write('\n')
formattedFile.close()

with open("Formatted.txt","r") as data:
	for thisLine in data:
		if not thisLine.strip():
			continue
		p = regexnum.search(thisLine)
		m = regex.search(thisLine)
		program =""
		code=""
		if p!= None and m!= None:
			program =  thisLine[p.end():m.start()]
			code = thisLine[m.start():]
			
		if p== None:
			words = thisLine.split()
			if len(words)>=2 and (toString(words[0:2]) in instKeywords or toString(words[0:3]) in instKeywords):
				lastInsti = re.sub('\n' , '' , thisLine)
			else:
				program += re.sub('\n' , '' , thisLine)
		if p!= None and m!= None:
			print lastInsti + "," + program + ","+ code,



