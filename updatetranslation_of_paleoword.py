import json
from torah.models import Word

def wt():
	"""
	USAGE
	=====
	./manage.py shell
	>>> import updatetranslation_of_paleoword
	>>> updatetranslation_of_paleoword.wt()
	"""

	fp_paleo = json.loads(open('torah/json/paleo/genesis.json').read())
	fp_trans = json.loads(open('torah/json/mtt/genesis.json').read())
	paleo_data = fp_paleo['text'] # [['line1','line2'...], ...]
	#trans_data = fp_trans['text'] # [[['word1', ...], ...], ...]
	
	for i in range(len(paleo_data)):
		for j in range(len(paleo_data[i])):
			line = paleo_data[i][j]
			#print(trans_data[i])
			trans = fp_trans['text'][i][j][::-1] #[  [  [
			
			for n,word in enumerate(line.split(' ')):
				item = Word.objects.get(name = word)
				if item.translation:
					print('There is already a translation')
					# print(trans[n])
				else:
					item.translation = trans[n]
					item.save()
