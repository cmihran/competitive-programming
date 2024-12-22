def pretty_print(matrix):
    for row in matrix:
        print(''.join(row))
    print()

def build_matrix(lines):
    matrix = []
    for line in lines:
        row = []
        for c in line:
            if c != '\n':
                row.append(c)
        matrix.append(row)
    m = len(matrix)
    n = len(matrix[0])
    return n, m, matrix
