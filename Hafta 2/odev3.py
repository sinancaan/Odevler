kullanici_adi = "sinan"
sifre = "1234"
giris_hakki = 3

while True:
	
	if (giris_hakki > 0):
		ka = input("Lütfen kullanıcı adınızı giriniz: ")
		sif = input("Lütfen şifrenizi giriniz: ")
		if (kullanici_adi == ka) and (sifre == sif):
			print("Giriş Başarılı")
			break
		else:
			print("Hatalı Bilgi Girdiniz.")
			giris_hakki -= 1
			continue
	else:
		print("Giriş hakkınız kalmadı.")
		cevap = input("Hesap açmak ister misiniz: (E/H)")
		if cevap.upper() == "E":
			yeni_ka = input("Lütfen kullanıcı adınızı giriniz: ")
			yeni_sif = input("Lütfen şifrenizi giriniz: ")
			yeni_sif_tekrar = input("Lütfen şifrenizi tekrar giriniz: ")
			if (yeni_sif == yeni_sif_tekrar):
				print("Giriş Yapıldı.")
				break
			else:
				print("Şifreler Eşleşmiyor.")
				continue
		else:
			print("Çıkış Yapılıyor.")
			break