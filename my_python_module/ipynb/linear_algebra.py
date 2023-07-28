from . import np 


def swap_rows(m, row_num_1, row_num_2):
    """
    Gaussian elimination basic operation 1
    """
    m_new = m.copy()
    m_new[[row_num_1, row_num_2]] = m_new[[row_num_2, row_num_1]]
    return m_new


def multiply_row(m, row_num, row_num_multiple):
    """
    Gaussian elimination basic operation 2
    """
    m_new = m.copy()
    m_new[row_num] = m_new[row_num] * row_num_multiple
    return m_new
    

def add_rows(m, row_num_1, row_num_2, row_num_1_multiple):
    """
    Gaussian elimination basic operation 3
    """
    m_new = m.copy()
    m_new[row_num_2] = row_num_1_multiple * m_new[row_num_1] + m_new[row_num_2]
    return m_new

def solve(m, b):
    return np.linalg.solve(m,b)

def determinant(m):
    return np.linalg.det(m)

def combine_system(m,b):
    return np.hstack((m, b.reshape(b.size, 1)))


