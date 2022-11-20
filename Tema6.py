# # 1.Clasa Cerc
# # Atribute: raza, culoare
# # Constructor pentru ambele atribute
# # Metode:
# # ● descrie_cerc() - va PRINTA culoarea și raza
# # ● aria() - va RETURNA aria
# # ● diametru()
# # ● circumferinta()
#
#
import math


class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f'raza={self.raza} culoare={self.culoare}')

    def area(self):
        return math.pi * self.raza * self.raza

    def diametru(self):
        return 2 * self.raza

    def circumeferinta(self):
        return 2 * math.pi * self.raza


cerc1 = Cerc(8, 'Verde')
print(cerc1.descriere_cerc())
print(cerc1.area())
print(cerc1.diametru())
print(cerc1.circumeferinta())


# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
#
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().


class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        return (self.lungime, self.latime, self.culoare)

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return (2 * self.lungime) + (2 * self.latime)


Dreptunghi1 = Dreptunghi(7, 3, 'Negru')
print(Dreptunghi1.descrie())
print(Dreptunghi1.aria())
print(Dreptunghi1.perimetru())


# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat:
    nume: None
    prenume: None
    salariu: None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        return (self.nume, self.prenume, self.salariu)

    def nume_complet(self):
        return (self.nume + " " + self.prenume)

    def salariu_lunar(self):
        return (self.salariu)

    def salariu_anual(self):
        return (self.salariu * 12)

# s = 100.000
# p = 10
# fin = 110.000
    def marire_salariu(self, procent):
        self.salariu = self.salariu + (self.salariu / 100 * procent)
        print(f'Salariu marit = {self.salariu}')


Angajat1 = Angajat('Carp', 'George', 7000)
print(Angajat1.descriere())
print(Angajat1.nume_complet())
print(Angajat1.salariu_lunar())
print(Angajat1.salariu_anual())
print(Angajat1.marire_salariu(10))


# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)


class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'{self.titular_cont} are in {self.iban} suma de {self.sold}')
    def debitare_cont(self, suma):
        return self.sold - suma
    def creditare_cont(self, suma):
        return self.sold + suma
Cont1 = Cont('RO14BTRLEUR000000','Popescu Vasile',5000)
print(Cont1.afisare_sold())
print(Cont1.debitare_cont(1000))
print(Cont1.creditare_cont(5000))



