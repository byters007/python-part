import re

skippingKeywords = ["Table" , "Course" , "Code"]
instKeywords = ["Indian Institute" , "Indian School" , "Institute of Technology,"]
raw = open("programmeCode.txt",'rb')
regex = re.compile("[A-Z][0-9][0-9][0-9][0-9]?")
regexnum = re.compile("[0-9][0-9]([0-9])?")
institutes=[]
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
    if c == '\t':
      while (len(result) % tabstop != 0):
        result += ' ';
    elif c=='\f':
    	continue
    else:
      result += c    
  return result

formattedFile = open("Formatted.txt" , 'w')
for line in raw.readlines():
	formattedFile.write(line[0:72])
	formattedFile.write(line[72:])
formattedFile.close()

data = open("Formatted.txt",'rb')
for line in data.readlines():	
	words = line.split()
	if len(words) == 0 or len(words) == 1:
		continue
	else:
		if words[0] in skippingKeywords:
			continue
		
		numberOfInstitutes = line.count(instKeywords[0]) + line.count(instKeywords[1]) +  line.count(instKeywords[2])
		if (numberOfInstitutes == 0 ):
			#	print line
			p = regexnum.search(line)
			institutes[positionOne].append(line[0:72])			 #for correcting line52 in programmeCode.txt
			#institutes[positionTwo].append(line[0:m.end()])
			institutes[positionTwo].append(line[72:])
				
		if (numberOfInstitutes == 1 ):
			firstHalf = line[0:72]
			secondHalf = line[72:]
			wordsInFirstHalf = firstHalf.split()
			if len(wordsInFirstHalf) != 0:
				if toString(wordsInFirstHalf[0:2]) in instKeywords[0:2]:
					institutes.append([toString(words[0:5])])
					positionOne = len(institutes)-1
					#print institutes[positionOne]

				elif toString(words[0:3]) in instKeywords[2:1]:
					institutes.append([toString(words[0:7])])
					positionOne = len(institutes)-1
				else:
					institutes[positionOne].append( line[0:line.find("Indian")] )
					institutes.append( [line[line.find("Indian"):] ] )
					positionTwo = len(institutes)-1
			else:
					institutes[positionOne].append( line[0:line.find("Indian")] )
					institutes.append( [line[line.find("Indian"):] ] )
					positionTwo = len(institutes)-1


		if (numberOfInstitutes == 2):
			institutes.append([ toString(words[0:5]) ])
			positionOne = len(institutes)-1
			institutes.append([ toString(words[5:]) ])
			positionTwo = len(institutes)-1
			
for list in institutes:
	for number in list:
		print number
	print 
	print







	if p!= None and m!= None:
			
		if p== None:
			words = line.split()
			if len(words)>=2:
				if toString(words[0:2]) in instKeywords or toString(words[0:3]) in instKeywords:
					lastInsti = line
				else
					program += line

		print lastInsti + "," + program+ ","+ line[m.start():end]
