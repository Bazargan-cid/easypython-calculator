#fungsi untuk penjumlahan
def add(x, y):
    return x + y
#fungsi untuk pengurangan
def subtract(x, y):
    return x - y
#fungsi untuk perkalian
def multiply(x, y):
    return x * y    
#fungsi untuk pembagian
def divide(x, y):

    #menangani pembagian dengan nol
    if y == 0:
        return "Tidak bisa dibagi dengan nol!"
    return x / y
    
#menampilkan menu operasi
print("Pilih Operasi.")
print("1. Add") 
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#meminta input dari pengguna
while True: # Loop ini akan membuat program terus berjalan sampai ada input yang valid atau user keluar
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Input tidak valid. Mohon masukkan angka.")
            continue # Lanjut ke iterasi berikutnya (minta input lagi)

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break # Keluar dari loop setelah operasi selesai
    else:
        print("Input tidak valid. Mohon masukkan 1, 2, 3, atau 4.")