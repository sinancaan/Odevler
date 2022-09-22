dictionary = {"taksit":"installment", "enflasyon":"inflation", "taşınmak":"moving", "olgunluk":"maturity", "çeşit":"variety", "mezar":"tomb",
			"fatura":"recipt", "ama":"but", "sihir":"magic", "faydalı":"beneficial", "şeytan":"devil", "alan":"terretory", "daha iyi":"better"}

while True:
	print("Sözlük Uygulamasına Hoş Geldiniz")
	print("1 - Kelie Arama")
	print("2 - Kelime Silme")
	print("3 - Tüm Kelimeleri Listeleme")
	print("4 - Çıkış")
	secim = int(input("Lütfen yapmak istediğiniz işlemin numarasını yazınız: "))

	if secim == 1:
		while True:
			kelime = input("Lütfen aramak istediğiniz kelimeyi giriniz (Çıkış=Q): ").lower()

			if kelime in dictionary.keys():
				print(f"Girdiğiiz \"{kelime}\" kelimesinin ENG dilindeki karşılığı \"{dictionary[kelime]}\"")
			elif kelime == "q":
				print("Çıkış yapılıyor...")
				break
			else:
				secim = input("Bu kelime sözlükte bulunmuyor. Kelimeyi eklemek ister misiniz(E/H): ").lower()
				if secim == "e":
					key = input("Lütfen eklemek istediğiniz kelimenin TR karşılığını giriniz: ").lower()
					value = input("Lütfen eklemek istediğiniz kelimenin ENG karşılığını giriniz: ").lower()

					dictionary[key] = value
					print(f"TR: {key} \t => ENG: {value}")

				elif secim == "h":
					continue
				else:
					print("Lütfen geçerli bir cevap giriniz.")
					continue

	elif secim == 2:
		while True:
			kelime = input("Lütfen silmek istediğiniz kelimeyi giriniz (Çıkış=Q): ").lower()

			if kelime in dictionary.keys():
				dictionary.pop(kelime)
				print("Kelime silindi.")
				break
			elif kelime == "q":
				print("Çıkış yapılıyor...")
				break
			else:
				print("Sözlükte bulunmayan bir kelime girdiniz. Lütfen tekrar deneyin.")
				continue

	elif secim == 3:
		for k, v in dictionary.items():
			print(f"TR: {k} \t=> ENG: {v}")
		print("\n")

	elif secim == 4:
		 break