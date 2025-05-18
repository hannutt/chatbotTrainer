from datetime import datetime
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
import os
from django.core.files.storage import FileSystemStorage
# Create your views here.
def startingPage(request):
    return render(request,"index.html")


def returnCB():
    cb=ChatBot('Norman')
    return cb

#tiedosto tuodaan frontista javascript input filen avulla ja talletetaan python funktion
#avulla työkansioon.
def uploadFile(request):
    file=request.FILES['uploadFile']
    fs = FileSystemStorage()
    filename = fs.save(file.name,file)
    
    return render(request,'index.html')

#tallennetaan textarea elementtiin kirjoitettu sisältö tekstitiedostoon.
def trainBot(request):
    now = datetime.now()
    lf = now.strftime("%H%M%S")
    print(os.getcwd())
    data=request.POST['data']
    file=open(f"{os.getcwd()}\\data{lf}.txt","w")
    file.write(data)
    return render(request,'index.html')


def loadData(request):
     cb=returnCB()
     file=request.FILES['loadfile']
     fs = FileSystemStorage()
     filename = fs.path(file.name)
     print(filename)
     datalist=[]
     f=open(filename,'r')
     for line in f:
         datalist.append(line)
     trainer = ListTrainer(cb)
     trainer.train(datalist)
     
    
     return render(request,'index.html')


def discuss(request):
     cb=returnCB()
     talk=request.POST['talk']
     resp = cb.get_response(talk)
     context={'resp':resp}
     return render(request,'index.html',context)
    