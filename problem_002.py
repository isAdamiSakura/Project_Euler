
a = 0 # Fibonacci sayılarını oluşturmak için başlangıç değerleri
b = 1

sayilar = []   # çift Fibonacci sayılarını tutacak liste


while a+b < 4_000_000: # Fibonacci sayılarını 4 milyonun altında olacak şekilde oluşturuyoruz

  a,b = b, a + b #Fibonacci sayılarını oluşturuyoruz. En çok uğraştığım yer aslında baya basitmiş syntax bilmek önemli unutmamak için pratik şart

  if b % 2 == 0: # çift sayıları kontrol ediyoruz
        sayilar.append(b) # çift sayıları listeye ekliyoruz

print(sum(sayilar)) # çift sayıların toplamını ekrana yazdırıyoruz

