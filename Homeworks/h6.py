""" Homework 6 - needs to be presented before exam day
O fabrica de masini are nevoie de un obiect iterabil care sa contina seriile si loturile masinilor produse in ziua respectiva.
Seriile si loturile sunt numere intregi de tip int
Un lot este alcatuit din 20 de masini jumatate din lot sunt cu volan pe dreapta si jumatate cu volan pe stanga
Numerotarea loturilor incepe de la prima masina produsa cu seria 1 si lot 1
Ziua de lucru stocata in obiectul contruit de voi poate incepe cu orice numar de serie si numarul de bucati produse in acea zi poate avea orice valoare
Obiectul iterat va returna numerele loturilor din care fac parte masinile din acea zi, numerotarea lor a inceput de la prima masina produsa cu seria 0 si lot 0
Masinile cu serii pare sunt cu volan pe dreapta iar cele cu serii impare cu volan pe stanga
1)Definire: 40p
  - Creati o clasa pentru un obiect iterabil
   a) constructorul primeste doua argumente de tip int, seria de inceput si numarul de bucati. ex: (101, 41) 10p
   b) obiectul are doua metode: prima returneaza o lista cu seriile cu volan pe dreapta si a doua o lista cu seriile cu volan pe stanga 15p
   c) iterator-ul returnat de object va comtine loturile din care fac parte seriile din obiectul curent  15p
2) Executie: 40p
- Creati o instanta a clasei de mai sus dand ca argumente: serie_inceput 314, bucati 90. 10p
- Iterati obiectul creat si salvati fiecare valoare din iteratie in acelas fisier pe linie noua. 30p
3) Documentatie: 20p
   a) adaugati type hints 5p
   a) documentati modulul 5p
   b) documentati clasele 5p
   c) documentati metodele 5p
"""
class FabricaItter():
    """class doc"""
    def __init__(self,data:int):
        """method doc"""
        self.data=data
    def __iter__(self):
        """method doc"""
        return self
    def __next__(self):
        """method doc"""
        if not self.data:
            raise StopIteration
        return self.data.pop(0)

class Fabrica():
    """class doc"""
    def __init__(self, serie_inceput:int,nr_buc:int):
        """method doc"""
        self.serie_inceput=serie_inceput
        self.nr_buc=nr_buc
        self.volan_dreapta = []
        self.volan_stanga = []
        for i in range(self.serie_inceput,self.serie_inceput+self.nr_buc):
            if i%2==0:
                self.volan_dreapta.append(i)
            else:
                self.volan_stanga.append(i)
    def __iter__(self):
        """method doc"""
        result=[]
        for i in range(self.serie_inceput,self.serie_inceput+self.nr_buc):
            if i//20 not in result:
                result.append(i//20)
        return FabricaItter(result)
    def volan_dr(self):
        """method doc"""
        return self.volan_dreapta
    def volan_st(self):
        """method doc"""
        return self.volan_stanga


ziua1=Fabrica(314,90)

with open("../Probl_test/fisout.txt", "w") as fis:
    for x in ziua1:
        fis.write(str(x)+" ")






