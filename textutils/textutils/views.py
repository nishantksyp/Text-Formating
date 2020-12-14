from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyse(request):
    djtext=request.POST.get('text','default')
    removefunc = request.POST.get('removefunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charactercount = request.POST.get('charactercount', 'off')
    print(removefunc)

    #analyzed=djtext
    if removefunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose':'removed punctuation', 'analyzed_text':analyzed}
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()

        params={'purpose':'capitalize', 'analyzed_text':analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char

        params={'purpose':'Removed new line', 'analyzed_text':analyzed}
        djtext = analyzed

    if (charactercount == "on"):
        analyzed = len(djtext)

        params={'purpose':'Number Of Character', 'analyzed_text':analyzed}

    if(removefunc!="on" and fullcaps!="on" and newlineremover!="on" and charactercount!="onn" ):
        return HttpResponse("Please select any operation:------------! TRY AGAIN......")


    return render(request, 'analyse.html', params)