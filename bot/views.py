from datetime import datetime
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os,pathlib
from django.core.files.storage import FileSystemStorage
from pypdf import PdfReader
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

#valitun tiedoston sisällön luku
def loadData(request):
     cb=returnCB()
     #valittu tiedosto
     file=request.FILES['loadfile']
     filestr=str(file)
     file_extension = pathlib.Path(filestr).suffix
     if file_extension==".txt":
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
     if file_extension==".pdf":
         readPdfFile(file)
         
    
     return render(request,'index.html')

def readPdfFile(file):
    reader = PdfReader(file)
    totalPages=len(reader.pages)
    print(totalPages)
    #i silmukkamuuttujaa kasvatetaan, kunnes se on yhtä suuri kuin totalpages eli
    #pdf tiedoston sivujen kokonaismäärä
    for i in range(0,totalPages):
        page = reader.pages[i]
        text = page.extract_text()
    txtToList=text.split()
    cb=returnCB()
    trainer = ListTrainer(cb)
    trainer.train(txtToList)



def discuss(request):
     cb=returnCB()
     talk=request.POST['talk']
     resp = cb.get_response(talk)
     context={'resp':resp}
     return render(request,'index.html',context)
    