import Rio097

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print("MATRIKS A")

for i in A:
    print(i)

print()

print("MATRIKS B")

for i in B:
    print(i)

print()

print("HASIL PERKALIAN A x B")

hasil = Rio097.kali(A, B)

for i in hasil:
    print(i)

print()

print("TRANSPOSE MATRIKS B")

hasil = Rio097.transpose(B)

for i in hasil:
    print(i)

print()

print("DETERMINAN MATRIKS A")

print(Rio097.determinan2x2(A))