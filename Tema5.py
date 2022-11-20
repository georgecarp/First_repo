# 1.Funcție care să calculeze și să returneze suma a două numere

a = int(input('a = '))
b = int(input('b = '))

def rezultat(a,b):
    print(a+b)
rezultat(a,b)


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar


def numar(valoare =int(input('Numarul este:'))):
    if valoare %2==0:
        return True
    else:
        return False
rezultat = numar()
print(rezultat)


# 3. Funcție care returnează numărul total de caractere din numele tău complet.
 # (nume, prenume, nume_mijlociu)



def numar_caractere(nume, prenume, nume_mijlociu):
    caractere = len(nume + prenume + nume_mijlociu)
    return caractere

caractere = numar_caractere('Carp','George','Geo')
print(caractere)


# 4. Funcție care returnează aria dreptunghiului

def aria_dreptungi(lungime,latime):
    arie = lungime * latime
    return arie
arie = aria_dreptungi(8,4)
print(arie)


# 5. Funcție care returnează aria cercului

def aria_cercului(r):
    aria2 = 3.14 * r ** 2
    return aria2
aria2 = aria_cercului(10)
print(aria2)

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.

def diplay_list():
    phrase = 'Lucky dog'
    if ('L' in phrase):
        return True
    else:
        return False
rezultat = diplay_list()
print(rezultat)

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

def lista_numere(numere_Positive):
    lista_noua = []
    for numar in numere_Positive:
        if numar > 0:
            lista_noua.append(numar)
    return lista_noua
numere_Positive = [-2,-1,0,1,2]
result = lista_numere(numere_Positive)
print(result)



# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.


def lista_numere(x,y):

    if x >y:
        print('Primul numar este mai mare decat al 2 lea numar')
    elif x < y:
        print(('Al doilea numar este mai mare decat primul numar'))
    else:
        print('Numerele sunt egale')


x = int(input('Introduceti un numar: '))
y = int(input('Introduceti un numar: '))


lista_numere(x,y)



# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False


x = 9
set_numar = {1,3,5,7,9}

def numar_set(x, set_numar):
    if x in set_numar:
        print('nu am adaugat numărul în set. Acesta există deja')
        return False
    else:
        set_numar.add(x)
        print('am adaugat numărul nou în set')
        return True

result = numar_set(x,set_numar)
print(set_numar)




