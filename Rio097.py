def kali(A, B):

    if len(A[0]) != len(B):
        return "Matriks tidak dapat dikalikan"

    hasil = []

    for i in range(len(A)):

        baris = []

        for j in range(len(B[0])):

            jumlah = 0

            for k in range(len(B)):

                jumlah = jumlah + A[i][k] * B[k][j]

            baris.append(jumlah)

        hasil.append(baris)

    return hasil


def transpose(A):

    hasil = []

    for j in range(len(A[0])):

        baris = []

        for i in range(len(A)):

            baris.append(A[i][j])

        hasil.append(baris)

    return hasil


def determinan2x2(A):

    if len(A) != 2 or len(A[0]) != 2:
        return "Matriks harus 2 x 2"

    return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])