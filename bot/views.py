from datetime import datetime
from django.shortcuts import redirect, render
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os,pathlib
from django.core.files.storage import FileSystemStorage
from pypdf import PdfReader
from chatbot.cbVars import Variables
# Create your views here.
var=Variables()
def startingPage(request):
    return render(request,"index.html")

#tiedosto tuodaan frontista javascript input filen avulla ja talletetaan python funktion
#avulla työkansioon.
def getAdaptions(request):
    mathCB=request.POST['math']
    if mathCB:
        var.adaptions=True
    else:
        print("no adaptions selected")
    return redirect(startingPage)

def uploadFile(request):
    file=request.FILES['uploadFile']
    fs = FileSystemStorage()
    filename = fs.save(file.name,file)
    
    return render(request,'index.html')

#välittää käyttäjän syötteet botille harjoitusmateriaaliksi.
def trainBot(request):
    data=request.POST['data']
    #luodaan splitillä lista , merkillä erotetaan merkit omiksi alkioiksi
    datalist=data.split(",")
    trainer=ListTrainer(var.CbotNoAdaptions)
    trainer.train(datalist)
    
    return render(request,'index.html')

#valitun tiedoston sisällön luku
def loadData(request):
     #valittu tiedosto
     file=request.FILES['loadfile']
     filestr=str(file)
     file_extension = pathlib.Path(filestr).suffix
     if file_extension==".txt":
         readTxtFile(file)
     if file_extension==".pdf":
         readPdfFile(file)
     return redirect(startingPage)

def readTxtFile(file):
    fs = FileSystemStorage()
     #valitun tiedoston tallennus juurikansioon
    filename = fs.save(file.name,file)
    datalist=[]
     #tiedoston avaus ja läpikäynti silmukalla
    f=open(filename,'r')
    for line in f:
        datalist.append(line)
        trainer = ListTrainer(var.CbotNoAdaptions)
        trainer.train(datalist)


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
    trainer = ListTrainer(var.CbotNoAdaptions)
    trainer.train(txtToList)



def discuss(request):
     if var.adaptions:
         talk=request.POST['talk']
         resp = var.cbMath.get_response(talk)
         context={'resp':resp}
     if var.adaptions==False:
        talk=request.POST['talk']
        resp = var.CbotNoAdaptions.get_response(talk)
        context={'resp':resp}
     return render(request,'index.html',context)
    