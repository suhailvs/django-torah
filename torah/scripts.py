import json
from torah.models import Word,Line

"""
USAGE
=====
./manage.py shell
from torah import scripts
helper = scripts.LoadData()
helper.load_words()
helper.link_words_and_lines()
"""

"""
https://judaism.stackexchange.com/a/44235/3087
+ There are 304,805 letters in the Torah.
+ There are 79,976 words in the Torah.
+ There are 5,888 or 5,845 verses in the Torah.
"""
class LoadData:
	def __init__(self):
		self.titles = ['genesis','exodus','leviticus','numbers','deuteronomy']
		self.folder = 'torah/json/'

	def link_words_and_lines(self):
		for line in Line.objects.all():
			words = Word.objects.filter(name__in=line.name.split(' '))
			line.word_set.add(*words)

	def get_chapters(self, title):
		paleo = json.loads(open(f'{self.folder}/paleo/{title}.json').read())
		trans = json.loads(open(f'{self.folder}/mtt/{title}.json').read())
		return {'paleo':paleo['text'], 'trans': trans['text']}

	def load_words(self):
		for title in self.titles:
			words,lines,errors=[],[],[]
			datas = self.get_chapters(title)
			for n_chap,chapter in enumerate(datas['paleo']):
				for n_line,line in enumerate(chapter):
					lines.append(Line(title = title,chapter_no=n_chap+1,line_no=n_line+1,name=line))
					for n_word,word in enumerate(line.split(' ')):
						try:
							translation = datas['trans'][n_chap][n_line][::-1][n_word]
						except:
							# errors.append(f'translation didnt exists - {n_chap}:{n_line}:{n_word}')
							translation = ''
						words.append(Word(name=word, translation=translation))

			Word.objects.bulk_create(words, ignore_conflicts=True)
			Line.objects.bulk_create(lines)
			
			# with open(f'logs/errors_{title}.json', 'w') as outfile:
			# 	json.dump(errors, outfile,indent = 4)

