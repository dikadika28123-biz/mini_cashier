
print("================================")
print("        MINI CASHIER")
print("================================")

barang1 = input("Masukkan nama barang pertama : ")
harga1 = int(input("Masukkan harga barang pertama : "))
jumlah1 = int(input("Masukkan jumlah barang pertama : "))

total = harga1 * jumlah1

print("\n========== STRUK BELANJA ==========")
print(f"Nama barang   : {barang1}")
print(f"Harga barang  : Rp{harga1}")
print(f"Jumlah        : {jumlah1}")
print(f"Total belanja : Rp{total}")
print("=================================")
print("Terima kasih telah berbelanja!")
