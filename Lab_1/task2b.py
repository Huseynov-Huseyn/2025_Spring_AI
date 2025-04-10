import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
print("1:", s1)

s1.index = ['w', 'x', 'y', 'z']
print("2:", s1)

s2 = pd.Series({'p': 5, 'q': 10, 'r': 15})
print("3:", s2)

print("4:", s2['q'])

print("5:", s1[s1 > 25])

print("6:", s1[s1 > 20] / 10)

df1 = pd.DataFrame([(1, 2), (3, 4)])
print("7:", df1)

df1.index = ['r1', 'r2']
df1.columns = ['c1', 'c2']
print("8:", df1)

df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print("9:", df2)

print("10:", df2[df2['A'] > 1])
