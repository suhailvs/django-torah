from django.shortcuts import render, redirect
import json

def showline(request, title='genesis', chapter=1, line=1):
	if request.method=='POST':
		return redirect('/%s/%s/%s/'%(request.POST['title'],request.POST['chapter'],request.POST['line']))
	paleo_data = json.loads(open('torah/json/paleo/%s.json'%title).read())
	english_data = json.loads(open('torah/json/english/%s.json'%title).read())
	context = {
		'current': {'title':title, 'chapter':chapter, 'line':line},
		'paleo':paleo_data['text'][chapter-1][line-1],
		'english': english_data['text'][chapter-1][line-1],
	}
	return render(request,'line.html',context)

def showword(request):
	w = request.GET.get('word','')
	trans = ["Ancient", "Pronunciation", "English", "Definition"]
	if w:
		data = json.loads(open('torah/json/paleo/dictionary.json').read())
		for i in range(len(data['text'])):
			word = data['text'][i][0]
			if word == w:
				trans = data['text'][i]
				break
	context = {
		'word': w,
		'pron': trans[1],
		'eng':trans[2],
		'def':trans[3]
	}
	return render(request,'word.html',context)