#kalkulator dengan fungsi def
print("KALKULATOR SEDERHANA")
print("=" * 30)
print("1.penjumlahan \t [+]")
print("2.pengurangan \t [-]")
print("3.perkalian \t [*]")
print("4.pembagian \t [/]")

opsi = int(input("pilih operasi yang ingin anda lakukan (1/2/3/4) :"))
num1= int(input("masukan bilangan pertama : "))
num2 = int(input("masukan bilangan kedua : "))

def tambah(num1,num2):
    return num1 + num2
def kurang(num1,num2):
    return num1 - num2
def kali(num1,num2):
    return num1 * num2
def bagi(num1,num2):
    return num1 / num2

if opsi == 1:
    print("\nuser memilih penjumlahan")
    print("HASILNYA ADALAH {}" .format(tambah(num1,num2)))
elif opsi == 2:
    print("\nuser memilih pengurangan ")
    print("HASILNYA ADALAH {}" .format(kurang(num1,num2)))
elif opsi == 3:
    print("\nuser memilih perkalian ")
    print("HASILNYA ADALAH {}" .format(kali(num1,num2)))
elif opsi == 4:
    print("\nuser memilih pembagian")
    print("HASILNYA ADALAH {}" .format(bagi(num1,num2)))
else:
    print("INPUT YANG ANDA MASUKAN SALAH !!!")