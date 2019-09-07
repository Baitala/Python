#else выполняется после нормального завершения
#если вышли через break то else пропускается
x=10
while x>0:
    print(x)
    x=x-1
    if x == 5:
        continue #прервать итерацию, пойти на следующую итерацию

    if x == 1:
        break #выйти минуя else
else:
    print("While ended OK.")

print(x)