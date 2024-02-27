# tulis solusi code disini
class BangunRuang:
    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, rusuk):
        self.rusuk = rusuk

    def volume(self):
        return self.rusuk**3
    
class Balok(BangunRuang):
    def __init__(self,panjang,lebar,tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        return self.panjang*self.lebar*self.tinggi
    
class Tabung(BangunRuang):
    def __init__(self,radius,tinggi):
        self.radius = radius
        self.tinggi = tinggi

    def volume(self):
        return 22/7*(self.radius**2)*self.tinggi
    

tabung = Tabung(7,10)
print(tabung.volume())