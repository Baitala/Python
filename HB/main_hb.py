import happy_birthday as hb
from datetime import date

debug = True
if debug:
    Yaryna_BD = date.today()
    Keanus_BD = date.today()
else:
    Yaryna_BD = date(1989, 9, 14)
    Keanus_BD = date(1964, 9, 2)

Yaryna = hb.Person_to_congratulate("Ярина","Ярино",Yaryna_BD,"uk")
Yaryna.Happy_Birthday("Женя",10)

Keanu_Reeves = hb.Person_to_congratulate("Keanu","Keanu",Keanus_BD,"en")
Keanu_Reeves.Happy_Birthday("Eugene",100)

print(Keanu_Reeves)

print(Yaryna)

#Congratulating Keanu and Yaryna
#print(Keanu_Reeves + Yaryna)

#Raises AttributeError
#Yaryna.a = 2