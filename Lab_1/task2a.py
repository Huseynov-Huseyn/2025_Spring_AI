reqemler = [5, 10, 15, 20]
print("1:", reqemler)

print("2:", len(reqemler))

reqemler.append(25)
print("3:", reqemler)

reqemler.insert(2, 12)
print("4:", reqemler)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
birlesmis = list1 + list2
print("5:", birlesmis)

print("6:", reqemler[2:4])

reqemler[0] = 50
print("7:", reqemler)

print("8:", 19 in reqemler)

letters = ["a", "b", "a", "c"]
print("9:", letters.count("a"))

letters2 = ["x", "y", "x", "z"]
letters2 = [i for i in letters2 if i != "x"]
print("10:", letters2)

nums = [7, 2, 9, 1]
nums.sort(reverse=True)
print("11:", nums)

boyuk_10 = [i for i in reqemler if i > 10]
print("12:", boyuk_10)
