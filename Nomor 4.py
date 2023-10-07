A = input()
B = input()
C = input()

Adetik= (int(A[:2])*3600)+(int(A[3:5])*60)+int(A[6:8])
Bdetik = (int(B[:2])*3600)+(int(B[3:5])*60)+int(B[6:8])
Cdetik = (int(C[:2])*3600)+(int(C[3:5])*60)+int(C[6:8])

if(Adetik<Bdetik and Adetik<Cdetik):
    mobil_tercepat = "Mobil A"
    waktu_tercepat = A
elif(Bdetik<Cdetik and Bdetik<Adetik):
    mobil_tercepat = "Mobil B"
    waktu_tercepat = B
else:
    mobil_tercepat = "Mobil C"
    waktu_tercepat = C


print(f"{mobil_tercepat} tercepat, dengan perolehan waktu {waktu_tercepat}");
