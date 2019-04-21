"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

i = 2
j = 0
n = 600851475143
l = []
z = []
for i in range(2, int(n**0.5)):
    if n % i == 0:
        l.append(i)
print(l)
for k in range(len(l)-1):
    a = 2
    b = 0
    while a**2 <= l[k] and b !=1:
        if l[k] % a == 0:
            b = 1
        a += 1
    if b != 1:
        z.append(l[k])
        z_max = max(z)
print(z_max)








