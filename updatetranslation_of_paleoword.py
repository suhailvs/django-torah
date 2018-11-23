
import json

from torah.models import Word

def wt():
	paleo = json.loads(open('torah/json/paleo/genesis.json').read())
	trans = json.loads(open('torah/json/mtt/genesis.json').read())
	paleo_data = paleo['text']
	trans_data = trans['text']
	
	for chapter in paleo_data:
		for i,line in enumerate(chapter):
			t = trans_data['text'][i][::-1]
			for j,word in enumerate(line.split(' ')):
				item = Word.objects.get(name = word)
				if item.translation:
					print('There is already a translation')
				else:
					item.translation = t[j]
					item.save()

	
