# Sukurkite funkciją, kuri sudaugintų (NxN) matricas (two dimensional arrays) ir gražintų rezultatą.

# 🤷‍♂️ Čia nėra jokių konkrečių nurodymų 🤷‍♂️ Pagalvokite, ką darytumėte, jei jums būtų duota tokia užduotis darbe.

matrix1 = [[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]]
matrix2 = [[10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]]

result = [[0 for x in range(3)] for y in range(3)]

def multiplyMmatrix(matrix1, matrix2):

    for a in range(len(matrix1)):
        for b in range(len(matrix2[0])):
            for c in range(len(matrix2)):
			
                result[a][b] += matrix1[a][c] * matrix2[c][b]
    return result

print (multiplyMmatrix(matrix1, matrix2))

