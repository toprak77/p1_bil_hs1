# isimuzunluk = len(input("merhaba adın ne"))
# isimuzunluk_str = str(isimuzunluk)
# print("isminde " + isimuzunluk_str + " karakter var")
# fl = float(1.322)
# print(type(fl))
# intt = int(232)
# print(type(intt))
# st = str(123123)
# print(type(st))
# print(100 + float(15.23))
# print(str(122) +str(324))
# ikihanelisayi = str(input("iki haneli bir"))
# toplam = int(ikihanelisayi[0]) + int(ikihanelisayi[1])
# print("toplam: " + str(toplam))
# print(2 * 4 + 6 / 3 - 2)
# boy = float(input("boyunu gir (m): "))
# kilo = float(input("kilonu gir (kg): "))
# vki = int(kilo/boy**2)
# print("vücut kitle indeksiniz: " + str(vki))
# print(8/3)
# print(type(8/3))
# print(8//3)
# print(type(8//3))
# result = 8/4
# result /= 2
# print(result)
# sayi = 5
# sayi = sayi+1
# print(sayi)
# print("sayı =" +str(sayi))
# print(f"sayı= {sayi}") #FString
# yas = input("kaç yaşındasın")
# yas_int = int(yas)
# ay = yas_int * 12
# hafta = yas_int * 52
# gun = yas_int *365
# print(f"{ay} aylıksın")
# print(f"{hafta} haftalıksın")
# print(f"{gun} günlüksün")
# print("lunaparka hoşgeldin")
# print("biletler yetişkin 10 12 den küçükler 5tl")
# boy = int(input("boyunu gir (cm)"))
# yas = int(input("yaşını gir"))
# biletfiyati = 0
# if boy > 80 :
#     if(yas < 12):
#         biletfiyati = 5
#     else:
#         biletfiyati = 10
#     print(f"çarpışan arabaya binebilirsin fiyat {biletfiyati} tl")
# elif boy > 80 and boy < 120:
#     if(yas < 12):
#         biletfiyati = 5
#     else:
#         biletfiyati = 10
#     print(f"trene binebilirsin {biletfiyati} tl")
# elif boy > 120 and boy < 140:
#     if(yas > 12):
#         biletfiyati = 5
#     else:
#         biletfiyati = 10
#     print(f"gondola binebilirsin fiyat {biletfiyati} tl")
# elif boy > 140:
#     if(yas < 12):
#         biletfiyati = 5
#     else:
#         biletfiyati = 10
#     print(f"Kamikazeye binebilirsiniz! Fiyat {biletfiyati} TL")
# else:
#     print("Lunaparkta herhangi bir araca binmek için boyunuz yetmiyor!")
# sayi = int(input("tek mi çift mi olduğunu öğrenmek için bir sayı gir"))
# kalan = sayi % 2
# if kalan == 0:
#     print("sayın çift")
# else:
#     print("sayın tek")
# boy  = float(input("Boyunuzu giriniz (m): "))
# kilo = float(input("Kilonuzu giriniz (kg):"))
# vki = int(kilo/boy**2)
# if vki < 18.5:
#     print(f"Vücut Kitle İndeksiniz: {vki} , Zayıfsınız!")
# elif vki > 18.5 and vki < 25:
#     print(f"Vücut Kitle İndeksiniz: {vki} , Kilonuz Normal")
# elif vki > 25 and vki < 30:
#     print(f"Vücut Kitle İndeksiniz: {vki} , Kilolusunuz")
# elif vki > 30 and vki < 35:
#     print(f"Vücut Kitle İndeksiniz: {vki} , Obezsiniz")
# elif vki > 35:
#     print(f"Vücut Kitle İndeksiniz: {vki} , Aşırı Kilolusunuz")
yil = int(input("hangi yılı kontrol etmek istiyorusnuz"))
if yil % 4 == 0:
    if yil % 100 == 0:
        if yil %400 == 0:
            print(f"{yil}bir artık yıldır")
        else:
            print(f"{yil} bir artık yıl değildir!.")
    else:
         print(f"{yil} bir artık yıl değildir!.")
else:
     print(f"{yil} bir artık yıl değildir!.")