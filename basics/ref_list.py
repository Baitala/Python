a = [1]
a.append([2])
print("a =", a)
a[1].append([3, a])
print("a =", a)

b = [1]
b.append(2)
print("b =", b)

c = [1]
c.append([2])
c[1].append([3, None])
print("c =", c)
p = c
while p is not None:
    print(p[0])
    p = p[1]

