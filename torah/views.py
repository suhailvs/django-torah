from django.shortcuts import render, redirect
import json

def home(request):
	return render(request,'home.html')

def showline(request, title='genesis', chapter=1, line=1):
	if request.method=='POST':
		return redirect('/%s/%s/%s/'%(request.POST['title'],request.POST['chapter'],request.POST['line']))
	paleo_data = json.loads(open('torah/json/paleo/%s.json'%title).read())
	english_data = json.loads(open('torah/json/english/%s.json'%title).read())
	context = {
		'page': '%s - %d:%d'%(title,chapter,line),
		'paleo':paleo_data['text'][chapter-1][line-1],
		'english': english_data['text'][chapter-1][line-1],
		'p':'abgdefzhjiklmnxopsqrct'
	}
	return render(request,'line.html',context)