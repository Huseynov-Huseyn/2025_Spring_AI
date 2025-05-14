import pandas as pd

# 1. s1 adlı Series yaradın
s1 = pd.Series([10, 20, 30, 40])

# 2. İndeksləri təyin edin
s1.index = ['w', 'x', 'y', 'z']

# 3. Dictionary-dən s2 adlı Series yaradın
s2 = pd.Series({'p': 5, 'q': 10, 'r': 15})

# 4. s2-dən 'q' indeksli elementi seçin
q_value = s2['q']

# 5. s1-dən 25-dən böyük elementləri seçin
greater_than_25 = s1[s1 > 25]

# 6. s1-də 20-dən böyük elementləri 10-a bölün
divided = s1[s1 > 20] / 10

# 7. ((1, 2), (3, 4)) listindən df1 adlı dataframe yaradın
df1 = pd.DataFrame([(1, 2), (3, 4)])

# 8. Sətir və sütun adlarını təyin edin
df1.index = ['r1', 'r2']
df1.columns = ['c1', 'c2']

# 9. Dictionary-dən df2 yaradın
df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['r1', 'r2'])

# 10. df2-dən 'r1' sətrini seçin
row_r1 = df2.loc['r1']

# 11. df2-də 'A' sütunu 1-dən böyük olan sətirləri seçin
filtered = df2[df2['A'] > 1]
