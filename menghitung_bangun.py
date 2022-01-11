#menghitung bangun datar

print("=" * 20)
print("1. mencari luas")
print("2. mencari keliling")
print("=" * 20)

pilihan_awal = int(input("pilih tindakan 1/2 : "))

if pilihan_awal == 1:
    print("=" * 20)
    print("1.persegi")
    print("2.persegi panjang")
    print("3.segitiga")
    print("4.jajar genjang")
    print("=" * 20)
    
    choice = int(input("pilih bangun datar 1/2/3/4: "))
    
    if choice == 1:
        bil = int(input("masukan bilangan :"))
        luas_prg = bil ** 2
        print("hasilnya adalah " + str(luas_prg))
    
    elif choice == 2:
        num1 = int(input("masukan panjang :"))
        num2 = int(input("masukan lebar :"))
        luas_prgp = float(num1 * num2)
        print("hasilnya adalah " + str(luas_prgp))

    elif choice == 3:
        num1 = int(input("masukan alas :"))
        num2 = int(input("masukan tinggi :"))
        luas_sgt = 0.5 * num1 * num2
        print("hasilnya adalah " + str(luas_sgt))

    elif choice == 4:
        num1 = int(input("masukan alas :"))
        num2 = int(input("masukan tinggi"))
        luas_jjg = num1 * num2
        print("hasilnya adalah " + str(luas_jjg))

    else:
        print("TIDAK VALID")

elif pilihan_awal == 2:
    print("=" * 20)
    print("1.persegi")
    print("2.persegi panjang")
    print("3.segitiga")
    print("4.jajar genjang")
    print("=" * 20)

    choice2 = int(input("pilih bangun datar 1/2/3/4"))

    if choice2 == 1:
        sisi = int(input("masukan bilangan :"))
        kel_prg = 4 * sisi
        print("hasilny adalah " + str(kel_prg))

    elif choice2 == 2:
        bil1 = int(input("masukan panjang :"))
        bil2 = int(input("masukan lebar :"))
        kel_prgp = float(2 * (bil1*bil2))
        print("hasilnya adalah " + str(kel_prgp))

    elif choice2 == 3:
        bil1 = int(input("masukan bilangan A:"))
        bil2 = int(input("masukan bilangan B:"))
        bil3 = int(input("masukan bilangan C:"))
        kel_sgt = bil1 + bil2 + bil3 
        print("hasilnya adalah " + str(kel_sgt))

    elif choice2 == 4:
        bil1 = int(input("masukan bilangan A:"))
        bil2 = int(input("masukan bilangan B:"))
        kel_jjg = 2 * (bil1+bil2)
        print("hasilnya adalah " + str(kel_jjg))

    else:
        print("TIDAK VALID")

else:
    print("TIDAK DAPAT DI PROSES")