#myself
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Hello")
    param={"name":"YEN","place":"Wari, Dhaka"}
    return render(request,"index.html",param)
def about(request):
    return HttpResponse('''<h1> This is about page </h1> <a href ="https://www.bracu.ac.bd/">YEN</a> ''')

def removefirst(req):
    return HttpResponse('''<h1>RemoveFirst</h1> <a href="/about"> Back </a>''')
def analyze(req):
    djtext=req.POST.get('text','default')
    removepu=req.POST.get('removepun','off')
    uppercase=req.POST.get("UPPERCASE","off")
    newline=req.POST.get("Newlineremover","off")


    if removepu=="on":
      analyzed = ""
      punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
      for i in djtext:
          if i not in punc:
              analyzed+=i
      params={"purpose": "Remove Punctuations", "analyzed_text":analyzed}
   # return HttpResponse('''<h1>Removepunc</h1> <a href="/"> Back </a>''')
      djtext=analyzed
      #return render(req,"analyze.html",params)

    if uppercase=="on":
        analyzed = ""
        for i in djtext:
            analyzed+=i.upper()
        params={"purpose":"Upper Case","analyzed_text":analyzed}
        djtext=analyzed
       # return render(req,"analyze.html",params)
    if newline=="on":
        analyzed = ""
        for i in djtext:
            if i != "\n" and i !="\r":
               analyzed+=i
        params={"purpose":"New Line Remover","analyzed_text":analyzed}


    if removepu!="on" and uppercase!="on" and newline!="on":
        return HttpResponse("Please select the opeation again")
    return render(req, "analyze.html", params)