
toplam = 0 # istediğimiz sayıların toplamını tutacak değişken

for i in range(0,1000):
    if i % 3 == 0 or i % 5 == 0: # 3 veya 5'in katı olan sayıları kontrol ediyoruz
        toplam += i # bu sayıları toplama ekliyoruz

print(toplam) #for'un hizasında yazma sebebimiz aradaki işlemleri değil direkt sonucu görmek eğer if'in altında yazarsak tüm adımları görürüz
