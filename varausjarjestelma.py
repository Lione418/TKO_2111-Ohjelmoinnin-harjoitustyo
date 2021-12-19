import json
#Tuodaan aikaominaisuudet, jotta ohjelma tietää mikä päivä on
import datetime
tanaan = datetime.date.today()
#Lopussa ylimääräinen maanantai, jotta "huomenna"-toiminnot toimivat sunnuntainakin
vkPv = ("maanantai","tiistai","keskiviikko","torstai","perjantai","lauantai","sunnuntai","maanantai")
viikonpv = tanaan.weekday()
pv = []
for i in vkPv:
    pv.append(i[:2])


#Luetaan tarjolla olevat elokuvat
elokuvat = {}
with open("elokuvat.csv") as tiedosto:
   for rivi in tiedosto:
        tiedot = rivi.strip().split(",")
        elokuvat[tiedot[0]] = [tiedot[1],tiedot[2]]

#Tuodaan salitiedot
with open("pieni_sali.json", 'r') as f:
    pieni_sali = json.load(f)
with open("heureka_sali.json", 'r') as f:
    heureka_sali = json.load(f)
with open("iso_sali.json", 'r') as f:
    iso_sali = json.load(f)

def lisaaElokuva():
    avain = input("Anna elokuvan nimi (tai poistu painamalla P): ")
    if avain == "P":
        return
    arvo1 = input("Anna elokuvan ikäraja: ")
    arvo2 = input("Anna elokuvan kesto (esim. '1h 33min'): ")
    f = open("elokuvat.csv", "a")
    f.write(f"{avain},{arvo1},{arvo2}\n")
    f.close()
    print(f"Lisäsit elokuvan: {avain}, {arvo1}, {arvo2}")
    elokuvat[avain] = [arvo1,arvo2]

def elokuvavalikko():
    print("Ohjelmistossa nyt: ")
    for nimi in elokuvat:
        tiedot = ""
        for i in elokuvat[nimi]:
            tiedot += ", "
            tiedot += i
        print(f"{nimi}{tiedot}")

def tanaanOhjelmistossa():
    print(f"Tänään on {vkPv[viikonpv]}. Päivän näytökset: ")
    with open("pieni_sali.json", 'r') as f:
        pieni_sali = json.load(f)
    print("Pieni sali: ")
    print("klo 12 --- " + pieni_sali[f"{pv[viikonpv]}1e"])
    print("klo 15 --- "+ pieni_sali[f"{pv[viikonpv]}2e"])
    print("klo 18 --- "+ pieni_sali[f"{pv[viikonpv]}3e"])

    with open("heureka_sali.json", 'r') as f:
        heureka_sali = json.load(f)
    print("Heureka-sali: ")
    print("klo 12 --- " + heureka_sali[f"{pv[viikonpv]}1e"])
    print("klo 15 --- "+ heureka_sali[f"{pv[viikonpv]}2e"])
    print("klo 18 --- "+ heureka_sali[f"{pv[viikonpv]}3e"])

    with open("iso_sali.json", 'r') as f:
        iso_sali = json.load(f)
    print("Iso sali: ")
    print("klo 12 --- " + iso_sali[f"{pv[viikonpv]}1e"])
    print("klo 15 --- "+ iso_sali[f"{pv[viikonpv]}2e"])
    print("klo 18 --- "+ iso_sali[f"{pv[viikonpv]}3e"])



def huomennaOhjelmistossa():
    print(f"Huomenna on {vkPv[viikonpv + 1]}. Huomisen näytökset: ")
    with open("pieni_sali.json", 'r') as f:
        pieni_sali = json.load(f)
    print("Pieni sali: ")
    print("klo 12 --- " + pieni_sali[f"{pv[viikonpv+1]}1e"])
    print("klo 15 --- "+ pieni_sali[f"{pv[viikonpv+1]}2e"])
    print("klo 18 --- "+ pieni_sali[f"{pv[viikonpv+1]}3e"])

    with open("heureka_sali.json", 'r') as f:
        heureka_sali = json.load(f)
    print("Heureka-sali: ")
    print("klo 12 --- " + heureka_sali[f"{pv[viikonpv+1]}1e"])
    print("klo 15 --- "+ heureka_sali[f"{pv[viikonpv+1]}2e"])
    print("klo 18 --- "+ heureka_sali[f"{pv[viikonpv+1]}3e"])

    with open("iso_sali.json", 'r') as f:
        iso_sali = json.load(f)
    print("Iso sali: ")
    print("klo 12 --- " + iso_sali[f"{pv[viikonpv]}1e"])
    print("klo 15 --- "+ iso_sali[f"{pv[viikonpv]}2e"])
    print("klo 18 --- "+ iso_sali[f"{pv[viikonpv]}3e"])

def ohjelmisto():
    pass

def varaaPaikka():
    pass

#Game on
print("Tervetuloa!")
jatkuu = True
while jatkuu:
    #Aloitusvalikko
    print("Valitse seuraavista:")
    print("(E) Elokuvat")
    print("(T) Tänään")
    print("(H) Huomenna")
    print("(S) Selaa ohjelmistoa")
    print("(X) Poistu")
    x = input()

    #Elokuvavalikko
    if x == "E":
        elokuvavalikko()

    #Tänään ohjelmistossa
    elif x == "T":
        tanaanOhjelmistossa()

    #Huomenna ohjelmistossa
    elif x == "H":
        huomennaOhjelmistossa()

    #Selaa ohjelmistoa
    elif x == "S":
        ohjelmisto()

    elif x == "X":
        jatkuu = False

    #Ylläpitäjän käyttöliittymä
    elif x == "9876":
        print("Hei ylläpitäjä!")
        admin = True
        while admin:
            print("(1) Lisää elokuva")
            print("(X) Palaa päävalikkoon")
            y = input()

            if y == "1":
                lisaaElokuva()

            elif y == "X":
                admin = False
    
