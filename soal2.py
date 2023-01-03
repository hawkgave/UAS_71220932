tiket = 25000
print ("=" *5, "Selamat datang di XXV", "=" *5)
tanggal = int(input("Masukkan tanggal hari ini: "))
genap = tanggal % 2 == 0
ganjil = tanggal % 2 != 0

print ("=" *2, "Berikut genre film yang tersedia", "=" *2)
print ("1. Horror")
print ("2. Action")

p = int(input("Silahkan pilih mau nonton film genre apa : "))
if (p==1):
    genap = tanggal % 2 == 0
    ganjil = tanggal % 2 != 0
    print ("1. The Devil's light")
    print ("2. Pengabdi Setan")
    p2 = int(input("Silahkan mau nonton film apa: "))
    if (p2==1 or p2==2):
        jumlahhor = int(input("Mau memesan tiket sebanyak: "))
        totalaan = tiket*jumlahhor
        print ("Jumlah yang harus dibayar adalah Rp.", totalaan)
    else:
        print ("Pilihan yang anda pilih tidak tersedia di bioskop ini")
elif (p==2):
    print ("1. Black Panther: Wakanda Forever")
    print ("2. Avatar: The Way of Water")
    p3 = int(input("Silahkan mau nonton film apa: "))
    if (p3==1 or p3==2):
        jumlahact = int(input("Mau memesan tiket sebanyak: "))
        totalan = tiket*jumlahact
        print ("Jumlah yang harus dibayar adalah Rp.", totalan)
    else:
        print ("Pilihan yang anda pilih tidak tersedia di bioskop ini")
else:
    print ("Pilihan yang anda pilih tidak tersedia di bioskop ini")
