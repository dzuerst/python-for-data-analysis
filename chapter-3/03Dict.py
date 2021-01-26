# Dict
# Dict ini termasuk struktur data yang penting pake banget di python
# Dict biasanya juga bisa dipanggil hash map atau juga array assosiatif
# Nilainya berisi pasangan key-value yang merupakan sebuah objek
# untuk ngebuat sebuah dict kita perlu kurawal buka dan kurawal tutup {} curly braces bahasa linggisnya

dict_a = {'nama':'Dicky P.', 'kebangsaan':'Indonesia'}
print(dict_a)

# kita bisa insert objek baru dalam sebuah dict caranya gini mang
dict_a['kecepatan'] = 93
print(dict_a)

# kita juga bisa menghapus objek yang mau kita hapus pada suatu dict
# caranya gini mang
del dict_a['kecepatan']
print(dict_a)

# kita juga bisa ngambil semua value atau key yang ada di dict

# ngambil key ye
print(dict_a.keys())

# ngambil value nih
print(dict_a.values())

