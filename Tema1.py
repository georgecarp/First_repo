# 1.In cadrul unui comentariu explica cu cuvintele tale ce este o variabila.
#
# O variabila reprezinta o parte din memorie unde tinem informatii.Sau cu alte cuvinte o cutiuta cu valori.
#
# 2.Declara si initializeaza cate o variabila din fiecare din urmatoarele tipuri de variabila:

# String:
marca='Huawei'
model='P30'

print(f'Am cumparat un telefon {marca}')
print(f'Este modelul {model}')


# Intenger

marca='Huawei'
model='P30'
An_fabricatie=2019

print(f'Am cumparat un telefon {marca}' )
print(f'Este modelul {model}')
print(f'Anul fabricatiei {An_fabricatie}')

# Float

marca='Huawei'
model='P30'
An_fabricatie=2019
Greutate=150.55

print(f'Am cumparat un telefon {marca}' )
print(f'Este modelul {model}')
print(f'Anul fabricatiei {An_fabricatie}')
print(f'Are greutatea de {Greutate}')

# Bolean

marca='Huawei'
model='P30'
An_fabricatie=2019
Greutate=150.55
Baterie_lithium='True'

print(f'Am cumparat un telefon {marca}' )
print(f'Este modelul {model}')
print(f'Anul fabricatiei {An_fabricatie}')
print(f'Are greutatea de {Greutate}')
print(f'Contine baterie hazmat {Baterie_lithium}')

# 3.Utilizeaza functia type pentru a verifica daca au tipul de date asteptat.

marca='Huawei'
model='P30'
An_fabricatie=2019
Greutate=150.55
Baterie_lithium=True


print(type(marca))
print(type(Greutate))
print(type(An_fabricatie))
print(type(Baterie_lithium))

# 4.Rotunjeste ‘float-ul’folosind functia round() si salveaza aceasta modificare in acceasi variabila (suprascriere) si verifica tipul acesteia.
marca='Huawei'
model='P30'
An_fabricatie=2019
Greutate=150.55
Baterie_lithium=True

Greutate = round(Greutate)
print(Greutate)
print(type(Greutate))

# 5.Foloseste print() si printeaza in console 4 propozitii folosind cele 4 variabile.

prenume='george'
oras='iasi'
marca='Huawei'
model='P30'
magazin='Flanco'
An_fabricatie=2019
Greutate= 150.55
Baterie_lithium=True


print(f'Numele meu este {prenume}')
print(f'este un telefon usor avand greutatea de {Greutate}')
print(f'produsul are o baterie hazmat {Baterie_lithium}')
print(f'Anul de fabricatie este : {An_fabricatie}')


# 6.Citeste de la tastatura:
# -numele
# -prenumele
# Afiseaza: ‘Numele complet are x caractere
nume=input('Numele=')
prenume=input('Prenumele=')
print(f'Numele complet are {len(nume + prenume)} caractere')


# 7.Citeste de la tastatura
# -lungimea
# -latimea
# Afiseaza:’Aria dreptunghiului este x’.

lungime=input('Lungime=')
latime=input('Latime')

lungime_int = int(lungime)
latime_int = int(latime)

print(f' Aria dreptunghiului este { lungime_int * latime_int}')


# 8.Avand stringul: ‘Coral is the stupidest animal or the smartest rock’:
# -afiseaza de cate ori aparate cuvantul ‘the’.



prop='Coral is either the stupidest animal or the smartest rock'
x=prop.count(" the ")

# 9.Accelasi string.
# Afiseaza de cate ori apare cuvantul the;
# Printeaza rezultatul

prop='Coral is either the stupidest animal or the smartest rock'
x=prop.count(" the ")
print(x)


# 10.Folositi un assert ca sa verificati dace acest string contine doar numere

prop='Coral is either the stupidest animal or the smartest rock'

assert prop == str(prop)
print('contine litere')
assert prop == int(prop)
print('contine numere')



