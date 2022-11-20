# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do.
# ● Afișeaz-o
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.

thislist = ['do','re','mi','fa','sol','la','si','do']
print(thislist)

thislist = ['do','re','mi','fa','sol','la','si','do']
print(thislist[::-1])


thislist = ['do','re','mi','fa','sol','la','si','do']
thislist.reverse()
print(thislist[::-1])



# 2. De câte ori apare ‘do’?

thislist = ['do','re','mi','fa','sol','la','si','do']
count = thislist.count('do')
print('The count of do is:',count)

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.

lista1 = [3,1,0,2]
lista2 = [6,5,4]
lista1.extend(lista2)
print(lista1)


lista1 +=lista2
print('lista1', lista1)

# 4.
# ● Sortează și afișază lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
# ● Afișaza iar lista.


lista1 = [3,1,0,2]
lista2 = [6,5,4]
lista1 +=lista2
lista1.sort()
print('lista1', lista1)


def myfunc(n):
  return abs(n - 0)

lista1 = [3,1,0,2]
lista2 = [6,5,4]
lista1 +=lista2
lista1.sort(key = myfunc)
print(lista1)


#
# . Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.
lista1 = [3,1,0,2]
lista2 = [6,5,4]
lista1 +=lista2

if lista1:
   print ('Lista nu este goala')
else:
   print('Lista este goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lista1 = [3,1,0,2]
lista2 = [6,5,4]
lista1.extend(lista2)
lista1.clear()


# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.


lista1 = [3,1,0,2]
lista2 = [6,5,4]
lista1.extend(lista2)
lista1.clear()

if lista1:
   print ('Lista nu este goala')
else:
   print('Lista este goala')

# Lista este goala * after run



# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {'Ana' : 8,
         'Gigel' : 10,
         'Dorel' : 5
         }
x = dict1.keys()
print(x)

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

dict1 = {'Ana' : 8,
         'Gigel' : 10,
         'Dorel' : 5
         }
print('Ana a luat nota',dict1['Ana'])
print('Gigel a luat nota',dict1['Gigel'])
print('Dorel a luat nota',dict1 ['Dorel'] )

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare

dict1 = {'Ana' : 8,
         'Gigel' : 10,
         'Dorel' : 5
         }
dict1['Dorel'] = 6
print(dict1)

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi

dict1 = {'Ana' : 8,
         'Gigel' : 10,
         'Dorel' : 5
         }
dict1.pop('Gigel')
dict1['Ionica']=9
print(dict1)

12.
# Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt
# a.
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

# b.
zile_sapt.update(weekend)
print(zile_sapt)


# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

if weekend.issubset(zile_sapt):
    print('weekend is a subset')
else:
    print('weekend is not a subset')

# 14. Afișează diferențele dintre aceste 2 seturi.

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

difference = zile_sapt.symmetric_difference(weekend)
print(difference)

# 15. Afișază intersecția elementelor din aceste 2 seturi.

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

intersection = zile_sapt.intersection(weekend)
print(intersection)
