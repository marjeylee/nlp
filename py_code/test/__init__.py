a = {}
for i in range(10000000):
    a[str(i)] = i

for i in range(10000000):
    print(a[str(i)])
