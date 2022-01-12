# membuat kalkulator 

print("=" * 25)
print("KALKULATOR SEDERHANA ")
print("1.penjumlahan \t [+]")
print("2.pengurangan \t [-]")
print("3.perkalian \t [*]")
print("4.pembagian \t [/]")
print("=" * 25)

pilihan = int(input("pilih operasi yang ingin dilakukan 1/2/3/4 : "))
bil1 = int(input("masukan bilangan pertama : "))
bil2 = int(input("masukan bilangan kedua : "))

if pilihan == 1:
    print("\nuser memilih penjumlahan")
    hasil = bil1 + bil2
    print("hasil dari operasi tersebut adalah " + str(hasil))

elif pilihan == 2:
    print("\nuser memilih pengurangan")
    hasil = bil1 - bil2
    print("hasil dari operasi tersebut adalah " + str(hasil))

elif pilihan == 3:
    print("\nuser memilih perkalian")
    hasil = bil1 * bil2
    print("hasil dari operasi tersebut adalah " + str(hasil))

elif pilihan == 4:
    print("\nuser memilih pembagian")
    hasil = bil1 / bil2
    print("hasil dari operaso tersebut adalah " + str(hasil))

else:
    print("TIDAK DAPAT DILANJUTKAN")