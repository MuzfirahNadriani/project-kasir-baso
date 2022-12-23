def fungsimenu():
    pembeli = input("Masukkan nama Pembeli: ")
    print ("Nama Pembeli :", pembeli) 

    def rmakanan():
        global totalmakan
        global porsi
        global makan
        print ("----------------- Menu Makanan -----------------")
        print("1. Bakso Krakatau - Rp 30000")
        print("2. Bakso Urat - Rp 15000")
        print("3. Bakso Sultan - Rp 50000")
        print("4. Bakso Atom - Rp 20000")
        nomor=int(input("Masukan Pilihan: "))
        porsi= int(input("Berapa Porsi: "))
    
        if nomor==1:
            totalmakan=porsi*30000
            print (porsi," porsi Bakso Krakatau = Rp", totalmakan)
            makan=("Bakso Krakatau")
        elif nomor==2:
            totalmakan=porsi*15000
            print (porsi," porsi Bakso Urat = Rp", totalmakan)
            makan=("Bakso Urat")
        elif nomor==3:
            totalmakan=porsi*50000
            print (porsi, " porsi Bakso Sultan = Rp", totalmakan)
            makan=("Bakso Sultan")
        elif nomor==4:
            totalmakan=porsi*20000
            print (porsi, " porsi Bakso Atom = Rp", totalmakan)
            makan=("Bakso Atom")
        else:
            print("Pilihan tidak ada, silahkan masukan lagi!!")
            rmakanan()

    def rminuman():
        global totalminum
        global minum
        global gelas
        print("----------------- Menu Minuman -----------------")
        print("1. Es teh Manis - Rp 5000")
        print("2. Es jeruk - Rp 7000")
        print("3. Es Kelapa Muda - Rp 15000")
        nomor=int(input("Masukan Pilihan: "))
        gelas= int(input("Berapa Gelas: "))

        if nomor==1:
            totalminum=gelas*5000
            print (gelas," Es Teh Manis = Rp", totalminum)
            minum=(" Gelas Es Teh")
        elif nomor==2:
            totalminum=gelas*7000
            print (gelas, " Gelas Es Jeruk = Rp", totalminum)
            minum=("Es Jeruk")
        elif nomor==3:
            totalminum=gelas*15000
            print (gelas, " Gelas Es Kelapa Muda = Rp", totalminum)
            minum=("Es Kelapa Muda")
        else:
            print("Pilihan tidak ada, silahkan masukan lagi!!")
            rminuman()

    rmakanan()
    rminuman()
    totalsemua=totalmakan+totalminum

    

    if totalsemua >=100000:
        diss = totalsemua * 0.05
        pajak = totalsemua * 0.10
        total = totalsemua - diss + pajak
    
    else:
        diss = 0
        pajak = totalsemua * 0.10
        total = totalsemua - diss + pajak

    print("\nTotal harus Dibayar: Rp",total)
    uang=int(input("Uang Tunai Pembeli: Rp "))
    kembalian=int(uang-total)
    print("Kembalian :",kembalian)
    


    print("\n==================================")
    print("========== S T R U K   B E L I =========")
    print("==================================")
    print ("Nama\t\t:",pembeli)
    print ("Beli\t\t:",porsi,makan,"( Rp", totalmakan,")")
    print ("\t\t ",gelas,minum,"( Rp", totalminum,")")
    print ("Tagihan\t\t: Rp",totalsemua)
    print ("Disscount\t: Rp",diss)
    print ("Pajak\t\t: Rp",pajak)
    print ("Harga Akhir\t: Rp",total)
    print ("Dibayar\t\t: Rp",uang)
    print ("Kembalian\t: Rp",kembalian)
    print("==================================")
    print("==================================")
    input_j2 = input("Pesan Lagi?: (Y/N) ")
    j2 = str(input_j2)
    if j2 == "Y" or j2 == "y":
        fungsimenu()
    elif j2 == "N" or j2 == "n":
        print ("Semoga Hari Mu Menyenangkan! ")
        quit()

kondisi = True

while (kondisi == True):
    fungsimenu()