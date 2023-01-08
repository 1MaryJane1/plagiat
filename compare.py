import ast


def levenstein(str1, str2):
    n, m = len(str1), len(str2)
    if n > m:
        str1, str2 = str2, str1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str1[j - 1] != str2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


print("Введите путь к первому файлу")
n = str(input())
print("Введите путь ко второму файлу")
m = str(input())
with open(n) as f:
    s1 = f.read()
with open(m) as f:
    s2 = f.read()
d = (len(s1) + len(s2)) // 2
print(((d - (levenstein(s1, s2))) / d))
print((d - levenstein(ast.dump(ast.parse(s1)), ast.dump(ast.parse(s2)))) / d)