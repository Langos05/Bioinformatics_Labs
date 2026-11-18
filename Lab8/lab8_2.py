def f(a, b, match, mismatch):
    if a == b:
        return match
    return mismatch

def align(s1, s2, match=2, mismatch=-2, gap=-2):
    n = len(s1)
    m = len(s2)
    matrix = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        matrix[i][0] = i * gap
    for j in range(m + 1):
        matrix[0][j] = j * gap

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = matrix[i - 1][j - 1] + f(s1[i - 1], s2[j - 1], match, mismatch)
            top = matrix[i - 1][j] + gap
            left = matrix[i][j - 1] + gap
            matrix[i][j] = max(diag, top, left)

    align1 = ""
    align2 = ""
    i = n
    j = m

    while i > 0 or j > 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + f(s1[i - 1], s2[j - 1], match, mismatch):
            align1 = s1[i - 1] + align1
            align2 = s2[j - 1] + align2
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + gap:
            align1 = s1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            align1 = "-" + align1
            align2 = s2[j - 1] + align2
            j -= 1

    return matrix, align1, align2

s1 = "GAACGTTTC"
s2 = "GAAGTCTA"

matrix, a1, a2 = align(s1, s2)

for row in matrix:
    print(row)

print(a1)
print(a2)