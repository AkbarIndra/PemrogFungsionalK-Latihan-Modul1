random_list = [105, 3.1, "Hello", 737, "Phyton", 2.7, "World", 412, 5.5, "AI"]

# Membuat struktur untuk menyimpan data terpisah
int_data = {}
float_data = ()
str_data = []

# Memisahkan data
for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item % 100) // 10
        ratusan = item // 100
        int_data[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float):
        float_data += (item,)
    elif isinstance(item, str):
        str_data.append(item)

# Menampilkan hasil
print("Data Integer (dalam bentuk dictionary):")
for key, value in int_data.items():
    print(f"{key}: ratusan={value[0]}, puluhan={value[1]}, satuan={value[2]}")

print("\nData Float (dalam bentuk tuple):")
print(float_data)

print("\nData String (dalam bentuk list):")
print(str_data)