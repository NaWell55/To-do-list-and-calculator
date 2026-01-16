import math

isim = input("İsminizi Girin: ")
yas = int(input("Yaşınızı Girin: "))
if (yas > 90) or (yas < 9):
    print("Lütfen gerçek yaşınızı giriniz")
elif (yas < 90) or (yas > 9):
    print("Hoşgeldin " + isim.title() + " " + "Yaşın: " + str(yas))
    while True:
        print("""\n--- MENÜ ---
        1- Yapılacak ekle
        2- Yapılacak Listesi
        3- Yapılacak Sil
        4- Hesap makinesi 
        5- Çıkış""")

        secim = input("Seçiminizi girin (1-6): ")

        if secim == "1":
            print("""\n--- Yapılıcak Ekle ---""")

            YapilacakEkle = input("Ne eklemek istersiniz: ")

        elif secim == "2":
            print("""\n--- Yapılacak Listesi ---""")
            print(str(YapilacakEkle).title())


        elif secim == "3":
            print("""\n--- Yapılacak Sil ---""")
            YapilacakSil = input(YapilacakEkle.title() + " Adlı Yapılacağınızı silmek istiyor musunuz?(Evet, Hayır): ")
            if YapilacakSil == "Evet":
                YapilacakEkle = ""
                print("Yapılacak silindi.")

        elif secim == "4":
            print("""\n--- Hesap makinesi ---""")
            sayi1 = int(input("1. Sayıyı Giriniz: "))
            sayi2 = int(input("2. Sayıyı Giriniz: "))
            islemsecim = input("""İşlem Seçiniz
            (Çıkmak için "Çık" yazın)
            1-Toplama
            2-Çıkarma
            3-Çarpma
            4-Bölme
            5-Üssünü Alma
            6-Karekök Alma
            Seçiminiz: """)
            if islemsecim == "1":
                print(sayi1 + sayi2)
            elif islemsecim == "2":
                print(sayi1 - sayi2)
            elif islemsecim == "3":
                print(sayi1 * sayi2)
            elif islemsecim == "4":
                if sayi1 or sayi2 == 0:
                    print("0'a bölemezsin")
                else:
                    print(sayi1 / sayi2)

                if sayi1 or sayi2 == 0:
                    print("0'a bölemezsin")
            elif islemsecim == "5":
                print(sayi1 ** sayi2)
            elif islemsecim == "6":
                karekok = int(input("Karekök almak istediğiniz sayıyı girin: "))
                print(math.sqrt(karekok))
            elif islemsecim == "Çık":
                print()
            else:
                print("Yanlış bir rakam yazdınız")
        elif secim == "5":
            cikis = input("Çıkmak istediğinze emin misiniz?(Evet, Hayır): ")
            if cikis == "Evet":
                print("Güle Güle...")
                break

else:
    print("Yanlış karakter(ler) kullandınız bir daha deneyiniz...")
