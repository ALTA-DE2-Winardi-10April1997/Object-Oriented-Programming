# tulis solusi code disini
class BangunDatar:
    def hitung_luas(self):
        pass
    def hitung_keliling(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi**2
    
    def hitung_keliling(self):
        return self.sisi*4
    
class SegiTiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5*self.alas*self.tinggi
    def hitung_keliling(self):
        sisi_miring = (self.alas**2 + self.tinggi**2)**0.5
        return self.alas+self.tinggi+sisi_miring
    
class PersegiPanjang(BangunDatar):
    def __init__(self,lebar,panjang):
        self.lebar = lebar
        self.panjang = panjang

    def hitung_luas(self):
        return self.panjang*self.lebar
    
    def hitung_keliling(self):
        return 2*(self.panjang+self.lebar)
    