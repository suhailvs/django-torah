from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

import json

from .models import Word

def get_line(lang,c):
    data = json.loads(open('torah/json/%s/%s.json'%(lang,c['title'])).read())
    return data['text'][c['chapter']-1][c['line']-1]

def showline(request, title='genesis', chapter=1, line=1):
    if request.method=='POST':
        return redirect('/%s/%s/%s/'%(request.POST['title'],request.POST['chapter'],request.POST['line']))

    context = {'current': {'title':title, 'chapter':chapter, 'line':line}}

    for lang in ['paleo','english','hebrew']:
        context[lang] = get_line(lang,context['current'])

    return render(request,'line.html',context)

def showword(request):
    w = request.GET.get('word','')
    trans = '----'
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


class AjaxView(View):

    def get(self, request, *args, **kwargs):
        w = request.GET.get('word','')
        item = Word.objects.get(name = w)
        print('fetched: ', item.desc)
        print(item.lines.all())
        return HttpResponse(json.dumps({
            'id':item.id,
            'description':item.desc,
            'lines':[{'id':l.id,'t':l.title,'c':l.chapter,'l':l.line} for l in item.lines.all()]
        }))

    def post(self, request, *args, **kwargs):
        w = Word.objects.get(id = request.POST['id'])
        w.desc = request.POST['description']
        w.save()
        print('saved: ', w.desc)
        return HttpResponse('saved')