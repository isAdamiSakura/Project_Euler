
toplam = 0 # istediğimiz sayıların toplamını tutacak değişken

for i in range(1, 706_000, 2): # 1'den 706.000'e kadar olan tek sayıları alıyoruz
      a = i**2 # her bir tek sayının karesini alıyoruz
      toplam += a # karelerin toplamını hesaplıyoruz
print(toplam) # sonuç olarak toplamı ekrana yazdırıyoruz

