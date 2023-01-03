username = ["brucewyne", "victorstone", "ciscoramon"]
print ("=" *42)
print ("*" *13, "Justice League", "*" *13)
print ("=" *42)

login = input(str("Masukkan username anda: "))
user=login.lower()
member=[]

while True:
    if user in username:
        print()
        print ("=" *5, "WELCOME ", user, "=" *5)
        print ("1. Tambah Anggota Justice League")
        print ("2. Hapus Anggota Justice League")
        print ("3. Tampilkan Anggota Justice League")
        print ("4. Exit")
        p1 = int(input("Masukkan pilihan anda: "))
        if (p1==1):
            add = input("Nama anggota baru:")
            member.append(add)
            print("Data", "'", add,"'","berhasil ditambahkan")
            print(member)
        elif (p1==2):
            hapus = (input("Anggota yang akan dihapus: "))
            if hapus not in member:
                print ("data", "'", hapus, "'", "tidak ditemukan")
            else:
                member.remove(hapus)
                print("data" , "'", hapus, "berhasil dihapus")
                print(member)
        elif (p1==3):
            print ("Daftar Anggota Justice League: ")
            for i in member:
                print ("|", i, end = '|')
        elif (p1==4):
            print ("see u next time MR.", login, "GLFH")
    else:
        print ("Access Denied")
        break