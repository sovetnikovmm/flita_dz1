def f(i):
    if i == 0:
        return '0'
    if i < 0:
        return '-' + f(abs(i))
    n = ''
    while i > 0:
        x = str(i % 2)
        n = x + n
        i = int(i) // 2
    return n


def check_digit(string: str):
    if not string.isdigit() and string[0] == '-':
        return string[1::].isdigit()
    else:
        return string.isdigit()

s = int(input("Введите количество вводимых элементов:"))
set10 = set(input("Введите элемент множества десятичных чисел:") for a in range(s))
set10 = set(b for b in set10 if check_digit(b))
set10 = set(int(c) for c in set10)
set2 = set()
for i in set10:
    set2.add(f(i))
print("Множество десятичных чисел:", sorted(set10))
print("Множество двоичных чисел:", sorted(set2))
