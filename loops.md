```
for i in range(10):
    print(i)
```

```
i = 0
while i < 10:
    print(i)
    i += 1
```

```
one2ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in one2ten:
    print(i+1)
```

```
for i in range(10):
    print(i+1)
else:
    print("for-else")
```

```
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("while-else")
```

```
from math import pi, sin
theta = 0
while True:
    if sin(theta) < 1:
        continue
    else:
        break
        print(f"theta: {theta} | sin(theta) = 1")

    theta += 1*(pi/180)
```
