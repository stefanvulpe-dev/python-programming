def get_spiral_order_string(matrix):
    m = len(matrix)
    n = len(matrix[0])
    visited = [[0 for i in range(n)] for j in range(m)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = 0
    j = 0
    k = 0
    spiral_order = ''
    for _ in range(m * n):
        spiral_order += (str(matrix[i][j]))
        visited[i][j] = 1
        if i + di[k] < 0 or i + di[k] >= m or j + dj[k] < 0 or j + dj[k] >= n or visited[i + di[k]][j + dj[k]] == 1:
            k = (k + 1) % 4
        i += di[k]
        j += dj[k]
    return spiral_order


print(get_spiral_order_string([['f', 'i', 'r', 's'], ['n', '_', 'l', 't'], ['o', 'b', 'a', '_'], ['h', 't', 'y', 'p']]))
