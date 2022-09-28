# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
modal = float(input("Tuliskan Modal Tabungan / Pinjaman Awal: "))
persenbunga = float(input("Tuliskan Persentase Bunga Pertahunan: "))
waktu = float(input("Tuliskan Waktu: "))

# Mengkonversi
bunga = persenbunga * modal * waktu
total = modal + bunga

# Menampilkan Hasil
print('==========================================================')
print('Maka Besar Bunga = Rp. %d' %(bunga))
print('Maka Total Tabungan / Pinjaman Akhir  = Rp. %d' %(total))
print('==========================================================')
