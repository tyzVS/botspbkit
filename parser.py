import requests
import urllib.request
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.spbkit.edu.ru/index.php?option=com_timetable&Itemid=82'
url2 = 'http://service.spbcoit.ru:3080/replacements/view.html'

response = requests.get(url)
response2 = requests.get(url2)
soap = BeautifulSoup(response.text, "html.parser")
url = 'http://www.spbkit.edu.ru/index.php?option=com_timetable&Itemid=82'
response = requests.get(url)
soap = BeautifulSoup(response.text, "html.parser")
rasp1 = soap.find(class_="timetablediv")
gruppi = [0, 0, 0, 0, 0, 121, 122, 123, 124, 125, 126, 127, 21, 22, 211, 212, 213, 214, 215, 216, 11, 12, 301, 302, 303, 304, 305, 306, 1, 2, 491, 492, 493, 494, 495, 496]

def ponedelnik(mygr1: int):
    mygr = 0
    mygr = mygr + mygr1
    nom = gruppi.index(mygr, 4)
    gr1 = "gruppi-" + str(nom)
    rasp = rasp1.find("div", id=gr1)
    global den_nedeli
    den1 = 0
    den2 = 0
    den3 = 10
    para = ""
    nomer = 1
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == "":
            predmet = "⠀⠀"
            para = str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        else:
            para = str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        den1 = den1 + 1
    para = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + str(den_nedeli) + "\n" + str(para)
    den1 = den1
    return para
def vtornik(mygr1):
    mygr = 0
    mygr = mygr + mygr1
    nom = gruppi.index(mygr, 4)
    gr1 = "gruppi-" + str(nom)
    rasp = rasp1.find("div", id=gr1)
    den1 = 10
    den2 = 1
    den3 = 20
    para = ""
    nomer = 1
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == "":
            predmet = "⠀⠀"
            para = str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        else:
            para = str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        den1 = den1 + 1
    para = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + str(den_nedeli) + "\n" + "\n" + str(para)
    den1 = den1
    return para
def sreda(mygr1):
    mygr = 0
    mygr = mygr + mygr1
    nom = gruppi.index(mygr, 4)
    gr1 = "gruppi-" + str(nom)
    rasp = rasp1.find("div", id=gr1)
    den1 = 20
    den2 = 2
    den3 = 30
    para = ""
    nomer = 1
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == "":
            predmet = "⠀⠀"
            para = str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        else:
            para = str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        den1 = den1 + 1
    para = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + str(den_nedeli) + "\n" + "\n" + str(para)
    den1 = den1
    return para
def chetverg(mygr1):
    mygr = 0
    mygr = mygr + mygr1
    nom = gruppi.index(mygr, 4)
    gr1 = "gruppi-" + str(nom)
    rasp = rasp1.find("div", id=gr1)
    den1 = 30
    den2 = 3
    den3 = 40
    para = ""
    nomer = 1
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == "":
            predmet = "⠀⠀"
            para = str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        else:
            para = str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        den1 = den1 + 1
    para = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + str(den_nedeli) + "\n" + str(para)
    den1 = den1
    return para
def pyatnica(mygr1):
    mygr = 0
    mygr = mygr + mygr1
    nom = gruppi.index(mygr, 4)
    gr1 = "gruppi-" + str(nom)
    rasp = rasp1.find("div", id=gr1)
    den1 = 40
    den2 = 4
    den3 = 50
    para = ""
    nomer = 1
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == "":
            predmet = "⠀⠀"
            para = str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        else:
            para = str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        den1 = den1 + 1
    para = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + str(den_nedeli) + "\n" + str(para)
    den1 = den1
    return para
def sybbota(mygr1):
    mygr = 0
    mygr = mygr + mygr1
    nom = gruppi.index(mygr, 4)
    gr1 = "gruppi-" + str(nom)
    rasp = rasp1.find("div", id=gr1)
    den1 = 50
    den2 = 5
    den3 = 60
    para = ""
    nomer = 1
    vse_pari = rasp.find_all('b')
    while den1 != den3:
        predmet = vse_pari[den1].text.strip().replace("\n", "")
        dni = rasp.find_all("span")
        den_nedeli = dni[den2].text
        if predmet == "":
            predmet = "⠀⠀"
            para = str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        else:
            para = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + str(para) + "\n" + str(nomer) + ".⠀⠀" + str(predmet)
            nomer = nomer + 1
        den1 = den1 + 1
    para = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + str(den_nedeli) + "\n" + str(para)
    den1 = den1
    return para

def zaminka(mygr1):
    mygr = 0
    mygr = mygr + mygr1
    nom = gruppi.index(mygr, 4)
    page = 'http://service.spbcoit.ru:3080/replacements/api/fetch-rep'
    html = urlopen(page).read()
    soup = BeautifulSoup(html, "html.parser")
    group = soup.find_all("tr")
    data = soup.find_all(class_="content")
    all = soup.find("table")
    al = all.find_all('tr')
    zampr = data[1].text.strip()
    newpr = data[3].text.strip()
    i = 0
    daaaa = 0
    otvet2 = ""
    otvet = ""
    zameni = ""
    while True:
        try:
            i = i + 1
            if i > len(group):
                zameni = "Замен нет"
                break
            if str(mygr) == group[i].text.strip():
                gru = group[i].text.strip()
                i = i + 2
                grp = group[i].find_all('td')
                num1 = grp[0].text.strip()
                naz1 = grp[1].text.strip()
                if naz1 == "":
                    naz1 = "Поставили пару"
                deist1 = grp[2].text.strip()
                newpar1 = grp[3].text.strip()
                if newpar1 == "":
                    newpar1 == "Нет пары"
                i = i + 2
                daaaa:int = 1
                otvet = al[0].text.strip() + "\n\n" + str(zampr) #+ str(newpr)
                num1_1 = int(num1) + 1
                pervii = num1 + "-" + str(num1_1) + "  " + naz1 + "\n\n" + "Заменяющий преподаватель\n" + str(deist1) + "\n\n" + str(newpr) + "\n" + str(newpar1)
                otvet2 = pervii + "\n" + "--------------------------------------" + "\n"
                grp1 = group[i].find_all('td')
                zameni = otvet + "\n" + otvet2
                if len(grp1) > 3:
                    num2 = grp1[0].text.strip()
                    naz2 = grp1[1].text.strip()
                    if naz2 == "":
                        naz2 = "Поставили пару"
                    deist2 = grp1[2].text.strip()
                    newpar2 = grp1[3].text.strip()
                    if newpar2 == "":
                        newpar2 == "Нет пары"
                    num2_2 = int(num2) + 1
                    vtoroi = num2 + "-" + str(num2_2) + "  " + naz2 + "\n\n" + "Заменяющий преподаватель\n" + str(deist2) + "\n\n" + str(newpr) + "\n" + str(newpar2)
                    otvet2 = otvet2 + vtoroi + "\n" + "--------------------------------------" + "\n"
                    zameni = otvet + "\n" + otvet2
                else:
                    break
                i = i + 2
                grp2 = group[i].find_all('td')
                if len(grp2) > 1:
                    num3 = grp2[0].text.strip()
                    naz3 = grp2[1].text.strip()
                    if naz3 == "":
                        naz3 = "Поставили пару"
                    deist3 = grp2[2].text.strip()
                    newpar3 = grp2[3].text.strip()
                    if newpar3 == "":
                        newpar3 == "Нет пары"
                    num3_3 = int(num2) + 1
                    tretii = num3 + "-" + str(num3_3) + "  " + naz3 + "\n\n" + "Заменяющий преподаватель\n" + str(deist3) + "\n\n" + str(newpr) + "\n" + str(newpar3)
                    otvet2 = otvet2 + tretii + "\n" + "--------------------------------------" + "\n"
                    zameni = otvet + "\n" + otvet2
                    break
                else:
                    zameni = otvet + "\n" + otvet2
                    break
                break
        except:
            if zameni == '':
                zameni = "Замен нет"
            else:
                break
    return zameni

def zvonki():
    zvonok = """1. 09:00 - 09:45 
2. 09:50 - 10:35
3. 11:05 - 11:50 
4. 11:55 - 12:40 
5. 13:10 - 13:55 
6. 14:00 - 14:45 
7. 14:55 - 15:40
8. 15:45 - 16:30
9. 16:35 - 17:20
10. 17:25 - 18:10"""
    return zvonok

