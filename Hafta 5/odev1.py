sayi = int(input("Faktoriyel almak istediğiniz sayıyı girin: "))

def faktoriyel_al(sayi):
	sonuc = 1
	for i in range(1, sayi+1):
		sonuc *= i
	print(sonuc)

faktoriyel_al(sayi)