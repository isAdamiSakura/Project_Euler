
sayi = 600851475143

bölen = 2 

while sayi > 1:
   if sayi % bölen == 0:
     sayi = sayi // bölen
   else:
     bölen += 1

print(bölen)