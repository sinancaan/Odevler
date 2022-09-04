sayi = int(input("Lütfen bir sayı giriniz: "))
baslangic = 1
kareler_toplami = 0
kupler_toplami = 0

while baslangic <= sayi:
	if (baslangic % 2 == 0):
		kupler_toplami += baslangic ** 3
		baslangic += 1
	else:
		kareler_toplami += baslangic ** 2
		baslangic += 1

print(f"Girdiğiniz değere kadar olan tek sayıların kareler toplamı: {kareler_toplami}")
print(f"Girdiğiniz değere kadar olan çif sayıların küpler toplamı: {kupler_toplami}")