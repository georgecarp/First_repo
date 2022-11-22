# # ABSTRACTION
# # Clasa abstractă FormaGeometrica
# # Conține un field PI=3.14
# # Conține o metodă abstractă aria (opțional)
# # Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# # probabil am colturi’
#
# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
#
# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)
#
# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)
#
class FormaGeometrica():
    PI = 3.14

    def arie(self):
        raise NotImplementedError
    def descrie(self):
        print('Cel mai probabil am colturi')

class Patrat(FormaGeometrica):
       def __int__(self,latura):
           self.__latura=latura
       def latura(self):
           return self.__latura
       def get_latura(self):
           print((f'Latura are {self.__latura}'))
           return self.__latura
       def set_latura(self):
           print(f'Noua latura este {latura}')
           self.__latura = latura_dorita
       def latura(self):
           print(f'Am sters latura')
           self.__latura = None
           self.__latura=latura
       def __init__(self,latura):
           self.latura=latura
       def arie(self):
            return self.latura* self.latura



Patrat1 = Patrat(4)
print(Patrat1.arie())
print(Patrat1.descrie())
Patrat2 = Patrat1
Patrat2.latura = 8
print(Patrat2.arie())
del Patrat2.latura

class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self.raza=raza
    def raza(self):
        return self.__raza
    def raza(self):
        print(f'Raza este {raza}')
        return self.__raza
    def raza(self,raza):
        print(f'Noua raza este {raza}')
        self.__raza = raza
    def raza(self):
        print(f'Am sters raza')
        self.__raza = None
    def arie(self):
        return self.raza * self.raza * self.PI

Cerc1 = Cerc(10)
print(Cerc1.arie())
Cerc2 = Cerc1
Cerc2.raza = 14
print(Cerc2.arie())
del Cerc2.raza



# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui



class square:
    def __init__(self,lenght):
        self.lenght = lenght
    def perimeter(self):
        return 4 * (self.lenght)
    def area(self):
        return self.lenght * self.lenght
    def descrie(self):
        return('Eu nu am colturi')
class circle:
    def __init__(self,radius):
        self.radius = radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
    def area(self):
        return 3.14 * self.radius * self.radius

square1 = square(10)
print(square1.perimeter())
print(square1.area())
print(square1.descrie())
circle1 = circle(4)
print(circle1.perimeter())
print(circle1.area())