# 1.Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else.
#
# Folosind combinatia if else putem stabili comenzi care sa fie executate cand conditia instructiunii if este false.
# If este conditia
# -codul v-a fi executat daca este adevarata conditia
# -else codul v-a fi executat daca conditia este falsa

# 2.Verifica si afiseaza daca x este numar natural sau nu.

x = int(input('x = '))
if x >= 0:
 print(f'{x} este numar natural')
else:
 print(f'{x} nu este numar natural')

# 3.Verifica si afiseaza daca x este numar pozitiv,negative sau neutru.

x = 2022

if x == 0:
    print('Numarul este neutru')
elif x < 0:
    print ('Numarul este negativ')
elif x > 0:
    print ('Numarul este pozitiv')
else:
    print ('Numarul este invalid')


# 4.Verifica si afiseaza daca x este intre – 2 si 13.
# x = 8 # daca este intre - 2 si 13

if x < -2:
    print('Numarul nu este intre -2 si 13')
elif x == -2:
    print ('Numarul nu este intre -2 si 13')
elif x > -2:
    print('Numarul este intre - 2 si - 13')
else:
    print ('Numarul este invalid')


# 5.Verifica daca diferenta dintre x si y este mai mica decat 5
x = 10
y = 7
z = x - y
print(z)

if z > 5:
    print('Afirmativ')
else:
    print('Negative')


# 6.Verifica daca x NU este intre 5 si 27 – a se folosi ‘not’.
x = 4

if x < 25 and not x >= 5:
    print ('Numarul nu se regaseste intre 5 si 25')
else:
    print ('Numarul se regaseste intre 5 si 25')

# 7. x si y (int)
# Verifica si afiseaza care din ele este mai mare.

x = int(input("Alege un numar: "))
y = int(input("Alege un numar : "))

if x > y:
    print('X este mai mare')
elif  y > x:
    print("y este mai mare")
else:
    print("numerele sunt invalide")


# 8. x,y,z -laturile unui triunghi
# Afiseaza daca triunghiul este isoscel,echilateral sau oarecare.
# isoscel 2 laturi egale una diferita
# echilateral toate laturile sunt egale
# oarecare laturi diferite

print("Introduceti lungimile laturilor triunghiului")

x = int(input("Latura unghiului este de: "))
y = int(input("Latura unghiului este de: "))
z = int(input("Latura unghiului este de :"))

if x == y == z:
    print("triunghiul este echilateral")
elif x == y != z:
    print("triunghiul este isoscel")
elif x == z != y:
    print("triunghiul este isoscel")
elif y == z != x:
    print("triunghiul este isoscel")
else:
    print("triunghiul este oarecare")


# 9.Citeste o litera de la tastatura.Verifica daca este vocala sau nu.
# Vocala = (a,e,I,o,u)

# *special mention am nevoie de google…eu initial am incercat cu or in loc de in.

x = str(input("Introduceti o litera: "))

if str(x) in ("a", "e", "i", "o", "u"):
    print("Litera este o vocala")
else:
    print("Litera este o consoana")


# 10.Transformă și printează notele din sistem românesc în > Peste 9 => A Peste 8 => B Peste 7 => C Peste 6 => D Peste 4 => E 4 sau sub => F


nota = int(input("Introduceti nota: "))

if nota > 9:
    print('A')
elif nota > 8:
    print ('B')
elif nota > 7:
    print('C')
elif nota > 6:
    print ('D')
elif nota > 4:
   print ('E')
else:
    print('F')

# Extra:
#
# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

number = input("Introduceti un numar format din patru cifre ")
if (len(number)) == 4:
    print ("x are 4 cifre")
else:
    print("Eroare")
