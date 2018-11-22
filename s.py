
import json

from torah.models import Word

def wt():
	paleo = json.loads(open('torah/json/paleo/genesis.json').read())
	paleo_data = paleo['text'][0]

	trans_data = json.loads(open('genesis1.json').read())

	for i,line in enumerate(paleo_data):
		t = trans_data['text'][i][::-1]
		#if i ==2:break
		for j,word in enumerate(line.split(' ')):
			print (word,t[j])
			item = Word.objects.get(name = word)
			if item.translation:
				print('There is already a translation')
			else:
				item.translation = t[j]
				item.save()
			#print(item)

	
