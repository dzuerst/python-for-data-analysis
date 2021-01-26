# list sama seperti tompel
# bisa menyimpan banyak data pada suatu variabel
# bedanya list ini lebih open minded, elemen-elemennya bisa diubah (mutable)
# ga kayak tompel tuh yang konservatif, ga mau berubah isinye wkwk

# ngebikin list kaga ribet, tambahin aja kurung siku
# sistem bakal kenal tuh, ohh ini list toh..
# kalo kurung biasa, sistem bakal mengidentifikasiin variabel tersebut sebagai tuple
a_list = [10,20,30,40,50]
print(a_list)

# kita bisa ngedit elemen yang ada di list
# of course hal ini gak bisa lu lakuin di tuple yang konservatif wkwk..
a_list[2] = 25
print(a_list)

# karena list open minded, dia juga bisa nambahin elemen-elemen baru pada variabelnya
# jadi elemen yang dia punya gak itu-itu aja
# dan elemen yang lu mau tambahin gak harus angka, bisa juga yang lain
# suka-suka lu deh asal gak error oghey?

a_list.append("Sebuah ilmu baru")
print(a_list)

# list juga bisa nambahin elemen ke posisi tertentu
# fungsi yang dipake adalah insert, jika pengen nambahin elemen ke posisi terakhir
# pakenya append oghey deal ?
a_list.insert(1,"Tambahin ke indeks ke 1 nih ye")
print(a_list)

# list juga bisa ngehapus suatu elemen pada index tertentu
# pake aja function pop
a_list.pop(1)
print(a_list)

# lu juga bisa ngehapus elemen dengan value yang lu mau pake function remove oghey?
a_list.remove('Sebuah ilmu baru')
print(a_list)

# lu juga bisa cek apakah di sebuah list ada elemen yang lo cari ato gak, gini mang
# canggih kan? jelas dong, mang uler gitu loh..
print(20 in a_list)

# lu juga bisa nyatuin dua buah list
# serius? iya lah
list_a = ['a','b','c']
list_b = [1,2,3]
gabungin_list = list_a + list_b
print(gabungin_list)

# cara kedua nyatuin dua buah list
list_a.extend(['d','e','f'])
print(list_a)

# dan lu juga bisa ngurutin elemen-elemen yang ada di list
# pake fungsi sort
list_c = [1,5,3,29,25,4,3,9,12]
list_c.sort()
print(list_c)

# bahkan kerennya lagi lu bisa ngurutin kata berdasarkan jumlah hurufnya
list_d = ["suka","ngoding","gue"]
list_d.sort(key = len)
print(list_d)

# ada sebuah lib pada python yang canggih
# lib ini bisa tahu dimana index yang tepat pada elemen baru
# yang mau diinputkan agar nilai-nilai pada list tetap terurut

import bisect

list_e = [1,2,2,3,4,5,5,6,9,11]
print(bisect.bisect(list_e, 7))

# slicing
# slicing nih maksudnye kita mengambil elemen-elemen dengan range / rentang
# tertentu aje, jadi gak semuanya
# misal nih [1:5] artinya ambil elemen dari index ke 1 sampai index ke 5 [start:stop]
# ingat ye, sampai dan sampai dengan itu ga sama

list_f = [1,5,4,2,3,4,19]
list_f_slicing = list_f[1:5]
print(list_f)
print(list_f_slicing)

# btw ada beberapa cara lagi nih dalam slicing langsung liat aje nih

# ambil elemen start di awal sampe index ke 5
list_f_1 = list_f[:5]
print(list_f_1)

# ambil elemen start di 5 sampe index terakhir
list_f2 = list_f[5:]
print(list_f2)



