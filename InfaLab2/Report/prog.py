import re
from functools import reduce
bits= [int(i) for i in input()]
a=[]
cr = 1
ci = 1
for i in range(len(bits)):
    if i+1 & i == 0: #проверяем является ли i степению 2
        a.append(f"r{cr}")
        cr+=1
    else:
        a.append(f"i{ci}")
        ci+=1
f = reduce(lambda x,y: x^y,[i for i, bit in enumerate(bits,1) if bit])
if f != 0:
    print(f"Ошибка в бите {a[f-1]}")
    bits[f - 1] = int(not bits[f - 1])
else:
    print(f"Ошибок нет")
print(f"Правильное сообщение:{''.join([str(bits[i]) for i in range(len(bits)) if not(re.match(r'^r', a[i]))])}")

