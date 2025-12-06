import sys, time

_list = []
while True:
    _list = list(map(int, input("Введите массив из 6 пар через пробел: ").split()))
    if len(_list) == 12:
        break

_list = [[_list[i], _list[i + 1]] for i in range(0, len(_list) - 1, 2)]
timer1 = time.time()
max_num = 0
for a in range(0, len(_list) - 1):
    for b in range(0, len(_list[a]) - 1):
        if _list[a][b] > _list[a][b + 1]:
            if _list[a][b] % 5 != 0:
                max_num += _list[a][b]
            else:
                if _list[a][b + 1] % 5 != 0:
                    max_num += _list[a][b + 1]
                else:
                    print(0)
                    sys.exit()
        else:
            if _list[a][b + 1] % 5 != 0:
                max_num += _list[a][b + 1]
            else:
                if _list[a][b] % 5 != 0:
                    max_num += _list[a][b]
                else:
                    print(0)
                    sys.exit()
                    
print(max_num)
print(f"Время: {time.time() - timer1}")

timer2 = time.time()
max_num = 0
min_num = 0
for a in range(0, len(_list) - 1):
    max_num += max(_list[a])
    min_num += min(_list[a]) % 5 == 0
    
print(max_num - min_num)
print(f"Время: {time.time() - timer2}")
