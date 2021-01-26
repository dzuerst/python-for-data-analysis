# Tipe data tuple (tompel)
# berisi banyak data dan datanya gak bisa diubah (immutable)
tup = 10,20,30
print(tup)

# tuple bersarang atau nested tuple (tuple dalam tuple)
nested_tup = ((10,20,30),(40,50,60))
print(nested_tup)

# Ngeakses elemen pada tuple pada indeks tertentu
print(tup[2])
print(nested_tup[0][2])

# UNPACK TUPLE
# Ngeluarin nilai dari tuple ke suatu variabel
a,b,c = tup
print(a)
print(a + b)

# Barter nilai antar 2 variabel jadi gak ribet dan gak perlu pake temp macam di c++ (bjir gibah)
a,b = 10,20
b,a = a,b
print(a)

# Saat lu unpack pake 3 variabel sedangkan tupelnya 5 elemen
# maka sisanya bakal kesimpan ke variabel terakhir oghey mamang?
# jangan lupa sisanya dikasih tanda bintang oghey
tup2 = (10,20,30,40,50,60,60)
a2,b2, *sisanye = tup2
print(sisanye)

# Ngedapetin banyak elemen yang ada di suatu tuple liat bawah mamang.
print('Ada', len(tup2), 'elemen mang pada variabel tup2, asikk!')

# Ngedapetin banyak elemen (tertentu) pada suatu tompel eh tuple
# count adalah method di tuple yang biasanya dipake
# btw len bukan dari tuple ye len itu method bawaan mang uler (python)
print('Ada', tup2.count(60), 'angka 60 pada tup2 mang!')

