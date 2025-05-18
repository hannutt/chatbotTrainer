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
    cb=ChatBot('Norman',storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3')
    return cb

#tiedosto tuodaan frontista javascript input filen avulla ja talletetaan python funktion
#avulla työkansioon.
def uploadFile(request):
    file=request.FILES['uploadFile']
    fs = FileSystemStorage()
    filename = fs.save(file.name,file)
    
    return render(request,'index.html')

#välittää käyttäjän syötteet botille harjoitusmateriaaliksi.
def trainBot(request):
    cb=returnCB()
    data=request.POST['data']
    #luodaan splitillä lista , merkillä erotetaan merkit omiksi alkioiksi
    datalist=data.split(",")
    trainer=ListTrainer(cb)
    trainer.train(datalist)
    
    return render(request,'index.html')


def loadData(request):
     cb=returnCB()
     #valittu tiedosto
     file=request.FILES['loadfile']
     fs = FileSystemStorage()
     #valitun tiedoston tallennus juurikansioon
     filename = fs.save(file.name,file)
     datalist=[]
     #tiedoston avaus ja läpikäynti silmukalla
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
    