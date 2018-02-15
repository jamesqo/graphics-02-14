import math


def print_matrix( matrix ):
    print("This is a {0}x{1} matrix".format(len(matrix), len(matrix[0])))
    for r in range(len(matrix)):
        row = matrix[r]
        print(str(row))

def ident(matrix):
    assert(len(matrix) == len(matrix[0]))

    for r in range(len(matrix)):
        row = matrix[r]
        for c in range(len(row)):
            if c == r:
                row[c] = 1
            else:
                row[c] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    assert(len(m1[0]) == len(m2))
    
    m3 = new_matrix(rows=len(m1), cols=len(m2[0]))
    for r in range(len(m2)):
        m2row = m2[r]
        m1row = m1[r]
        for c in range(len(m2row)):
            # Should be row r of m1 dotted with column c of m2
            m2col = [other_m2row[c] for other_m2row in m2]
            print("DEBUG: dotting {0} with {1}".format(m1row, m2col))
            m3[r][c] = dot(m1row, m2col)

    return m3

def dot(v1, v2):
    assert(len(v1) == len(v2))

    result = 0
    for c1, c2 in zip(v1, v2):
        result += c1 * c2
    return result


# Indexed by column no, then by row no
def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m
