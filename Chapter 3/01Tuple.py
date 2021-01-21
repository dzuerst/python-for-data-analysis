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



