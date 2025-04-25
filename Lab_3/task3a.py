x = -4
if x > 0:
    print("müsbət")
elif x < 0:
    print("mənfi")
else:
    print("sıfır")

n = 7
if n % 2 == 0:
    print("cüt")
else:
    print("tək")

a, b, c = 15, 22, 13
print("Ən böyük:", max(a, b, c))

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
print(days.get(day, "Yanlış gün"))

temp = 18
if temp < 0:
    print("soyuq")
elif 0 <= temp <= 20:
    print("normal")
else:
    print("isti")

password = "123456789"
length = len(password)
if length < 8:
    print("qısa")
elif 8 <= length <= 12:
    print("orta")
else:
    print("uzun")

x = 15
if x % 3 == 0 and x % 5 == 0:
    print("3 və 5")
elif x % 3 == 0:
    print("3")
elif x % 5 == 0:
    print("5")
else:
    print("heç biri")

for i in range(0, 21):
    if i % 2 == 0:
        print(i)

text = "Bağda ərik var idi …"
for ch in text:
    print(ch)

for i in range(1, 11):
    if i == 3:
        continue
    print(i)

i = 1
while True:
    if i % 5 == 0:
        print(i)
        break
    i += 1

nums = [1, 3, 5, 7, 9]
for index, value in enumerate(nums):
    if value == 5:
        print("İndeks:", index)
        break
