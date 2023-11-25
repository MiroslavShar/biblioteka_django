import datetime
import random
import time
from polka.models import Person
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_django(request):
    return HttpResponse("Witaj Django")

def new_task(request):
    return HttpResponse("Jestem Mirek")

def time_actual(request):
    return HttpResponse(datetime.datetime.now())

def surname(request):
    return HttpResponse('jewtuszenko')

def lista_zakupów(request):
    return HttpResponse("""
    <ul>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
    <li>Bread</li>
    <li>Broad</li>
    </ul>""")

def napis(request, ilosc):
    s = ""
    for x in range(ilosc):
        s += "dupa<br>"
    return HttpResponse(s)

def witaj_dyn(request, imie):
    return HttpResponse("Witaj " + imie)

def hello_world(request):
    return HttpResponse("Hello world")

def random_numb(request):
    return HttpResponse(random.randint(1, 100))

def random_max(request, max_number):
    return HttpResponse(random.randint(1, max_number))

def random_min_max(request, min_numb, max_numb):
    return HttpResponse(random.randint(min_numb, max_numb))

def hello_name(request, name):
    return HttpResponse("Witaj " + name)

def kalkulator(request, numb1, znak, numb2):
    znak = znak
    if znak == "*":
        return HttpResponse(numb1 * numb2)
    elif znak == ":":
        return HttpResponse(numb1 / numb2)
    elif znak == "+":
        return HttpResponse(numb1 + numb2)
    elif znak == "-":
        return HttpResponse(numb1 - numb2)
    else:
        return HttpResponse("Coś poszło nie po myśli")

def kalkulator2(request, numb1, znak, numb2):
    znak = znak
    s = ""
    if znak == "*":
        for x in range(numb2 + 1):
            wynik = numb1 * x
            s += f"""
    <ul>
    <li>{numb1} {znak} {x} = {wynik}</li>
    </ul>
    """

        return HttpResponse(s)
    if znak == "/":
        for x in range(numb2 + 1):
            wynik = numb1 / x
            s += f"""
    <ul>
    <li>{numb1} {znak} {x} = {wynik}</li>
    </ul>
    """

        return HttpResponse(s)
    if znak == "+":
        for x in range(numb2 + 1):
            wynik = numb1 + x
            s += f"""
    <ul>
    <li>{numb1} {znak} {x} = {wynik}</li>
    </ul>
    """

        return HttpResponse(s)
    if znak == "-":
        for x in range(numb2 + 1):
            wynik = numb1 - x
            s += f"""
    <ul>
    <li>{numb1} {znak} {x} = {wynik}</li>
    </ul>
    """

        return HttpResponse(s)
    else:
        return HttpResponse("Coś poszło nie po myśli")

def tabela_mnożenia(request, numb1, numb2):
    tab = "<table border = 1>"
    for x in range(1, numb1 + 1):
        tab += "<tr>"
        for y in range(1, numb2 + 1):
            tab += f"<td>{x*y}</td>"
        tab += "</tr>"
    tab += "</table>"
    return HttpResponse(tab)

def dodaj_osobe(request):
    if request.method == 'GET':
        response = render(request,"dodaj_osobe.html")
        return response
    else:
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        p = Person(first_name = imie, last_name = nazwisko)
        p.save()
        return HttpResponse(f'Próbujesz dodać {imie} {nazwisko} do bazy')

def wyswietlanie_osob(request):
    osoby = Person.objects.all()
    return render(request, 'osoby.html', {'persons':osoby})


def osoba(request, id):
    o = Person.objects.get(id=id)
    return render(request, 'o.html', {'osoba':o})
