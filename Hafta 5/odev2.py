
en_basarili_sinif = str()
en_yuksek_not = 0

def ortalama_al():
	global en_yuksek_not
	global en_basarili_sinif
	toplam = 0
	sonuc = 0
	sube_adi = input("Şube Adını Girin: ").upper()
	ogrenci_sayisi = int(input("Öğrenci Sayısını Girin: "))

	for ogrenci_notu in range(ogrenci_sayisi):
		o_not = int(input(f"{ogrenci_notu+1}. örencinin notunu girin: "))
		if o_not < 0:
			o_not = 0
		elif o_not > 100:
			o_not = 100
		toplam += o_not
	sonuc = toplam/ogrenci_sayisi
	if en_yuksek_not < sonuc:
		en_yuksek_not = sonuc
		en_basarili_sinif = sube_adi


for i in range(4):
	ortalama_al()

print(f"En başarılı sınıf: {en_basarili_sinif}. Sınıf ortalaması: {en_yuksek_not}")