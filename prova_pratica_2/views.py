from django.shortcuts import render

def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    context={
             'materie':materie,
        }
    return render(request,"views_a.html",context)
def view_b(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    context={
        'voti':voti
     }
    return render(request,"views_b.html",context)
def view_c(request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    medie = {}
    cont=0
    for key,value in voti.items():
        media=0     
        cont+=1
        print(cont)
        for voto in value:
            media+=voto[1]
        media = media/len(value)
        medie[key]=media
    context={
            'medie':medie,
        }
    return render(request,"views_c.html",context)
def index_prova_2(request):
    return render(request,"index_prova_2.html")

