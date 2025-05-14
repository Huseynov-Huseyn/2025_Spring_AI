# 1) x-in müsbət, mənfi və ya sıfır olub-olmaması
x = -4
if x > 0:
    print("1) müsbət")
elif x < 0:
    print("1) mənfi")
else:
    print("1) sıfır")

# 2) n-in cüt və ya tək olması
n = 7
if n % 2 == 0:
    print("2) cüt")
else:
    print("2) tək")

# 3) a, b, c üçün ən böyüyü tapmaq
a, b, c = 5, 8, 3
print("3) Ən böyük:", max(a, b, c))

# 4) day dəyişəni ilə həftə günü
day = 5
days = {
    1: "Bazar ertəsi",
    2: "Çərşənbə axşamı",
    3: "Çərşənbə",
    4: "Cümə axşamı",
    5: "Cümə",
    6: "Şənbə",
    7: "Bazar"
}
print("4) Həftənin günü:", days.get(day, "Yanlış gün"))

# 5) Temperatur dərəcəsinə əsasən təsvir
temp = 18
if temp < 0:
    print("5) soyuq")
elif 0 <= temp <= 20:
    print("5) normal")
else:
    print("5) isti")

# 6) Şifrə uzunluğuna görə təsnifat
password = "myp@ss"
if len(password) < 8:
    print("6) qısa")
elif 8 <= len(password) <= 12:
    print("6) orta")
else:
    print("6) uzun")

# 7) x-in 3 və 5-ə bölünüb-bölünməməsi
x = 15
if x % 3 == 0 and x % 5 == 0:
    print("7) 3 və 5")
elif x % 3 == 0:
    print("7) 3")
elif x % 5 == 0:
    print("7) 5")
else:
    print("7) heç biri")

# 8) 0-dan 20-yə qədər cüt ədədləri çap et
print("8) Cüt ədədlər:")
for i in range(0, 21):
    if i % 2 == 0:
        print(i, end=' ')
print()

# 9) Verilən mətnin hərflərini ayrıca çap et
text = "Bağda ərik var idi …"
print("9) Mətnin hərfləri:")
for char in text:
    print(char)

# 10) 1-dən 10-a qədər, lakin 3 istisna olmaqla çap et
print("10) 3 istisna olmaqla 1-10:")
for i in range(1, 11):
    if i == 3:
        continue
    print(i, end=' ')
print()

# 11) İlk 5-ə bölünən ədədi while və break ilə tap
i = 1
while True:
    if i % 5 == 0:
        print("11) İlk 5-ə bölünən:", i)
        break
    i += 1

# 12) Verilən tuple-da 5-in indeksini tap
numbers = (1, 3, 5, 7, 9)
for index, num in enumerate(numbers):
    if num == 5:
        print("12) 5-in indeksi:", index)
        break
