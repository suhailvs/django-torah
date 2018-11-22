import urllib.request
from bs4 import BeautifulSoup

parseurl = lambda url: urllib.request.urlopen(url).read()

def soupparser(html_doc):
	soup = BeautifulSoup(html_doc, 'html.parser')
	lines = []
	for i,table in enumerate(soup.find_all('table')):
		for td in table.find_all('td'):
			for line in td('p'):
				#print(line.get_text())
				
				cur_word = []
				cur_line = []
				for word in line('a'):
					#print(word.contents[0].contents)
					cur_word.append(word.get_text())
					#print(word.get_text())
					if '(' in word.next_sibling: #("font", face="david"):
						
						#print(' '.join(cur_word))
						cur_line.append(' '.join(cur_word))
						#print('====')
						cur_word=[]
				if cur_line: 
					#print('-'*20)
					#print(cur_line)
					lines.append(cur_line)
	return lines


# html_doc = parseurl('http://www.mechanical-translation.org/mtt/G1.html')
# fp =open('html.txt','wb')
# fp.write(html_doc)
# fp.close()

fp =open('html.txt')
html_doc = fp.read()
data = { 
    "versionTitle": "Paleo Hebrew Word by Word, http://www.mechanical-translation.org/mtt/G1.html",
    "language": "eg", 
    "title": "Genesis", 
    "text": soupparser(html_doc)
}
import json
with open('genesis1.json', 'w') as outfile:
    json.dump(data, outfile,indent = 4)
