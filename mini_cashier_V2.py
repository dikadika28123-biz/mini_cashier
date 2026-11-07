print("================================")
print("        MINI CASHIER")
print("================================")

barang1 = input("Masukkan nama barang pertama : ")
harga1 = int(input("Masukkan harga barang pertama : "))
jumlah1 = int(input("Masukkan jumlah barang pertama : "))
member = input ("Apakah anda member ? Iya / Tidak : " )

total = harga1 * jumlah1
diskon = 0 

if member == "Iya" :
  if total >= 25000 :
      diskon = 0.10 
  else :
    diskon = 0.05
else : print("Tidak dapat diskon")


potongan = total * diskon 
bayar = total - potongan

print("\n========== STRUK BELANJA ==========")
print(f"Nama barang   : {barang1}")
print(f"Harga barang  : Rp{harga1}")
print(f"Jumlah        : {jumlah1}")
print(f"Total belanja : Rp{total}")
print(f"Diskon        : {diskon:.0%}")
print(f"Potongan      : Rp{potongan}")
print(f"Bayar         : Rp{bayar}")
print("=================================")
print("Terima kasih telah berbelanja!")
