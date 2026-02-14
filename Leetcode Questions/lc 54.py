matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    res = []
    top, left = 0, 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # traverse top row
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1

        # traverse right column
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        # traverse bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        # traverse left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res

print(spiral_matrix(matrix))
# [1, 2, 3, 6, 9, 8, 7, 4, 5]