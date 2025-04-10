a = 123
a_str = str(a)
print("1:", a_str, type(a_str))

b = 19.99
b_int = int(b)
print("2:", b_int)

c = "500"
c_num = int(c)
print("3:", c_num / 2)

a = 8
b = 12
print("4: a < b =", a < b)
print("4: a == b =", a == b)

x = 5
y = 10
z = 15
print("5:", (x < y) and (y < z))

print("6: Tam bölmə =", 25 // 4)
print("6: Qalıq =", 25 % 4)
print("6: Adi bölmə =", 25 / 4)

print("7:", 3 ** 4)

qiymet = 75.5
qiymet_int = int(qiymet)
print("8:", qiymet_int, type(qiymet_int))

n = 20
print("9: (n > 10) or (n < 5) =", (n > 10) or (n < 5))
print("9: (n > 15) and (n < 25) =", (n > 15) and (n < 25))

val = "42.8"
val_float = float(val)
print("10: Float-a çevirildi:", val_float, type(val_float))
val_int = int(val_float)
print("10: Tam ədədə çevirildi:", val_int, type(val_int))
