#Latihan perulangan membuat segitiga

sisi = 9

# 1. Menggunakan For

# dummy variable
print("awal for")
count = 1
for i in range(sisi):
  print("*"*count)
  count += 1

print("akhir for")

# 2. Menngunakan While

print("awal while")
count = 1
while True:
  print("*"*count)
  count += 1

  if count > sisi:
    break

print("akhir while")

# 3. hanya ganjil saja

print("awal while")
count = 1
spasi = int(sisi/2)
while True:
  # akan break jika count melebihi sisi
  if count > sisi:
    break

  if(count%2):
    # print jika ganjil
    print(" "*spasi,"*"*count)
    spasi -= 1
    count += 1
  else:
    # akan kembali ke atas jika ganjil
    count += 1
    continue

print("akhir while")

# 4. belah ketupat

print("belah ketupat")
count = 1
spasi = int(sisi/2)
while True:
  if(count%2):
    # print jika ganjil
    print(" "*spasi,"*"*count)
    spasi -= 1
    count += 1
  else:
    # akan kembali ke atas jika ganjil
    count += 1

  # akan break jika count melebihi sisi
  if count > sisi:
    break

# Mencetak pola kedua belah ketupat
count -= 2 
spasi = 1
while count > 0:
  if(count%2):
    # print jika ganjil
    print(" "*spasi,"*"*count)
    spasi += 1
    count -= 1
  else:
    # akan kembali ke atas jika ganjil
    count -= 1

print("akhir belah ketupat")