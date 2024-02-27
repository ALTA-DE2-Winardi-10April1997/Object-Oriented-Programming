# tulis solusi code disini
class HargaPengiriman:
    def __init__(self,panjang,lebar,tinggi,berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_harga(self):
        volume = self.panjang*self.lebar*self.tinggi
        berat_kg = round(self.berat)
        harga_standar = 5000
        if volume > 50:
            tarif_per_50cm3 = 5000 
            volume_tambahan = max(volume - 50, 0)
            jumlah_kali_50cm3 = (volume_tambahan + 49) //50 
            harga_volume = harga_standar + (jumlah_kali_50cm3 * tarif_per_50cm3)
        else:
            harga_volume = harga_standar

        harga_berat = berat_kg * harga_standar
        harga_total = max(harga_volume, harga_berat)
        return harga_total
    
panjang = float(input("Panjang (cm): "))
lebar = float(input("Lebar (cm): "))
tinggi = float(input("Tinggi (cm): "))
berat = float(input("Berat (kg): "))

harga_pengiriman = HargaPengiriman(panjang, lebar, tinggi, berat)

harga_total = harga_pengiriman.hitung_harga()
print(f"Harga Pengiriman: Rp {harga_total}")