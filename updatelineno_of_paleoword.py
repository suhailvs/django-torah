import json
from torah.models import Word,Line

def save_word_to_db():
	chap='genesis,exodus,deuteronomy,leviticus,numbers'
	n_lines, n_word, n_letters= 0,0,0
	
	for title in chap.split(','):
		paleo_data = json.loads(open('torah/json/paleo/%s.json'%title).read())
		for i,chapter in enumerate(paleo_data['text']):
			# data_word = []
			# data_line = []
			n_lines+=len(chapter)
			for j,line in enumerate(chapter):
				
				n_word+=len(line.split(' '))
				for word in line.split(' '):
					w = Word.objects.get(name=word)
					l = Line.objects.get(title = title, chapter = i+1, line = j+1)
					w.lines.add(l)
					#if not Word.objects.filter(name=word):
						#data_word.append(Word(name=word))
					n_letters+=len(word)
				# data_line.append(Line(title = title, chapter = i+1, line = j+1))
			
			# Word.objects.bulk_create(data_word)
			# Line.objects.bulk_create(data_line)

	print(n_lines,n_word,n_letters)


