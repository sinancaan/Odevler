sayi = 1
tek_toplam = 0
cift_toplam = 0

while sayi <= 1000:
	if (sayi % 2 == 0):
		cift_toplam += sayi
		sayi += 1
	else:
		tek_toplam += sayi
		sayi += 1

print(f"Tek sayıların toplamı: {tek_toplam}")
print(f"Çift sayıların toplamı: {cift_toplam}")