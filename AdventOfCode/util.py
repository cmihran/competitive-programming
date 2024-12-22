def pretty_print(matrix):
    # Print column indices with left alignment
    col_indices = '   | ' + ' '.join(f'{i:<2}' for i in range(len(matrix[0])))
    print(col_indices)
    print('-' * len(col_indices))

    # Print rows with row indices and padding
    for row_idx, row in enumerate(matrix):
        row_label = f'{row_idx:<2} | '
        print(row_label + ' '.join(f'{cell:<2}' for cell in row))
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
    return m, n, matrix
